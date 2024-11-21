**在虚拟机上安装pycharm并配置环境**

**1.使用虚拟机自带的python2.7环境**

使用wget指令从pycharm官网下载pycharm压缩包

**[wget
<https://download.jetbrains.com/python/pycharm-community-2024.2.4.tar.gz>]{.mark}**

解压缩

**[tar -xzvf pycharm-community-2024.2.4.tar.gz]{.mark}**

打开终端，进入文件的bin目录，运行. pycharm.sh命令

![](media/image1.png){width="5.768055555555556in"
height="0.5909722222222222in"}

点击new新建项目，将图中所示解释器选为虚拟机的bin目录下自带的Python2.7

![](media/image2.png){width="5.768055555555556in"
height="4.052777777777778in"}

![](media/image3.png){width="5.768055555555556in"
height="4.266666666666667in"}

下载get-pip.py:

**[wget <https://bootstrap.pypa.io/get-pip.py>]{.mark}**

\*如果显示版本过低而报错可以尝试下载2.7版本的pip（因为 Python 2.7
不再得到官方支持，下载的链接可能已经失效）。

**[wget <https://bootstrap.pypa.io/pip/2.7/get-pip.py>]{.mark}**

说明：

因为 Python 2.7 已经在 2020 年停止支持，推荐你尽可能使用 Python
3.x。如果你能安装 Python 3.x，那么你可以使用更新版的 pip 来进行包管理。

**[sudo yum install python3]{.mark}** 安装 Python 3（如果尚未安装）

**[sudo yum install python3-pip]{.mark}** 安装 Python 3 的 pip

**[pip3 --version]{.mark}** 确认是否安装成功

如果无法通过yum下载软件包可能是由于网络连接问题或配置的镜像源不可用，以下给出几种解决方案：

1.  检查网络连接

首先检查虚拟机的网络连接是否正常。你可以尝试使用以下命令来检查网络连接：

**[ping.baidu.com]{.mark}**

如果无法连接，可能需要调整网络配置，确保虚拟机能够访问外部网络。

2.  更换镜像源

如果网络连接正常，但仍然无法访问 CentOS
的镜像源，你可以尝试更换镜像源。编辑 /etc/yum.repos.d/CentOS-Base.repo
文件，修改镜像源地址为其他可用的镜像。

例如：**[sudo vi /etc/yum.repos.d/CentOS-Base.repo]{.mark}**

将 mirrorlist=http://mirrorlist.centos.org/ 替换为
baseurl=http://vault.centos.org/centos/7.9.2009/os/x86_64/。

3\. 禁用镜像源

> 如果你暂时不需要安装更多软件包，可以选择禁用出现问题的仓库，然后继续安装软件：

**[sudo yum \--disablerepo=base -y install python3]{.mark}**

4\. 使用离线安装

> 如果你无法解决镜像源的问题，可以尝试在其他机器上下载 Python 3
> 的安装包，使用 U盘等方式将其传输到虚拟机上进行手动安装。

5\. 使用 dnf（如果可用）

> CentOS 8 及以上版本默认使用 dnf 替代 yum。如果你的系统是基于 CentOS 8
> 或更高版本，可以尝试：

**[sudo dnf install python3]{.mark}**

> 如果没有 dnf，则可以尝试按照上面的方法进行配置

运行脚本安装pip:

**[python get-pip.py]{.mark}** 对于 Python 2.x

**[python3 get-pip.py]{.mark}** 对于 Python 3.x

如果想创建快捷方式可以创建一个脚本文件

**[nano \~/桌面/pycharm.desktop]{.mark}**

进入文件并写入脚本

\[Desktop Entry\]

Version=1.0

Name=PyCharm

Comment=PyCharm IDE

Exec=/home/1204/桌面/pycharm-community-2024.2.4/bin/pycharm.sh

Icon=/home/1204/桌面/pycharm-community-2024.2.4/bin/pycharm.png

Terminal=false

Type=Application

Categories=Development;IDE;

\*注意Exec和Icon部分要写入自己的文件路径

\[Desktop Entry\]

Version=1.0

Name=PyCharm

Comment=PyCharm IDE

Exec=/home/1204/桌面/pycharm-community-2024.2.4/bin/pycharm.sh

Icon=/home/1204/桌面/pycharm-community-2024.2.4/bin/pycharm.png

Terminal=false

Type=Application

Categories=Development;IDE;

\*注意Exec和Icon部分要写入自己的文件路径

通过 chmod +x 给 pycharm.desktop 文件添加执行权限

**[chmod +x \~/桌面/pycharm.desktop]{.mark}**

pip下载速度可能太慢建议使用镜像源：

创建全局配置文件

**[nano \~/.pip/pip.conf]{.mark}**

在文件中写入镜像源脚本

**[\[global\]]{.mark}**

**[index-url = <https://pypi.tuna.tsinghua.edu.cn/simple>]{.mark}**

保存并退出

**2创建虚拟环境**

若想要创建虚拟环境需要确保虚拟机中安装了python3，python2.7已经停止支持，很多现代的python工具和库都只支持python3

1.首先确保虚拟机中安装了python3

**[sudo yum install python3]{.mark}**

2.安装virtualenv，可以通过pip3安装virtualenv

**[sudo yum install python3-pip]{.mark}**

> **[pip3 install virtualenv]{.mark}**（或者**[sudo pip3 install
> virtualenv]{.mark}**）

（pip需要加入到环境变量中:[**echo \'export
PATH=\$PATH:/root/.local/bin\' \>\> \~/.bashrc** **source
\~/.bashrc**]{.mark}）

3.  创建虚拟环境

**[virtualenv myenv]{.mark}**

4.  激活虚拟环境

**[source myenv/bin/activate]{.mark}**

python3已经自带了venv模块，它也可以用来创建虚拟环境，不需要额外安装任何安装包：
**[python3 -m venv myenv]{.mark}**

5，退出虚拟环境

**[deactivate]{.mark}**

**3.创建conda环境**

1.安装Miniconda（更轻量版的conda）

**[wget
<https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>]{.mark}**

\*也可以下载完整的anaconda发行版：

**[wget
<https://repo.anaconda.com/archive/Anaconda3-2023.09-Linux-x86_64.sh>]{.mark}**

2.运行安装脚本

**[bash Miniconda3-latest-Linux-x86_64.sh]{.mark}**

**[\*bash Anaconda3-2023.09-Linux-x86_64.sh]{.mark}**

3.初始化conda

**[source \~/miniconda3/bin/activate]{.mark}**

**[\*source \~/anaconda3/bin/activate]{.mark}**

4.创建虚拟环境

**[conda create \--name myenv python=3.6]{.mark}**

5.激活虚拟环境

**[conda activate myenv]{.mark}**

6.退出虚拟环境

**[conda deactivate]{.mark}**

如果想再次进入虚拟环境可以使用：**[source
\<环境路径\>/bin/activate]{.mark}**（例如：source
/home/1204/myenv/bin/activate）或者如果已经在正确的目录中可以直接激活虚拟环境：**[activate
myenv]{.mark}**）

再次进入conda环境：**[conda activate \<环境名\>]{.mark}** （例如：conda
activate mycondaenv）

**说明（可能遇见的问题）：**

"Cannot find a valid baseurl for repo: base/7/x86_64"
出现此类报错可能是centos无法访问默认的mirrorlist.centos.org，可能是网络连接问题或者DNS配置不正确导致无法获取软件包仓库的镜像列表

解决方案：

1.  检查网络连接：首先确认服务器能连接到互联网，可使用ping命令；来测试与外部服务器的链接，若不能链接检查网络设置（例如DNS配置，网关等）确保服务器有正确的网络访问权限，可以检查网络接口：**[ip
    addr show ens33]{.mark}** 尝试重启：

> **[sudo ifdown ens33]{.mark}**
>
> **[sudo ifup ens33]{.mark}**

2.  更换镜像源

备份现有的仓库配置文件**[sudo cp /etc/yum.repos.d/CentOS-Base.repo
/etc/yum.repos.d/CentOS-Base.repo.bak]{.mark}**

编辑/etc/yum.repos.d/CentOS-Base.repo 文件（**[sudo vi
/etc/yum.repos.d/CentOS-Base.repo]{.mark}**），找到
\[base\]、\[updates\] 和其他仓库部分，将其 mirrorlist 行替换为
baseurl，mirrorlist行注释掉，并指定一个可用的镜像源。例如，使用阿里云的
CentOS
镜像源：[[http://mirrors.aliyun.com/centos/7/os/x86_64/]{.mark}](http://mirrors.aliyun.com/centos/7/os/x86_64/)
文件配置如下：

\# CentOS-Base.repo

\# The mirror system uses the connecting IP address of the client and
the

\# update status of each mirror to pick mirrors that are updated to and

\# geographically close to the client. You should use this for CentOS
updates

\# unless you are manually picking other mirrors.

\# If the mirrorlist= does not work for you, as a fall back you can try
the

\# remarked out baseurl= line instead.

\[base\]

name=CentOS-\$releasever - Base - mirrors.aliyun.com

failovermethod=priority

baseurl=http://mirrors.aliyun.com/centos/\$releasever/os/\$basearch/

http://mirrors.aliyuncs.com/centos/\$releasever/os/\$basearch/

http://mirrors.cloud.aliyuncs.com/centos/\$releasever/os/\$basearch/

gpgcheck=1

gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7

#released updates

\[updates\]

name=CentOS-\$releasever - Updates - mirrors.aliyun.com

failovermethod=priority

baseurl=http://mirrors.aliyun.com/centos/\$releasever/updates/\$basearch/

> http://m[irrors.aliyuncs.com/centos/\$releasever/updates/\$basearch/
> http://](irrors.aliyuncs.com/centos/$releasever/updates/$basearch/%20http://)mirrors.cloud.aliyuncs.com/centos/\$releasever/updates/\$basearch/

gpgcheck=1

gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7

#additional packages that may be useful

\[extras\]

name=CentOS-\$releasever - Extras - mirrors.aliyun.com

failovermethod=priority

baseurl=http://mirrors.aliyun.com/centos/\$releasever/extras/\$basearch/

http://mirrors.aliyuncs.com/centos/\$releasever/extras/\$basearch/

http://mirrors.cloud.aliyuncs.com/centos/\$releasever/extras/\$basearch/

gpgcheck=1

gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7

#additional packages that extend functionality of existing packages

\[centosplus\]

name=CentOS-\$releasever - Plus - mirrors.aliyun.com

failovermethod=priority

baseurl=http://mirrors.aliyun.com/centos/\$releasever/centosplus/\$basearch/

http://mirrors.aliyuncs.com/centos/\$releasever/centosplus/\$basearch/

http://mirrors.cloud.aliyuncs.com/centos/\$releasever/centosplus/\$basearch/

\"/etc/yum.repos.d/CentOS-Base.repo\" 62L, 2523C

3.  修改DNS配置

打开/etc/resolv.conf 文件：**[sudo vi /etc/resolv.conf]{.mark}**

在文件中添加Google公共DNS服务器

**[nameserver 8.8.8.8]{.mark}**

**[nameserver 8.8.4.4]{.mark}**

保存并关闭文件然后再次尝试更新：**[sudo yum update]{.mark}**

可以测试DNS解析是否正常：**[nslookup mirror.centos.org]{.mark}** 或者

**[dig mirror.centos.org]{.mark}**

如果对DNS配置做了更改可以重启NetworkManager服务来应用新的配置：

**[sudo systemctl restart NetworkManager]{.mark}**

"http://mirror.centos.org/centos/7/extras/x86_64/repodata/repomd.xml:
\[Errno 14\] HTTP Error 404 - Not Found"
若出现这类报错可以临时禁用extras仓库：

**[sudo yum \--disablerepo=extras update]{.mark}**

sudo yum-config-manager \--disable extras（永久禁用，自行选择使用）

然后再次运行更新

4.  检查防火墙设置

如果有防火墙规则可能阻止外部连接如果防火墙是启用状态可以尝试暂时关闭它来排除问题

**[sudo firewall-cmd --state]{.mark}** 检查防火墙状态

**[sudo systemctl stop firewalld]{.mark}** 关闭防火墙

\*5.检查是否有代理设置

有时系统可能配置了代理，导致无法访问外部网络。检查环境变量是否存在代理配置：**[echo
\$http_proxy]{.mark}** **[echo \$https_proxy]{.mark}**

如果有代理设置，可能需要暂时禁用它，或者更新代理设置以允许访问 CentOS
镜像。

\*6.解决内存问题

**在 VMware 中增加磁盘**：关闭虚拟机、修改磁盘大小、启动虚拟机

1.确认磁盘空间是否已增加： 确保你已在 VMware
或虚拟机管理工具中增加了磁盘大小。你可以通过 **[lsblk]{.mark}** 或
**[fdisk -l]{.mark}** 查看新磁盘空间是否可用，查看磁盘和分区信息：

**[sudo lsblk]{.mark}**

**[sudo fdisk -l]{.mark}**

2\. 扩展物理卷（如果磁盘空间已增加）：
假设你已经增加了磁盘容量并确认空间已增加，那么你需要扩展物理卷（PV）：

**[sudo partprobe]{.mark}**

然后扩展物理卷：

**[sudo pvresize /dev/sda2]{.mark}** 这里的 /dev/sda2
是设备分区路径，通常你需要查看系统中的磁盘分区，并修改为实际的分区路径。例如，使用
**[lsblk]{.mark}** 或 **[fdisk -l]{.mark}** 命令查看你的磁盘分区，可能是
/dev/sdb1, /dev/nvme0n1p1 等。

3\. 扩展逻辑卷：扩展物理卷后，接下来需要扩展逻辑卷。

**[sudo lvextend -l +100%FREE /dev/centos/root]{.mark}**
/dev/centos/root 是逻辑卷的路径，通常是根据你的卷组（Volume
Group，VG）和逻辑卷（LV）名称来设定的。你可以使用 **[lvdisplay]{.mark}**
或 **[vgs]{.mark}** 命令查看你的卷组和逻辑卷，确保路径正确。（下同）

这样会将所有可用的空闲空间分配给根逻辑卷。

5.  扩展文件系统：最后，扩展文件系统以使用新扩展的空间，如果文件系统是XFS使用
    xfs_growfs 命令：**[sudo xfs_growfs /dev/centos/root]{.mark}**
    （如果使用的是ext4文件系统可以使用：**[sudo resize2fs
    /dev/centos/root]{.mark}**）可以使用**[df -h]{.mark}**验证空间变化

> 如果物理卷未自动扩展：

1.  扩展分区

删除现有分区（不丢失数据）：因为磁盘已经扩展，我们需要通过调整分区表来让
sda2
使用所有可用空间。执行以下步骤前，请确保你已经备份了重要数据（虽然操作过程中数据不应该丢失，但最好小心为妙）。运行
fdisk 来调整分区大小：**[sudo fdisk /dev/sda]{.mark}**

然后依次执行以下命令：

输入 p 查看当前分区表。

输入 d 删除分区 /dev/sda2。

输入 n 创建新的分区，类型选择 8e（Linux LVM），并确保将分区大小设置为
（自己设置的大小）。

输入 w 保存更改并退出。

2.  重新扫描分区

重新分区后，你需要让操作系统识别新的分区表。可以使用以下命令重新扫描磁盘：**[sudo
partprobe]{.mark}**

3.  扩展物理卷（PV）

分区调整后，扩展物理卷来使用新的空间：**[sudo pvresize
/dev/sda2]{.mark}**

这会扩展物理卷，允许它使用新的分区空间。

4.  扩展逻辑卷（LV）

**[sudo lvextend -l +100%FREE /dev/centos/root]{.mark}**

5.  扩展系统文件

最后，扩展 XFS 文件系统来使用新的空间：

**[sudo xfs_growfs /dev/centos/root]{.mark}**
