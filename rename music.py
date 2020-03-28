import os
import filetype
import magic
from eyed3 import id3
import re

directory = 'Telegram Documents'

files = os.listdir(directory)
del files[0]
i = 1

for file in files:
    type = magic.from_file(directory + "\\" + file, mime=True)
    i += 1
    if type not in 'audio/mpeg':
        print('Cannot guess file type!')
    else:
        tag = id3.Tag()
        try:
            tag.parse(directory + "\\" + file)
        except:
            print('cannot open file')
        else:
            album = str(tag.album)
            album_artist = str(tag.album_artist)
            artist = str(tag.artist)
            title = str(tag.title)
            num = str((tag.track_num)[0])
            name = ''
            count = 0
            if num not in 'None':
                name = num + ' - '
            if artist not in 'None':
                name += artist + ' '
                count += 1
            if title not in 'None':
                name += title + ' '
                count += 1
            if album_artist not in 'None' and count < 2:
                name += album_artist + ' '
                count += 1
            if album not in 'None' and count < 2:
                name += album + ' '
                count += 1

            if count > 0:
                try:
                    os.rename(directory + "\\" + file, directory + "\\" + name + '.mp3')
                except:
                    print('cannot rename ' + file)
