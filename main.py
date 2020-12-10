print('Welcome to Youtube Downloader and Converter v0.0.1')
print('Loading...')

import os
import pytube
import file_converter
import video_downloader


print('''
    [+] 1. Download Videos Manually .
    [+] 2. Download a Playlist.
    [+] 3. Download Video and convert it into mp3.

    ''')

choice = input('Enter Your Choice: ')

if (choice == '1' or choice == '2'):
    quality = input('Choose Quality (low, medium, high, very high): ')
    if (choice == '2'):
        playlist_link = input('Enter URL of Playlist: ')
        destination_path = input('Enter destination path: ')
        video_downloader.download_playlist(
            playlist_link, quality, destination_path)
    if (choice == '1'):
        links = video_downloader.input_links()
        destination_path = input('Enter destination path: ')
        for link in links:
            video_downloader.download_video(link, quality, destination_path)

elif choice == "3":
    links = video_downloader.input_links()
    destination_path = input('Enter destination path: ')
    for link in links:
        filename, flag = video_downloader.download_video(
            link, 'low', destination_path)
        if not flag:
            print("[+] Converting to mp3")
            file_converter.convert_to_mp3(destination_path, filename)
            os.remove(os.path.join(destination_path, filename))
            
else:
    print('You\'ve Entered Invalid Input!')
    print('Terminating Script...')
