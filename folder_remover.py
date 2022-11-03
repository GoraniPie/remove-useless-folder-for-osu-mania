from operator import truediv
import shutil
import os
import sys
import send2trash

cur_folder_size = 0

osz_size = 0
else_size = 0
osz_size_total = 0
else_size_total = 0

no_map_cnt = 0
osz_cnt = 0

has_map = False
has_osz = False

songs = os.listdir()

no_map_list = []
osz_list = []

for folder in songs:
    if os.path.isdir(folder):
        
        else_size = 0
        has_map = False
        has_osz = False
        
        for file in os.listdir(folder):
            if os.path.splitext(file)[1] == ".osu":
                has_map = True
                else_size += os.path.getsize(os.getcwd() + '/' + folder + '/' + file)
            elif os.path.splitext(file)[1] == ".osz":
                has_osz = True
                osz_cnt += 1
                osz_size += os.path.getsize(os.getcwd() + '/' + folder + '/' + file)
            else:
                else_size += os.path.getsize(os.getcwd() + '/' + folder + '/' + file)
            
        if not has_map:
            else_size_total += else_size
            print("NO MAP : " + folder)
            no_map_list.append(folder)
            no_map_cnt += 1
            
        if has_osz:
            osz_size_total += osz_size
            osz_list.append(folder)
            
print("folders with no map : " + str(no_map_cnt) + ", " + str(round(else_size_total / (1024 * 1024), 2)) + " MB")
print("unzipped osz files : " + str(osz_cnt) + ", " + str(round(osz_size_total / (1024 * 1024), 2)) + " MB")
print("=============================================")
print("Are you sure to remove folders with no map? type YES to continue")
choice = input()

if choice == "YES":
    print("=============================================")
    print("type YES to remove every folder with no map,\nor type any else to remove every folder except folder that has osz")
    choice = input()
    
    if choice == "YES":
        print("=============================================")
        for folder in no_map_list:
            send2trash.send2trash(folder)
            print("MOVED TO RECYCLE BIN : " + folder)
    else:
        for folder in no_map_list:
            if folder not in osz_list:
                send2trash.send2trash(folder)
                print("MOVED TO RECYCLE BIN : " + folder)
            else:
                print("IGNORED(has osz) : " + folder)
else:
    print("ABORTED")
    
os.system('pause')