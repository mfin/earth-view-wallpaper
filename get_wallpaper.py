#!/usr/bin/env python3

import sys
import subprocess
import urllib.request
from random import randint


def run_command(command, shell):
    subprocess.run(command.split(), shell=shell)


with open('wallpaper_urls.txt') as f:
    wallpapers = f.readlines()
    wallpaper = sys.argv[1]
    urllib.request.urlretrieve(
        wallpapers[randint(0, len(wallpapers) - 1)],
        wallpaper)

    # If you're using feh to set your wallpaper, uncomment the line below
    # run_command('feh --bg-fill {}'.format(wallpaper), False)
