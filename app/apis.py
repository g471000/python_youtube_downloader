import texts, ytenum
import sys
from subprocess import call
from tkinter.filedialog import askdirectory
from pytube import YouTube, Playlist

# Ask directory that the user wants to save
# return the directory path that the user chosen
def ask_directory():
    while True:
        directory = askdirectory(title="Choose directory", initialdir="/Users")
        correct = input(
            "You will download file to [{directory}].\nIs that right? [y/n] ".format(
                directory=directory
            )
        )
        if correct == "y":
            return directory


def ask_playlist_or_video():
    while True:
        answer = input(
            "Are you downloading Playlist or Video(s)? Type (p)laylist or (v)ideo: "
        )
        if answer == "v" or answer == "video":
            return ytenum.downtype.VIDEO
        elif answer == "p" or answer == "playlist":
            return ytenum.downtype.PLAYLIST
        else:
            print("Invalid type. Please type again")


# Ask YouTube video link that the user wants to download
# Return YouTube objects' list 
def ask_video_link_and_get_video_list():
    video_list = []
    link = input("Please type YouTube video link: ")
    while True:
        try:
            yt = YouTube(link)
            youtube_list.append(yt)
            link = input("Insert another link if you have any. Otherwise, press [n]: ")

        except:
            print(
                "Invalid URL. Please type correct URL (e.g. https://youtu.be/hhXDFl6tmVYi)"
            )
            link = input("Please type YouTube Video link: ")

        if link == "n":
            return youtube_list

# Ask YouTube playlist link that the user wants to download
# Return YouTube Playlist Object
def ask_playlist_and_get_playlist():
	link = input("Please type YouTube Playlist link: ")
	while True:
		try:
			return Playlist(link)
		except:
			print("Invalid URL. Please type valid Playlsit URL (e.g. https://youtu.be/rCeM57e2BfU)")
			link = input("Please type YouTube Playlist link: ")   

# ask type that the user wants to download.
# user can download either video or audio
def ask_type():
    while True:
        type = input(
            "Which Type do you want to download? (Type '(a)udio' or '(v)ideo': "
        )
        if type == "a" or type == "audio":
            return ytenum.filetype.AUDIO 
        elif type == "v" or type == "video":
            return ytenum.filetype.VIDEO 
        else:
            print("Invalid Type! Please type again.")

# ask if user wants to open the finder with the
# downloaded location
def ask_open_finder_and_do(directory):
	while True:
		answer = input(
			"Do you want to open the Finder(Downloaded location)? [y/n]")
		if answer == 'y':
			call(["open", directory])
			return
		elif answer == 'n':
			return
		else:
			print("Invalid input. Please type y or n")
