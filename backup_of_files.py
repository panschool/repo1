# Source and destination directories that should be copied - change these destinations to change what is copied.
src_folder = '/Users/pan/osskoletest/'
dst_folder = '/Users/pan/osskoledestination/'


import shutil
import os
from datetime import datetime

today = datetime.now()
date_format = today.strftime("-%d-%m-%Y %H:%M:%S")


# This is not used anymore, but has potential to create a list, "file_list" and add every element
# from your folder to the file_list.

# def get_directory_files_to_list(src_folder):
#     global date_format
#     file_list = []
#     with os.scandir(src_folder) as files:
#         for file in files:
#             file_list.append(file.path + date_format)
#     return file_list

# This function is not used either, but has potential to sort the list. This is more useless,
# since the os will sort it, itself

# def sort_list(src_folder):
#     sorted_list = get_directory_files_to_list(src_folder)
#     sorted_list.sort()
#     return sorted_list

# print(sort_list('/Users/pan/osskoletest'))


# This is the actual program, that runs through the list os.listdir(src_folder) and save the values as file_name.
# The source is then defined, followed by the destination, the files should be copied to, a date is added also.
# Then the if statement states that if it's a regular file, it returns true,
# and the file goes into the shutil.copy(source, destination) function,
# which actually takes the files from A to B. Lastly the programme prints the copied files, to the terminal.
for file_name in os.listdir(src_folder):
    source = src_folder + file_name
    destination = dst_folder + file_name + date_format
    # Check if the source is a file
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print("Copied", file_name + date_format)
    # Check if the source is a directory
    elif os.path.isdir(source):
        shutil.copytree(source, destination)
        print("Copied directory", file_name + date_format)


print("Files copied to /Users/pan/osskoledestination")


# Kopier hele træet fra en bestemt folder og ned:::VIRKER IKKE:::
# source_dir = r"/Users/pan/osskoletest/"
# destination_dir = r"/Users/pan/osskoledestination/"
# shutil.copytree(source_dir, destination_dir)