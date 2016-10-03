#!/usr/bin/env python3

import argparse
import subprocess
import urllib.request
from random import randint


def run_command(command, shell):
    subprocess.run(command.split(), shell=shell)


def main():
    parser = argparse.ArgumentParser(description='Fetch a wallpaper from Google\'s Earth View')
    parser.add_argument('output', help='where to put fetched wallpaper')
    parser.add_argument('--source-file',
        default='wallpaper_urls.txt', help='path to file with wallpaper links')
    args = parser.parse_args()

    with open(args.source_file) as f:
        wallpapers = f.readlines()
        wallpaper = args.output
        urllib.request.urlretrieve(
            wallpapers[randint(0, len(wallpapers) - 1)],
            wallpaper)

        # If you're using feh to set your wallpaper, uncomment the line below
        # run_command('feh --bg-fill {}'.format(wallpaper), False)


if __name__ == '__main__':
    main()
