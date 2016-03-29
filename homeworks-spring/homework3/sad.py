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


sad = "/home/nina/PycharmProjects/classwork4/sad/"

if os.path.exists(sad) == False:
    os.mkdir("sad")

if command == "store":
    if os.path.isfile(path):
        shutil.copy(path, sad)
        print("Сделяль")
    if os.path.isdir(path):
        shutil.copytree(path, sad + path)
        print("Сделяль")

if command == "diff":
    subprocess.Popen(["diff", sad + path, path])
