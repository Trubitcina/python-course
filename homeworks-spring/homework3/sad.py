#!/usr/bin/python3.4

import argparse
import os.path
import shutil
import subprocess


parser = argparse.ArgumentParser(description="It's take 2 args: command, path"
                                 "Use two commands: store, diff")

parser.add_argument("command",
                    type=str,
                    choices=["store", "diff"],
                    help="store:save curr.file or folder status passed by2arg."
                    "diff:run diff util. for passed file and its last status")

parser.add_argument("path",
                    type=str,
                    help="Gimme the path to your file or folder!"
                    "I can't work with folders yet")

args = parser.parse_args()
command = args.command
path = args.path


sad_home = "/home/nina/sad"
new_sad = '/home/nina/sad/' + path

if os.path.exists(sad_home) == False:
    os.mkdir("sad")

if command == "store":
    if os.path.isfile(path):
        shutil.copy(path, sad_home)
    if os.path.isdir(path):
        shutil.copytree(path, sad_home)

if command == "diff":
    subprocess.Popen(["diff", new_sad, sad_home])
