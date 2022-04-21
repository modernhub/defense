import photo
import bot
import event
import cfg
import os

try:
    while True:
        coord = event.mouse_position()
        coord_x = coord[0]
        coord_y = coord[1]
        active_zone = cfg.coord

        if active_zone['x'][0] <= coord_x <= active_zone['x'][1] and \
            active_zone['y'][0] <= coord_y <= active_zone['y'][1]:
            
            while True:
                coord = event.mouse_position()
                coord_x = coord[0]
                coord_y = coord[1]
                if active_zone['x'][0] > coord_x or coord_x > active_zone['x'][1] and \
                            active_zone['y'][0] > coord_y or coord_y > active_zone['y'][1]:
                                if not event.keyboard_event():
                                    photo.take_photo()
                                    bot.start()
                                    os.popen('dbus-send --type=method_call --dest=org.gnome.ScreenSaver \
                                                /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock')
                                    exit(0)
                                break
except KeyboardInterrupt:
    print('\n It is working' )
