import os

PATH = '/home/mehran/Desktop'
fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in :', root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

print('Number of files:', fileCount)
print('Number of directories:', dirCount)
