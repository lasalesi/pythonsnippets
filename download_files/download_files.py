import urllib.request
import urllib.parse

#
# This is a simple script to download files from internet sites
#
# Developed for Python 3
#
# Copyright (C) lasalesi, 2018
#
# Usage:
# Place a file "files.txt" in the same folder which contains the file URLs
#

# Read input file
file = open("files.txt","r")
urls = file.read().split("\n")

# Download each file
for url in urls:
    # get the file from the url
    response = urllib.request.urlopen(url)
    data = response.read()
    # use the last part of the url as filename
    filename = url.split("/")[-1]
    # and save to disk
    open(filename, 'wb').write(data)
    # and log to screen
    print("Downloaded " + filename)

# close file
file.close