from moviepy.editor import VideoFileClip

def convert_to_mp3(filename):
    '''
    Extracts audio from the video file.

    :param filename: name of the video file.
    '''
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()