DEST=$(HOME)/.earth-view-wallpaper

install:
	mkdir $(DEST)
	cp get_wallpaper.py $(DEST)
	cp wallpaper_urls.txt $(DEST)
	cp systemd-user/earth-view-wallpaper.{service,timer} $(HOME)/.config/systemd/user/
	systemctl --user enable --now earth-view-wallpaper.timer

remove:
	systemctl --user disable --now earth-view-wallpaper.timer
	rm -rf $(DEST)
	rm $(HOME)/.config/systemd/user/earth-view-wallpaper.{service,timer}
