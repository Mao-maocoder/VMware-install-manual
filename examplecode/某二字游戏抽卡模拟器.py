import pygame
import random
import time
import os

# 初始化 pygame
pygame.init()

# 设置窗口大小和标题
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("原神抽卡模拟器")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)
PURPLE = (147, 112, 219)

# 设置字体
current_dir = os.path.dirname(__file__)

font_path = os.path.join(current_dir, 'fonts', 'dingliezhuhaifont-20240831GengXinBan)-2.ttf')
if os.path.exists(font_path):
    font = pygame.font.Font(font_path, 24)
    large_font = pygame.font.Font(font_path, 36)
else:
    font = pygame.font.SysFont("Arial", 24)
    large_font = pygame.font.SysFont("Arial", 36)

# 玩家初始资源
class Player:
    def __init__(self):
        self.stones = 160
        self.fate = 0
        self.pity_count = 0  # 保底计数
        self.guaranteed_up = False  # 大保底标记
        self.gacha_history = []  # 抽卡历史记录

# 输入框类
class InputBox:
    def __init__(self, x, y, w, h, prompt):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = ''
        self.txt_surface = font.render(self.text, True, self.color)
        self.active = False
        self.prompt = prompt
        self.prompt_text = font.render(prompt, True, self.color)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    # 只允许输入数字
                    if event.unicode.isdigit():
                        self.text += event.unicode
                self.txt_surface = font.render(self.text, True, self.color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.prompt_text, (self.rect.x, self.rect.y - 25))
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

# 按钮类
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.is_hovered = False

    def draw(self, screen):
        color = (min(self.color[0] + 30, 255), 
                min(self.color[1] + 30, 255), 
                min(self.color[2] + 30, 255)) if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False

# 抽卡结果类
class GachaResult:
    def __init__(self, rarity, character_type=""):
        self.rarity = rarity
        self.character_type = character_type
        self.color = GOLD if rarity == "五星" else PURPLE if rarity == "四星" else WHITE
        
    def __str__(self):
        return f"{self.rarity} {self.character_type}"

class GachaSimulator:
    def __init__(self):
        self.player = Player()
        self.single_pull_button = Button(WIDTH//2 - 220, HEIGHT - 80, 200, 50, "单抽", BLUE)
        self.ten_pull_button = Button(WIDTH//2 + 20, HEIGHT - 80, 200, 50, "十连抽", BLUE)
        self.history_button = Button(WIDTH - 120, 10, 100, 40, "历史记录", GREEN)
        self.conversion_rate = 160  # 160原石=1纠缠之缘
        self.history_page = 0  # 当前显示的历史记录页面
        self.history_per_page = 10  # 每页显示的历史记录数
        self.in_history_page = False  # 用来判断是否在历史记录页面
        self.gacha_history = [] 

    def get_user_input(self):
        input_box_stones = InputBox(250, HEIGHT // 2 - 50, 200, 40, "输入原石数量:")
        input_box_fate = InputBox(250, HEIGHT // 2 + 50, 200, 40, "输入粉球数量:")
        enter_button = Button(WIDTH // 2 - 100, HEIGHT - 100, 200, 50, "进入抽卡", BLUE)
        
        clock = pygame.time.Clock()
        running = True
        
        while running:
            screen.fill(BLACK)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                # 处理输入框事件
                input_box_stones.handle_event(event)
                input_box_fate.handle_event(event)
                
                # 点击进入抽卡按钮后跳出输入界面
                if enter_button.handle_event(event):
                    # 处理输入框的文本并更新玩家数据
                    try:
                        self.player.stones = max(0, int(input_box_stones.text))  # 更新玩家的原石数量
                        self.player.fate = max(0, int(input_box_fate.text))  # 更新玩家的粉球数量
                    except ValueError:
                        pass
                    running = False
            
            input_box_stones.draw(screen)
            input_box_fate.draw(screen)
            enter_button.draw(screen)
            
            pygame.display.flip()
            clock.tick(30)
        
        # 调试输出，确认是否同步更新
        print(f"输入的原石数量: {self.player.stones}")
        print(f"输入的粉球数量: {self.player.fate}")
        
        return True

    def pull(self):
        if self.player.pity_count >= 90:
            if self.player.guaranteed_up:
                return GachaResult("五星", "限定UP")
            else:
                result = GachaResult("五星", "限定UP" if random.random() < 0.5 else "常驻")
                if result.character_type != "限定UP":
                    self.player.guaranteed_up = True
                return result

        if self.player.pity_count >= 70:
            p_five_star = 0.1
        else:
            p_five_star = 0.006

        rand = random.random()
        if rand <= p_five_star:
            if self.player.guaranteed_up:
                self.player.guaranteed_up = False
                return GachaResult("五星", "限定UP")
            else:
                result = GachaResult("五星", "限定UP" if random.random() < 0.5 else "常驻")
                if result.character_type != "限定UP":
                    self.player.guaranteed_up = True
                return result

        if random.random() <= 0.051:
            return GachaResult("四星")

        return GachaResult("三星")

    def do_gacha(self, is_ten_pulls=False):
        pulls_needed = 10 if is_ten_pulls else 1
        fate_needed = pulls_needed
        
        # 检查粉球是否足够
        if self.player.fate < fate_needed:
            stones_needed = (fate_needed - self.player.fate) * self.conversion_rate
            if self.player.stones >= stones_needed:
                # 自动转换
                self.player.stones -= stones_needed
                self.player.fate += (stones_needed // self.conversion_rate)
            else:
                return None  # 资源不足
        
        self.player.fate -= fate_needed
        
        results = []
        four_star_count = 0  # 记录四星卡片的数量

        for _ in range(pulls_needed):
            self.player.pity_count += 1
            result = self.pull()

            # 如果结果是四星，增加四星计数
            if result.rarity == "四星":
                four_star_count += 1
            
            # 如果结果是五星，重置保底计数
            if result.rarity == "五星":
                self.player.pity_count = 0
            
            results.append(result)
            self.player.gacha_history.append(result)

        # 确保十连抽至少有一个四星卡片，并且最多有三个四星
        if is_ten_pulls:
            # 如果十连抽中没有四星，强制替换一个三星为四星
            if four_star_count == 0:
                for i in range(len(results)):
                    if results[i].rarity == "三星":
                        results[i] = GachaResult("四星")
                        break
                four_star_count = 1  # 已经插入了一个四星
            
            # 如果四星卡片超过3个，替换掉多余的四星为三星
            elif four_star_count > 3:
                for i in range(len(results)):
                    if results[i].rarity == "四星" and four_star_count > 3:
                        results[i] = GachaResult("三星")
                        four_star_count -= 1

        return results


    def draw_gacha_animation(self, results):
        if not results:
            return

        # 按照稀有度排序：五星 > 四星 > 三星
        sorted_results = sorted(results, key=lambda x: {"五星": 3, "四星": 2, "三星": 1}[x.rarity], reverse=True)
        
        screen.fill(BLACK)
        
        # 计算卡片的位置和大小
        card_width = 70
        card_height = 100
        padding = 10
        total_width = len(sorted_results) * (card_width + padding) - padding
        start_x = (WIDTH - total_width) // 2
        start_y = HEIGHT // 2 - card_height // 2

        # 逐个显示卡片的动画
        for i, result in enumerate(sorted_results):
            # 绘制卡片背景
            card_rect = pygame.Rect(start_x + i * (card_width + padding), start_y, card_width, card_height)
            pygame.draw.rect(screen, result.color, card_rect)
            pygame.draw.rect(screen, WHITE, card_rect, 2)

            # 绘制文字
            text = font.render(result.rarity, True, BLACK)
            text_rect = text.get_rect(center=(card_rect.centerx, card_rect.centery))
            screen.blit(text, text_rect)

            if result.character_type:
                type_text = font.render(result.character_type, True, BLACK)
                type_rect = type_text.get_rect(center=(card_rect.centerx, card_rect.centery + 30))
                screen.blit(type_text, type_rect)

            pygame.display.flip()
            pygame.time.delay(200)  # 每张卡片显示的延迟

        # 显示资源信息
        self.draw_resources()
        pygame.display.flip()
        pygame.time.delay(1500)

    def draw_resources(self):
        # 显示原石数量
        stones_text = font.render(f"原石: {self.player.stones}", True, WHITE)
        screen.blit(stones_text, (10, 10))

        # 显示粉球数量
        fate_text = font.render(f"粉球: {self.player.fate}", True, WHITE)
        screen.blit(fate_text, (10, 40))

        # 显示保底计数
        pity_text = font.render(f"距离保底: {self.player.pity_count}/90", True, WHITE)
        screen.blit(pity_text, (10, 70))

    def draw_history(self):
        GREY = (128, 128, 128)  # 灰色
        running = True

        # 按钮的实例化
        prev_button = Button(WIDTH // 2 - 120, HEIGHT - 70, 100, 50, "<", BLUE)
        next_button = Button(WIDTH // 2 + 20, HEIGHT - 70, 100, 50, ">", BLUE)
        back_button = Button(WIDTH // 2 - 100, HEIGHT - 150, 200, 50, "返回", BLUE)

        while running:
            screen.fill(BLACK)
            title = large_font.render("抽卡历史记录", True, WHITE)
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

            # 获取从当前页显示的历史记录
            start_index = self.history_page * self.history_per_page
            end_index = start_index + self.history_per_page
            recent_history = self.player.gacha_history[start_index:end_index]

            y = 100
            for i, result in enumerate(recent_history):
                text = font.render(f"{start_index + i + 1}. {str(result)}", True, result.color)
                screen.blit(text, (50, y))
                y += 30

            # 动态更新按钮状态
            prev_button.color = GREY if self.history_page == 0 else BLUE
            next_button.color = GREY if end_index >= len(self.player.gacha_history) else BLUE

            # 绘制按钮
            prev_button.draw(screen)
            next_button.draw(screen)
            back_button.draw(screen)

            pygame.display.flip()

            # 事件处理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # 翻页按钮点击
                if prev_button.handle_event(event) and self.history_page > 0:
                    self.history_page -= 1  # 上一页
                    break  # 重新绘制页面
                if next_button.handle_event(event) and end_index < len(self.player.gacha_history):
                    self.history_page += 1  # 下一页
                    break  # 重新绘制页面

                # 返回按钮点击
                if back_button.handle_event(event):
                    running = False  # 退出历史记录页面
                    break
    def run(self):
        if not self.get_user_input():
            return

        running = True
        clock = pygame.time.Clock()

        while running:
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # 单抽
                if self.single_pull_button.handle_event(event):
                    result = self.do_gacha()
                    if result:
                        self.draw_gacha_animation(result)

                # 十连抽
                if self.ten_pull_button.handle_event(event):
                    results = self.do_gacha(is_ten_pulls=True)
                    if results:
                        self.draw_gacha_animation(results)

                # 历史记录
                if self.history_button.handle_event(event):
                    self.draw_history()  # 进入历史记录界面后返回主界面继续运行

            self.single_pull_button.draw(screen)
            self.ten_pull_button.draw(screen)
            self.history_button.draw(screen)

            self.draw_resources()
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

    

if __name__ == "__main__":
    simulator = GachaSimulator()
    simulator.run()