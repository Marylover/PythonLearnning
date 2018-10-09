import os  #没想明白
for root, dirs, files in os.walk("/home/dong/练习", topdown=False):  #root:文件夹路径，dirs:文件夹名，files:文件名
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
