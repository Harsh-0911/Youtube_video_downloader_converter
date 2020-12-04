import os
from moviepy.editor import VideoFileClip


def convert_to_mp3(destination_path, filename):
    '''
    Extracts audio from the video file.

	:param destination_path: Path of where to store the file.
    :param filename: name of the video file.
    '''
    clip = VideoFileClip(os.path.join(destination_path, filename))
    clip.audio.write_audiofile(os.path.join(destination_path, filename[:-4]+".mp3"))
    clip.close()
    print('[+] Converted')