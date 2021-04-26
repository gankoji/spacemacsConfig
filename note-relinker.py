#!/usr/local/bin/python3
import sys
import os
import re

if len(sys.argv) < 4:
    print("Error: not enough arguments.")
    exit()

currentFile = sys.argv[1]
newFile = sys.argv[2]
vaultPath = sys.argv[3]

# Using a compiled regex expression to do text replacement
def replace(filePath, text, subs, flags=0):
    with open(filePath, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

## Directory walk for whole vault
for root, subdirs, files in os.walk(vaultPath):
    noteFiles = [f for f in files if f.endswith(".md")]

    regex = os.path.relpath(currentFile, root)
    regex = os.path.splitext(regex)[0]
    subs = os.path.relpath(newFile, root)
    subs = os.path.splitext(subs)[0]

    for note in noteFiles:
        if not (note.startswith(".#")):
            replace(os.path.join(root,note), regex, subs)
