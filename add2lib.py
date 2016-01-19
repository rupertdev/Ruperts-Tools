import logging
import os
import sys


files_dir = sys.argv[1]
#lib_dir = sys.argv[2]

for root, dirs, files in os.walk(files_dir):
    for file in files:
        if file.endswith('.mobi'):
            split = file.strip().split('-')
            if len(split) is 2:
                author = split[1]
                name = split[0].replace('.mobi', '')
                print(name + " by " + author)
            else:
                logging.error("Formatting on " + file + " is incorrect.")
