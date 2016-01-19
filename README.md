Tools
---
##mobi2epub

Script for crawling a given directory and converting all .mobi files to .epub files using Calibre's ebook-convert utility.

**Setup**
        1. Install calibre (sudo apt-get install calibre on ubuntu, download from website on mac)
    2. If you are on mac run the following command to add cli tools to your path.
       'export PATH=$PATH:/Applications/calibre.app/Contents/MacOS'
    3. pip install -r requirements_dev.txt


**Usage**

usage: mobi2epub.py [-h] [--dir [DIR]] [--overwrite] [--verbose]

optional arguments:

  -h, --help   show this help message and exit  

  --dir [DIR]  Dir to start the search for MOBI files

  --overwrite  Overwrite existing epub files? Defaults to false.

  --verbose    Run with full output from ebook-convert
