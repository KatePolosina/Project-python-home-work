import os
import stat
import time
import shutil
import sys

new_dir = '/Users/het/Desktop/МФТИ/pythonProject1'

#print(os.getcwd())
#print(os.listdir())
#print(os.listdir('new_folder'))
"""
os.chdir('/Users/het/Desktop/МФТИ/git-fpmi/FirstProject')
print(os.getcwd())
print(os.listdir())

print(os.path.join('FirstProject', 'new_directory'))

print(os.path.isfile('main.py'))

stat_info = os.stat('main.py')
print(stat_info)
print(stat.S_IMODE(stat_info.st_mode))

print(time.ctime(stat_info.st_ctime))
print(os.urandom(4).hex())
#print(os.system('ls'))
#print(os.umask(0o022))
#print(os.path.expanduser('~'))
print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
os.chdir('new_directory')
print(os.system('ls -a'))

print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('new_directory')
print(os.getcwd())
"""

folder = 'new_directory'
if os.getcwd().endswith(folder):
    print(f'Вы находитесь в папке {folder}')
    os.chdir('..')
    print(f'Вы вышли из папки {folder}')
if os.path.exists(folder):
    shutil.rmtree('new_directory')
    print(f'Папка {folder} удалена')
else:
    print(f'Папка {folder} не существует')
print(os.getcwd())

for item in sorted(os.listdir(), key=str.lower):
    print(item)
