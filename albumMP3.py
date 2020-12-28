import os
import sys
from mutagen.easyid3 import EasyID3


class AlbumMP3:

    def __init__(self, directory, artistName, albumName, yearReleased, songNames, fextension):
        self.directory = directory
        self.artistName = artistName
        self.albumName = albumName
        self.yearReleased = yearReleased
        self.songNames = songNames
        self.fextension = fextension

    def renameAlbumName(self):
        try:
            current_names = os.listdir(self.directory)
        except OSError:
            print('Directory does not exist.')
            sys.exit(1)

        for i in range(len(current_names)):
            file = EasyID3(self.directory + os.sep + current_names[i])  # navigate to file
            file['album'] = self.albumName
            file.save()

    def renameArtistName(self):
        try:
            current_names = os.listdir(self.directory)
        except OSError:
            print('Directory does not exist.')
            sys.exit(1)

        for i in range(len(current_names)):
            file = EasyID3(self.directory + os.sep + current_names[i])  # navigate to file
            file['artist'] = self.artistName
            file.save()

    def renameAllSongs(self):

        for i in range(len(self.songNames)):
            trackNum = i + 1
            newName = self.songNames[i]
            self.renameSong(newName, trackNum)

    # Rename a song based on a specific track number
    def renameSong(self, newName, trackNum):
        # Find song file in folder:
        try:
            current_names = os.listdir(self.directory)
        except OSError:
            print('Directory does not exist.')
            sys.exit(1)

        for name in current_names:
            file = EasyID3(self.directory + os.sep + name)
            if file['tracknumber'][0] == str(trackNum):  # song found
                print("file found")
                curFileName = name
                file['title'] = newName
                file.save()
                break

        if trackNum <= 9:  # adds '0' in front of num for track nums 1-9
            newFileName = '0' + str(trackNum) + '. ' + newName + self.fextension
        else:
            newFileName = str(trackNum) + '. ' + newName + self.fextension
        currentPath = self.directory + os.sep + curFileName
        newPath = self.directory + os.sep + newFileName
        os.rename(currentPath, newPath)
