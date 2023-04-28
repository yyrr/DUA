import glob
import random
import os
import shutil

# Get all paths to your images files and text files
PATH= '/opt/dua/data/kitti/initial/images/'
txt_paths = glob.glob(PATH+'*.png')

# Calculate number of files for training, validation
data_size = len(txt_paths)
train_size = int(data_size * 0.6)
test_size = int(data_size * 0.8)
print(data_size)
print(train_size)
print(test_size)

# Shuffle two list
img_txt = list(txt_paths)
random.seed(43)
random.shuffle(img_txt)

file2 = open(r"/opt/dua/data/kitti/train.txt", "w")
for f in img_txt[0:train_size]:
    file2.writelines(f[-10:])
    file2.write('\n')
file2.close()

file2 = open(r"/opt/dua/data/kitti/test.txt", "w")
for f in img_txt[train_size:test_size]:
    file2.writelines(f[-10:])
    file2.write('\n')
file2.close()

file2 = open(r"/opt/dua/data/kitti/val.txt", "w")
for f in img_txt[test_size:]:
    file2.writelines(f[-10:])
    file2.write('\n')
file2.close()




