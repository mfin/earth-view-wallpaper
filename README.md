# earth-view-wallpaper
A script that downloads a wallpaper from Google's Earth View. Inspired by Muzei's Earth View addon on Android.

## About
This python script downloads a wallpaper from Google's Earth View service to `$HOME/Pictures/earth-view.jpg`. Just set this image as your wallpaper with your favorite tool. The only dependency is Python 3.

Feel free to submit pull requests, if you want to extend the functionality (after all, it's [Hacktoberfest](https://hacktoberfest.digitalocean.com/)!)

## Installation
`make install` creates a directory `$HOME/.earth-view-wallpaper`, copies systemd user service and timer to `$HOME/.config/systemd/user/` and enables the timer for user. Script executes 10 minutes after boot and once every hour onwards.

`make remove` disables systemd user timer and removes all the files.

## Screenshot
![Screenshot](screenshot.png)
