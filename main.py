print('Welcome to Youtube Downloader and Converter v0.0.1')
print('Loading...')

import pytube
import video_downloader
import file_converter

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
        print('Starting Download...')
        video_downloader.download_playlist(playlist_link, quality)
        print('Finished Downloading!')
    if (choice == '1'):
        links = video_downloader.input_links()
        for link in links:
            video_downloader.download_video(link, quality)

elif choice == "3":
    links = video_downloader.input_links()
    for link in links:
        print("Downloading...")
        filename = video_downloader.download_video(link, 'low')
        print("Converting...")
        file_converter.convert_to_mp3(filename)

else:
    print('You\'ve Entered Invalid Input!')
    print('Terminating Script...')
