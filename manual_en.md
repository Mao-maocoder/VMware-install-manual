## Language Switching

[Switch to English](https://github.com/Mao-maocoder/VMware-install-manual/blob/main/manual_en.md) | [切换到中文](https://github.com/Mao-maocoder/VMware-install-manual/blob/main/manual.md)

# Installing PyCharm and Configuring the Environment on a Virtual Machine

## 1. Using the Virtual Machine's Built-in Python 2.7 Environment

### Downloading and Installing PyCharm

1. Use `wget` to download the PyCharm archive from the official PyCharm website:

   ```bash
   wget https://download.jetbrains.com/python/pycharm-community-2024.2.4.tar.gz
   ```

2. Extract the archive:

   ```bash
   tar -xzvf pycharm-community-2024.2.4.tar.gz
   ```

3. Open a terminal, navigate to the `bin` directory, and run `pycharm.sh`:

   ```bash
   cd pycharm-community-2024.2.4/bin
   ./pycharm.sh
   ```

4. When creating a new project in PyCharm, select the virtual machine's Python 2.7 interpreter.

### Installing pip

1. Download `get-pip.py`:

   ```bash
   wget https://bootstrap.pypa.io/get-pip.py
   ```

2. If you encounter an error due to an old version of pip, try downloading the Python 2.7 version of pip:

   ```bash
   wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
   ```

3. Run the script to install pip:

   ```bash
   python get-pip.py   # For Python 2.x
   python3 get-pip.py  # For Python 3.x
   ```

### Configuring the Mirror to Speed Up pip Downloads

1. Create the global configuration file ~/.pip/pip.conf:

   ```bash
   nano ~/.pip/pip.conf
   ```

2. Add the mirror source to the file:
   ```ini
   [global]
   index-url = https://pypi.tuna.tsinghua.edu.cn/simple
   ```

## 2. Creating a Virtual Environment

### Installing Python 3 and virtualenv

1. Install Python 3:

   ```bash
   sudo yum install python3
   ```

2. Install `virtualenv`:

   ```bash
   sudo yum install python3-pip
   pip3 install virtualenv
   ```

## Creating the Virtual Environment

1. Create the virtual environment using `virtualenv`:

   ```bash
   virtualenv myenv
   ```

2. Activate the virtual environment:

   ```bash
   source myenv/bin/activate
   ```

3. Deactivate the virtual environment:

   ```bash
   deactivate
   ```

### Using Python 3's Built-in venv Module

If Python 3 is already installed on the virtual machine, you can use Python's built-in `venv` module to create a virtual environment without needing `virtualenv`:

1. Create the virtual environment:

   ```bash
   python3 -m venv myenv
   ```

2. Activate the virtual environment:

   ```bash
   source myenv/bin/activate
   ```

3. Deactivate the virtual environment:

   ```bash
   deactivate
   ```

## Using a Conda Environment

### Installing Miniconda

1. Download and install Miniconda:

   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh
   ```

2. Initialize Conda:

   ```bash
   source ~/miniconda3/bin/activate
   ```

### Creating a Conda Environment

1. Create a virtual environment:

   ```bash
   conda create --name myenv python=3.6
   ```

2. Activate the virtual environment:

   ```bash
   conda activate myenv
   ```

3.Deactivate the virtual environment:

    ```bash
    conda deactivate
    ```

## Once the environment setup is complete, you can start writing Python code on the virtual machine.

- If using the built-in Python 2.7 version, you can run the code directly in the terminal:

```bash
python /path/yourprogram
```

- If using a custom virtual environment, you need to activate the environment before running the program:

```bash
source myenv/bin/activate
python /path/yourprogram
```

## 4. Common Issues and Solutions

### 1. PyCharm Startup is Slow

- Ensure that the virtual machine has enough memory (at least 2GB is recommended).
- Make sure the latest versions of PyCharm and JDK are installed.

### 2. The Virtual Machine Cannot Connect to the Network

- Check if the virtual machine's network mode is set to NAT or Bridged mode and ensure that the host machine can access the internet.

- Restart the network service:

```bash
sudo systemctl restart network
```

### 3. pip Installation Fails

- Configure the mirror source:
  Edit the `~/.pip/pip.conf` file and add the following content:

  ```ini
  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  ```

- Reinstall pip:
  ```bash
    python -m ensurepip --upgrade
    python -m pip install --upgrade pip
  ```

### 4. Insufficient Disk Space

- Clean up unnecessary files:

  ```bash
  sudo yum clean all
  sudo rm -rf /var/cache/yum
  ```

- Delete old unused kernels:

  ```bash
  sudo package-cleanup --oldkernels --count=1
  ```

### 5. Extending Disk Space (if necessary)

1. Ensure that disk space is increased in the virtual machine manager.

2. Resize the physical volume:

   ```bash
   sudo pvresize /dev/sda2
   ```

3. Resize the logical volume:

   ```bash
   sudo lvextend -l +100%FREE /dev/centos/root
   ```

4. Extend the file system (assuming you're using XFS):

   ```bash
   sudo xfs_growfs /dev/centos/root
   ```

5. Verify the space change:
   ```bash
   df -h
   ```

## 5. Conclusion

By following the steps above, you can successfully install and configure PyCharm on your virtual machine, create a virtual environment (using `virtualenv` or `conda`), and solve common installation and configuration issues. If possible, it is recommended to use Python 3.x to avoid issues after Python 2.7 is no longer supported.
