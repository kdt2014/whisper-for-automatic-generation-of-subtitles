import os
import shutil

# Define the source and target directories
source_dir = '/home/kdt/PycharmProjects/getsrt/Pytorch_audio'
target_dir = '/home/kdt/PycharmProjects/getsrt/Pytorch_audio_srt'

# Create the target directory if it does not exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Iterate through each subfolder in the source directory
for folder_name in os.listdir(source_dir):
    # Build the full path of the srt folder in the source directory
    srt_folder_path = os.path.join(source_dir, folder_name, folder_name + '_srt')

    # Check if this srt folder actually exists
    if os.path.isdir(srt_folder_path):
        # Build the full path of the srt folder in the target directory
        target_folder_path = os.path.join(target_dir, folder_name + '_srt')

        # Copy the entire folder to the target directory
        shutil.copytree(srt_folder_path, target_folder_path)
