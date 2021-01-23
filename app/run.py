import apis, ytenum, texts
import os, time
import glob
from pydub import AudioSegment

texts.get_header()

# ytenum.downtype.PLAYLIST or VIDEO
downtype = apis.ask_playlist_or_video()

# directory to save file(s). saved as string
directory = apis.ask_directory()

video_list = None
if downtype == ytenum.downtype.PLAYLIST:
    playlist = apis.ask_playlist_and_get_playlist()
    video_list = playlist.videos
else:
    video_list = ask_video_link_and_get_video_list()

# ytenum.filetype.VIDEO or AUDIO
filetype = apis.ask_type()

index = 0
for video in video_list:
	index += 1
	if index > 26:
		print("Downloading {index} | {video_title}...".format(
				index=index, video_title=video.title
			)
		)
		try:
			ys = None
			if downtype == ytenum.downtype.VIDEO:
				ys = video.streams.filter(only_video=True).order_by("resolution")
			else:
				ys = video.streams.filter(only_audio=True, file_extension='mp4').order_by('abr')
			
			try:
				ys.first().download(directory)
			except:
				print("failed download {video_title}".format(video_title=video.title))
		except:
			print("failed download")

			time.sleep(2)

print("Downloaded \n")
print("Complted Download {count} videos".format(count=index))

apis.ask_open_finder_and_do(directory)

texts.get_footer()
texts.exit_msg()

print("Press [Enter] to exit")
input()
sys.exit()
