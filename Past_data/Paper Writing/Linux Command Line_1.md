## Linux Command Line1

---

### 查看磁盘空间大小命令

```bash
Df命令是linux系统以磁盘分区为单位查看文件系统
可以加上参数查看磁盘剩余空间信息，命令格式：
df -hl

#########

### 下面是相关命令的解释：
查看磁盘剩余空间
df -hl
查看每个根路径的分区大小
df -h
[目录名] 返回该目录的大小
du -sh
[文件夹] 返回该文件夹总M数
du -sm

### 更多功能可以输入一下命令查看：
df --help
du --help

#########

查看硬盘的分区 
sudo fdisk -l
查看硬盘剩余空间 
df -h
查看目录占用空间 
du -hs 目录名
```

