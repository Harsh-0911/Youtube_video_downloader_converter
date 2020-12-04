import os
import pytube


def input_links():
    '''
    Takes URLs from the user either manually or from file.
    '''
    links = []

    print('-' * 30)
    print('[+] 1. Get links from .txt file')
    print('[+] 2. Input links manually')
    print('-' * 30)
    choice = input(': ')

    if (choice == '1'):
        file_path = input('Enter path of .txt file: ')
        with open(file_path, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.split('\n')[0]
            links.append(line)
        return links

    elif (choice == '2'):
        print('Enter links OR "STOP" to exit.')
        while True:
            url = input()
            if url.lower() == 'stop':
                break
            else:
                links.append(url)
        return links

    else:
        print('Invalid choice')
        print('Terminating...')


def choose_quality(resolution):
    '''
    Take the resolution and returns approprite itag.

    :param resolution: Resolution of video.
    :return: Relative itag according to specified resolution.
    '''
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in [
            "high", "1080", "1080p", "fullhd", "full_hd", "full hd"
    ]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def download_video(link, quality, destination_path):
    '''
    Downloads video from the youtube of the given quality.

    :param link: URL of the Youtube video
    :param quality: Quality/Resolution of the video
    :param destination_path: Path of where to store downloaded video.
    :return: Name of the downloaded video
    '''
    video_object = pytube.YouTube(link)
    video_itag = choose_quality(quality)
    stream = video_object.streams.get_by_itag(video_itag)
    if (stream is None):
        stream = video_object.streams.get_by_itag(18)
    print(f'[+] Downloading.. -  {video_object.title}')
    stream.download(destination_path)
    print(f'[+] Completed - {video_object.title}')

    return stream.default_filename


def download_videos(urls, quality, destination_path):
    '''
    Downloads multiple videos from the youtube.

    :param urls: List of URLs of youtube videos
    :param quality: Quality/Resolution of the video
    :param destination_path: Path of where to store downloaded videos.
    '''
    for url in urls:
        download_video(url, quality, destination_path)


def download_playlist(link, quality, destination_path):
    '''
    Downloads the playlist from the youtube.

    :param link: URL of the youtube playlist.
    :param quality: Quality/Resolution of the video
    :param destination_path: Path of where to store downloaded videos.
    '''
    playlist_object = pytube.Playlist(link)
    os.mkdir(os.path.join(destination_path, playlist_object.title))
    downloaded_video_location = os.path.join(
        destination_path, playlist_object.title)
    print(f'[+] Downloading playlist - {playlist_object.title}')
    download_videos(playlist_object.video_urls,
                    quality, downloaded_video_location)
    print(f'[+] Completed Downloading playlist - {playlist_object.title}')
