## Language Switching

[Switch to English](https://github.com/Mao-maocoder/VMware-install-manual/blob/main/manual_en.md) | [切换到中文](https://github.com/Mao-maocoder/VMware-install-manual/blob/main/manual.md)

# 在虚拟机上安装 PyCharm 并配置环境

## 1. 使用虚拟机自带的 Python 2.7 环境

### 下载并安装 PyCharm

1. 使用 `wget` 从 PyCharm 官网下载 PyCharm 压缩包：

   ```bash
   wget https://download.jetbrains.com/python/pycharm-community-2024.2.4.tar.gz
   ```

2. 解压缩：

   ```bash
   tar -xzvf pycharm-community-2024.2.4.tar.gz
   ```

3. 打开终端，进入文件的 `bin` 目录，运行 `pycharm.sh`：

   ```bash
   cd pycharm-community-2024.2.4/bin
   ./pycharm.sh
   ```

4. 在 PyCharm 中新建项目时，选择虚拟机的 Python 2.7 解释器。

### 安装 pip

1. 下载 `get-pip.py`：

   ```bash
   wget https://bootstrap.pypa.io/get-pip.py
   ```

2. 如果出现版本过低错误，可以尝试下载 2.7 版本的 pip：

   ```bash
   wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
   ```

3. 运行脚本安装 pip：
   ```bash
   python get-pip.py   # 对于 Python 2.x
   python3 get-pip.py  # 对于 Python 3.x
   ```

### 配置镜像源以加速 pip 下载

1. 创建全局配置文件 `~/.pip/pip.conf`：

   ```bash
   nano ~/.pip/pip.conf
   ```

2. 在文件中添加镜像源：
   ```ini
   [global]
   index-url = https://pypi.tuna.tsinghua.edu.cn/simple
   ```

## 2. 创建虚拟环境

### 安装 Python 3 和 virtualenv

1. 安装 Python 3：

   ```bash
   sudo yum install python3
   ```

2. 安装 `virtualenv`：
   ```bash
   sudo yum install python3-pip
   pip3 install virtualenv
   ```

### 创建虚拟环境

1. 使用 `virtualenv` 创建虚拟环境：

   ```bash
   virtualenv myenv
   ```

2. 激活虚拟环境：

   ```bash
   source myenv/bin/activate
   ```

3. 退出虚拟环境：
   ```bash
   deactivate
   ```

### 使用 Python 3 自带的 venv 模块

如果虚拟机已安装 Python 3，无需额外安装 `virtualenv`，可以使用 Python 自带的 `venv` 模块来创建虚拟环境：

1. 创建虚拟环境：

   ```bash
   python3 -m venv myenv
   ```

2. 激活虚拟环境：

   ```bash
   source myenv/bin/activate
   ```

3. 退出虚拟环境：
   ```bash
   deactivate
   ```

## 3. 使用 Conda 环境

### 安装 Miniconda

1. 下载并安装 Miniconda：

   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh
   ```

2. 初始化 Conda：
   ```bash
   source ~/miniconda3/bin/activate
   ```

### 创建 Conda 环境

1. 创建虚拟环境：

   ```bash
   conda create --name myenv python=3.6
   ```

2. 激活虚拟环境：

   ```bash
   conda activate myenv
   ```

3. 退出虚拟环境：
   ```bash
   conda deactivate
   ```

## 4. 常见问题与解决方案

### 1. PyCharm 启动速度慢

- 确保虚拟机有足够内存（建议至少 2GB）。
- 确保已安装最新版本的 PyCharm 和 JDK。

### 2. 虚拟机无法连接网络

- 检查虚拟机的网络模式是否设置为 NAT 或桥接模式，并确认主机能够访问外网。
- 重置网络服务：
  ```bash
  sudo systemctl restart network
  ```

### 3. pip 安装失败

- 配置镜像源：
  编辑 `~/.pip/pip.conf` 文件，添加以下内容：

  ```ini
  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  ```

- 重新安装 pip：
  ```bash
  python -m ensurepip --upgrade
  python -m pip install --upgrade pip
  ```

### 4. 磁盘空间不足

- 清理无用文件：

  ```bash
  sudo yum clean all
  sudo rm -rf /var/cache/yum
  ```

- 删除不需要的旧内核：
  ```bash
  sudo package-cleanup --oldkernels --count=1
  ```

### 5. 扩展磁盘空间（如果需要）

1. 确保在虚拟机管理工具中增加了磁盘空间。
2. 扩展物理卷：

   ```bash
   sudo pvresize /dev/sda2
   ```

3. 扩展逻辑卷：

   ```bash
   sudo lvextend -l +100%FREE /dev/centos/root
   ```

4. 扩展文件系统（假设使用 XFS 文件系统）：

   ```bash
   sudo xfs_growfs /dev/centos/root
   ```

5. 验证空间变化：
   ```bash
   df -h
   ```

## 5. 总结

通过上述步骤，你可以在虚拟机中成功安装并配置 PyCharm，创建虚拟环境（使用 `virtualenv` 或 `conda`），并解决一些常见的安装和配置问题。如果可能，尽量使用 Python 3.x 环境，以避免 Python 2.7 停止支持后出现的问题。

可以简单写一个代码测试环境是否搭建成功,创建好代码文件后如果不想以后再一次次的进入代码所在的目录可以编写一个脚本以便下次可以直接访问你的代码文件
 ```bash
 touch yourcode.sh # 创建脚本文件
 vim yourcode.sh # 编辑脚本文件
 ```
 脚本内容
 
 ```bash
 #!/bin/bash

# 激活 Conda 环境（如果使用了 Conda）
source /root/miniconda3/bin/activate base  # 根据你的 Conda 安装路径修改

# 切换到 Python 项目目录
cd /home/1204/PycharmProjects/pythonProject

# 运行 Python 脚本
python Snake.py
```

