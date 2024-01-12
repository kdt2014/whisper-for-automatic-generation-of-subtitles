import os
import shutil
from moviepy.editor import VideoFileClip

# Define the root directory where the video files are located
root_dir = r'D:\003download\Pytorch'

# Create a directory for the output audio files
output_dir = os.path.join(root_dir, 'Pytorch_audio')
os.makedirs(output_dir, exist_ok=True)  # The directory is created if it does not exist

# Iterate through each folder in the root directory
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    
    # Check if the current item is a directory
    if os.path.isdir(folder_path):
        # Create a directory for audio files inside each folder
        audio_dir = os.path.join(folder_path, f'{folder}_audio')
        os.makedirs(audio_dir, exist_ok=True)

        # Iterate through each file in the folder
        for video in os.listdir(folder_path):
            # Process only files with .mp4 extension
            if video.endswith('.mp4'):
                video_path = os.path.join(folder_path, video)
                audio_path = os.path.join(audio_dir, os.path.splitext(video)[0] + '.mp3')

                # Extract audio from the video file
                video = VideoFileClip(video_path)
                audio = video.audio
                audio.write_audiofile(audio_path)  # Save the audio file as mp3

        # Copy the entire directory of audio files to the output directory
        shutil.copytree(audio_dir, os.path.join(output_dir, f'{folder}_audio'))
