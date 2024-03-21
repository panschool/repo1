import sys

import shutil
import os
from datetime import datetime

today = datetime.now()
date_format = today.strftime("-%d-%m-%Y %H:%M:%S")

# Source og destination directories der skal kopieres
src_folder = '/Users/pan/osskoletest/'
dst_folder = '/Users/pan/osskoledestination/'





def get_directory_files_to_list(src_folder):
    global date_format
    file_list = []
    with os.scandir(src_folder) as files:
        for file in files:
            file_list.append(file.path + date_format)
    return file_list

def sort_list(src_folder):
    sorted_list = get_directory_files_to_list(src_folder)
    sorted_list.sort()
    return sorted_list

#print(sort_list('/Users/pan/osskoletest'))




for file_name in os.listdir(src_folder):
    source = src_folder + file_name
    destination = dst_folder + file_name + date_format
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print("Copied", file_name)


print("Files copied to /Users/pan/osskoledestination")


#Kopier hele træet fra en bestemt folder og ned:::VIRKER IKKE:::
# source_dir = r"/Users/pan/osskoletest/"
# destination_dir = r"/Users/pan/osskoledestination/"
# shutil.copytree(source_dir, destination_dir)
