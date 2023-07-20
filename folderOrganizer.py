#!/usr/bin/env python
# coding: utf-8

import os
import shutil


downloads_folder_path = f"{__file__}".replace("Desktop/folderOrganizer.py", "Downloads")


for file in os.listdir(downloads_folder_path):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    
    folder_to_organize_file = f"{downloads_folder_path}/{file_extension}"
    
    if not os.path.isdir(folder_to_organize_file):
        os.mkdir(folder_to_organize_file)
    
    shutil.move(f"{downloads_folder_path}/{file}", f"{folder_to_organize_file}/{file}")




