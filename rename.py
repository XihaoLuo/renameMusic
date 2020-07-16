# Xihao Luo
# Script for renaming album music
# Renames all the songs into '(track number).(artist name) - (song name)' format

import os
import sys
from mutagen.flac import FLAC


def rename(directory, current_names, artist, album, year, names, fextension):
    # Loop through to rename each one
    new_names = []
    for i in range(len(names)):
        current_name = current_names[i]
        current_path = directory + os.sep + current_name
        current_path = r'{}'.format(current_path)

        # Assuming we have less than 100 tracks in total
        if i+1 <= 9:  # adds '0' in front of num for track nums 1-9
            new_name = '0' + '{}'.format(i+1) + '. ' + names[i] + fextension
        else:
            new_name = '{}'.format(i+1) + '. ' + names[i] + fextension
        new_path = directory + os.sep + new_name
        new_path = r'{}'.format(new_path)

        new_names.append(new_name)  # saves the new names for later

        if current_name != new_name:
            os.rename(current_path, new_path)

    # Now fill in the tags
    for i in range(len(new_names)):
        file = FLAC(directory + os.sep + new_names[i])  # navigate to file

        file['title'] = u'{}'.format(names[i])  # change title
        file['tracknumber'] = '{}'.format(i+1)
        file['artists'] = artist
        file['albumartist'] = artist
        file['album'] = album
        file['year'] = year

        file.save()
    return


def main():
    # Information
    directory = input('Please enter album directory: ')
    try:
        current_names = os.listdir(directory)
    except OSError:
        print('Directory does not exist.')
        sys.exit(1)
    artist = input('Enter artist name: ')
    album = input('Enter album name: ')
    year = input('Enter album release year: ')
    names = [item for item in input("Enter the new names (in order - split by ; ): ").split(';')]
    ftype = input('Enter file type (flac/mp3/wav/m4a): ')

    fextension = ''
    if ftype in ['flac', 'mp3', 'wav', 'm4a']:
        fextension = '.' + ftype
    else:
        print('File type not recognized :(')
        sys.exit(1)

    rename(directory, current_names, artist, album, year, names, fextension)


if __name__ == '__main__':
    main()
