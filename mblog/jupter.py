# _*_ coding: utf-8 _*_

import os, shutil, glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR:",BASE_DIR)
source_dir = os.path.join(BASE_DIR, "images")
print("source_dir:",source_dir)
disk = os.statvfs("/")
print("disk",disk)
freespace = disk.f_bsize * disk.f_blocks
print("freespace",freespace)
pngfiles = glob.glob(source_dir + "/" + "*.png")
print("pngfiles:",pngfiles)
jpgfiles = glob.glob(source_dir + "/" + "*.jpg")
print("jpgfiles",jpgfiles)
giffiles = glob.glob(source_dir + "/" + "*.gif")
print("giffiles",giffiles)
allfiles = pngfiles + jpgfiles + giffiles
print("allfiles",allfiles)
print(type(allfiles))
allfilesize = 0
for f in allfiles:
    allfilesize += os.path.getsize(f)

print("allfilesize", allfilesize)

if allfilesize > freespace:
    print("硬盘空间不足")
    exit(1)

target_dir = source_dir + '/' + "output"
print(target_dir)
if os.path.exists(target_dir):
    target_dir = source_dir + '/' + "output1"
    if os.path.exists(target_dir):
        os.removedirs(target_dir)
    print("目标文件夹已存在，更改为output1")

os.mkdir(target_dir)
print(target_dir)
imageno = 0

for f in allfiles:
    print("f",f)
    dirname, filename = f.split('images/')
    print(dirname,filename)
    mainname, extname = filename.split('.')
    print(mainname,extname)
    targetfile = target_dir + str(imageno) + '.' + extname
    shutil.copyfile(f, targetfile)
    imageno += 1
