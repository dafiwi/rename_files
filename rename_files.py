#!/usr/bin/env python3

import os
import pathlib
import re

home_directory = os.environ.get('HOME', os.environ.get('USERPROFILE', ''))
directory_input = input("Please enter the directory path starting from HOME: ")
absolute_path = os.path.join(home_directory, directory_input)
directory_path = pathlib.Path(absolute_path)

# Adjust the schema to your needs here:
schema = 'your filename-2026-{index}'

pattern_string = schema.replace('{index}', r'(\d+)')
pattern = re.compile(f'^{pattern_string}$')

if directory_path.is_dir():

    # Check if files in directory_path were already renamed before and get max_index value
    max_index = 0
        
    for file_path in directory_path.iterdir():
        if file_path.is_file() and pattern.match(file_path.stem):
            match = pattern.match(file_path.stem) 
            if match:
                index = int(match.group(1))
                if index > max_index:
                    max_index = index
    
    next_index = max_index + 1
    
    # Rename files which do not match the pattern, starting with next_index 
    renamed_files_count = 0

    for file_path in directory_path.iterdir():
        if (file_path.is_file() and
            not pattern.match(file_path.stem)):
            
            suffix = file_path.suffix
            new_name = f"{schema.format(index=next_index)}{suffix}"
            new_path = file_path.with_name(new_name)
            
            if new_path.exists():
                print(f"Skip {file_path.name}: {new_name} does already exist.")
                continue
            
            file_path.rename(new_path)
            next_index += 1
            renamed_files_count += 1
    
    print(f"Renamed {renamed_files_count} files successfully. Next index: {next_index}")
else:
    print("Error: This directory does not exist.")