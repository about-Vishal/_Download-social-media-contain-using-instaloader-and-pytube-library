import instaloader
from pytube import YouTube
import os

# Function to download the profile picture from Instagram
def profilepiloader():
    Instadownloader = instaloader.Instaloader()

    acc = input("Enter InstaId (Eg: vishal9199):")
    
    # Downloads the profile picture
    Instadownloader.download_profile(acc, profile_pic_only=True)

2
# Function to download Instagram Reels using the Instagram ID
def download_instagram_reels(username, download_path):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist.")
        return

    for post in profile.get_posts():
        if post.typename == 'GraphVideo' and post.is_video:
            try:
                # Downloads the Instagram Reel video
                loader.download_post(post, target=download_path)
                print(f"Reel downloaded: {post.url}")
                break
            except Exception as e:
                print(f"Failed to download reel: {post.url}")
                print(f"Error: {e}")
                break


# Function to download audio from a YouTube video
def audioloader():
    youtube_video_url = input("Enter Your Url/link :")

    yt = YouTube(youtube_video_url)
    video_stream = yt.streams.filter(only_audio=True).first()
    video_stream.download(filename='temp_video')

    video_clip = VideoFileClip('temp_video.mp4')
    audio_clip = video_clip.audio
    
    # Writes the extracted audio as an MP3 file
    audio_clip.write_audiofile('extracted_audio.mp3')

    video_clip.close()
    audio_clip.close()
    os.remove('temp_video.mp4')

    print('Audio extraction complete.')


# Function to download video from a YouTube URL
def videoLoaderYt():
    link = input("Enter Your Url/link :")
    yt = YouTube(link)
    
    # Filters and selects the best progressive MP4 stream
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
    video_stream.download()


# Main loop for the user interface
while True:
    print("--")
    print('[1.] Download profilePic from Instagram.')
    print("[2.] Download Reels Using insta Id.")
    print("[3.] Download Audio from YouTube.")
    print("[4.]Download Video From YouTube.")
    print("--")
    print("what you want to do plz enter Your choice (1 to 4 ):")
    ch = int(input())

    if ch == 1:
        profilepiloader()
    elif ch == 2:
        id = input(r"Enter Insta Id :")
        download_instagram_reels(id, r'C:\Users\Hirdaya sah potam sa\Desktop\reels')
    elif ch == 3:
        audioloader()
    elif ch == 4:
        videoLoaderYt()
    else:
        print("Invalid Choice")

    print("--")
    print('Do you want to run continou? (Y/n):')
    print("--")
    y = input()

    if y.lower() != 'y':
        print("***********Thank You************")
        break
