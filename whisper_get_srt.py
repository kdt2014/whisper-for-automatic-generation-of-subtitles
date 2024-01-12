import os
import subprocess
import whisper

# Print the version of the Whisper library
print(whisper.__version__)

# Define the root directory where the audio files are located
root_dir = '/home/kdt/PycharmProjects/getsrt/Pytorch_audio/'

# Iterate through each subfolder in the root directory
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    
    # Check if the current item is a directory
    if os.path.isdir(folder_path):
        # Create a path for storing subtitles
        subtitles_path = os.path.join(folder_path, folder + '_srt')
        # Create the directory for subtitles if it doesn't exist
        if not os.path.exists(subtitles_path):
            os.mkdir(subtitles_path)

        # Iterate through each audio file in the folder
        for audio_file in os.listdir(folder_path):
            audio_path = os.path.join(folder_path, audio_file)
            
            # Check if the file is an audio file with specific extensions
            if os.path.isfile(audio_path) and audio_file.endswith(('.mp3', '.wav', '.m4a', '.flac')):
                try:
                    # Construct the command to run Whisper for subtitle generation
                    subtitle_file_name = os.path.splitext(audio_file)[0] + '.srt'
                    subtitle_file_path = os.path.join(subtitles_path, subtitle_file_name)
                    command = f'/home/kdt/anaconda3/envs/whisper_env/bin/whisper "{audio_path}" --model large-v2 --language English --output_format srt --output_dir "{subtitles_path}"'
                    subprocess.run(command, shell=True)

                    # Print a message on successful subtitle generation
                    print(f'Generated SRT for {audio_file}')
                except Exception as e:
                    # Print an error message if there is a problem in processing
                    print(f"Error processing file {audio_file}: {e}")
