import pytube


def input_links():
    '''
    Takes URLs from the user.
    '''
    links = []

    print('Enter links OR "STOP" to exit.')
    while True:
        url = input()
        if url == "STOP" or url == 'stop':
            break
        else:
            links.append(url)

    return links


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


def download_video(link, quality):
    '''
    Downloads video from the youtube of the given quality.

    :param link: URL of the Youtube video
    :param quality: Quality/Resolution of the video
    :return: Name of the downloaded video
    '''
    video_object = pytube.YouTube(link)
    video_itag = choose_quality(quality)
    stream = video_object.streams.get_by_itag(video_itag)
    print('Starting Download...')
    stream.download()
    print('Download Finished!')

    return stream.default_filename


def download_videos(urls, quality):
    '''
    Downloads multiple videos from the youtube.

    :param urls: List of URLs of youtube videos
    :param quality: Quality/Resolution of the video
    '''
    for url in urls:
        download_video(url, quality)


def download_playlist(link, quality):
    '''
    Downloads the playlist from the youtube.

    :param link: URL of the youtube playlist.
    :param quality: Quality/Resolution of the video
    '''
    playlist_object = pytube.Playlist(link)
    download_videos(playlist_object.video_urls, quality)
