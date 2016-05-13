#!/usr/bin/python
import logging
import os
import sys

from argparse import ArgumentParser
from subprocess import call

parser = ArgumentParser()

parser.add_argument("--dir", default=".", nargs="?",
                    help="Dir to start the search for eBook files, \
                    defaults to current directory")
parser.add_argument("--overwrite", default=False, action="store_true",
                    help="Overwrite existing epub files? Defaults to false.")
parser.add_argument("--verbose", default=False, action="store_true",
                    help="Run with full output from ebook-convert")
parser.add_argument("--input", default="epub", nargs="?",
                    help="File format to convert.")
parser.add_argument("--out", default='mobi', nargs="?",
                    help="File format to output.")
args = parser.parse_args()

def batch_convert(start_dir, overwrite, verbose, type_in, type_out):
    print "Looking for files.."
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(type_in):
                file_path = root + '/' + file
                out_path = file_path.replace(file.split('.')[1], type_out)
                if(overwrite or (not os.path.exists(out_path))):
                    try:
                        if verbose: ret = call(["ebook-convert",
                                                file_path, out_path])
                        else:
                            ret = call(["ebook-convert", file_path, out_path],
                                    stdout=open(os.devnull, 'wb'),
                                    stderr=open(os.devnull, 'wb'))
                    except ValueError as ve:
                        logging.error(ve)
                    except Exception as e:
                        logging.warning(e)
                    if ret != 0:
                        print("Conversion of " + file + " failed, "
                                "run with --verbose flag to find out why.")
                        continue
                    print(file + " converted successfully")
                else:
                    print(file + " skipped, " + type_out + "  already exists.")

batch_convert(args.dir, args.overwrite, args.verbose, args.input, args.out)
