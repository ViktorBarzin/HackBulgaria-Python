import random
import json
import inflection
import os
from prettytable import PrettyTable


class Song:
    TIME_SEPARATOR = ':'

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.__length = length

    def __str__(self):
        return '{0} - {1} from {2} - {3}'.format(self.artist, self.title, self.album, self.__length)

    def __eq__(self, other):
        return self.title == other.title and\
                self.artist == other.artist and\
                self.album == other.album and \
               self.__length == other.length

    def __hash__(self):
        return 17 * hash(self.title) * hash(self.artist) + hash(self.album) + hash(self.__length)

    def __calculate_len_in_seconds(self):
        split_time = self.__length.split(self.TIME_SEPARATOR)

        # Cast each element to int before making calculations
        split_time = [int(x) for x in split_time]

        if len(split_time) == 2:
            return split_time[0] * 60 + split_time[1]
        return split_time[0] * 3600 + split_time[1] * 60 + split_time[1]

    def length(self, seconds=False, minutes=False, hours=False):
        if not seconds and not minutes and not hours:
            return self.__length
        if seconds:
            return self.__calculate_len_in_seconds()
        if minutes:
            return self.__calculate_len_in_seconds() / 60
        if hours:
            return self.__calculate_len_in_seconds() / 3600

    def serialize(self):
        # print(self.__dict__)
        return self.__dict__

class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.__songs = []
        self.__length = 0
        self.__played_songs = []
        self.__current_index = 0

    def __update_length(self, value):
        self.__length += value

    @staticmethod
    def __pick_random_from_set(_set):
        rand_pick = random.randint(len(_set) - 1)
        return _set[rand_pick]

    def add_song(self, song):
        self.__songs.append(song)
        self.__update_length(1)

    def remove_song(self, song):
        self.__songs.remove(song)
        self.__update_length(-1)

    def add_songs(self, songs):
        self.__songs.extend(songs)
        self.__update_length(len(songs))

    def total_length(self):
        return self.__length

    def artists(self):
        # todo: test!
        artists = {set([x.artist for x in self.__songs]), 0}
        for song in self.__songs:
            artists[song] += 1
        return artists

    def next_song(self):
        if self.shuffle:
            if len(self.__played_songs) == len(self.__songs):
                if self.repeat:
                    self.__played_songs = []
                    return self.__pick_random_from_set(self.__songs)
                raise Exception('Played all songs!')
            return self.__pick_random_from_set([x for x in self.__songs if x not in self.__played_songs])

        if self.repeat:
            if self.__current_index + 1 == self.__length:
                return self.__songs[0]
            return self.__songs[self.__current_index + 1]
        return self.__songs[self.__current_index + 1] if self.__current_index + 1 < len(self.__songs) else None

    def pprint_playlist(self):
        table = PrettyTable(['Artist', 'Song', 'Length'])
        for song in self.__songs:
            table.add_row([song.artist, song.title, song.length()])
        print(table)

    def save(self, path=os.getcwd() + os.path.sep + 'playlist-data' + os.sep):
        # todo: use __dict__ instead of dict()
        with open(path + inflection.parameterize(self.name) + '.json', 'w') as w:
            json.dump(dict(name=self.name, shuffle=self.shuffle, repeated=self.repeat,
                           songs=[song.serialize() for song in self.__songs],
                           length=self.__length, played_songs=self.__played_songs,
                           current_index=self.__current_index), w, indent=4)
    @staticmethod
    def load(path):
        with open(path, 'r') as r:
            playlist = Playlist()
            j = json.load(r)
            # print(j)
            return Playlist(**j)

s = Song(title="Gosho", artist="Manowmmmar", album="The Sons of Odin", length="34:44")
s1 = Song(title="Odin", artist="pesho", album="The Sons of Odin", length="3:44")
s2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="1:3:44")
code_songs = Playlist(name="Python is the best", repeat=True, shuffle=True)
code_songs.add_songs([s, s1, s2])
# code_songs.pprint_playlist()
code_songs.save()
# code_songs = Playlist.load(os.getcwd() + '/playlist-data/python-is-the-best.json')

# print(code_songs.next_song())
