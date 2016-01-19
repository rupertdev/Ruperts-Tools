#!/usr/bin/python
import logging
import os
import sys

from argparse import ArgumentParser
from subprocess import call

parser = ArgumentParser()

parser.add_argument("--dir", default=".", nargs="?",
                    help="Dir to start the search for MOBI files, \
                    defaults to current directory")
parser.add_argument("--overwrite", default=False, action="store_true",
                    help="Overwrite existing epub files? Defaults to false.")
parser.add_argument("--verbose", default=False, action="store_true",
                    help="Run with full output from ebook-convert")
args = parser.parse_args()

def batch_convert(start_dir, overwrite, verbose):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.mobi'):
                epub_path = root + '/' + file.replace('.mobi', '.epub')
                file_path = root + '/' + file
                if(overwrite or (not os.path.exists(epub_path))):
                    try:
                        if verbose: ret = call(["ebook-convert",
                                                file_path, epub_path])
                        else:
                            ret = call(["ebook-convert", file_path, epub_path],
                                    stdout=open(os.devnull, 'wb'),
                                    stderr=open(os.devnull, 'wb'))
                    except Exception as e:
                        logging.warning(e)
                    if ret != 0:
                        print("Conversion of " + file + " failed")
                        continue
                    print(file + " converted successfully")
                else:
                    print(file + " skipped, epub already exists.")
batch_convert(args.dir, args.overwrite, args.verbose)
