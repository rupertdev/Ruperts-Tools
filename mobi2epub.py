#!/usr/bin/python
import os
import sys

from argparse import ArgumentParser
from subprocess import call

parser = ArgumentParser()

parser.add_argument("start", default=".", nargs="?",
                    help="Dir to start the search for MOBI files")
args = parser.parse_args()

def batch_convert(start_dir):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.mobi'):
                epub_path = root + '/' + file.replace('.mobi', '.epub')
                file_path = root + '/' + file
                ret = call(["ebook-convert", file_path, epub_path],
                            stdout=open(os.devnull, 'wb'))
                if ret != 0:
                    print("Conversion of " + file + " failed, stopping....")
                    exit()

                print(file + " converted successfully")

batch_convert(args.start)
