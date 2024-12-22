import yt_dlp
import tkinter as tk
from tkinter import filedialog
import subprocess
import os

# Set the path to the FFmpeg executable

ffmpeg_path = "D:\\ffmpeg-2024-12-19-git-494c961379-full_build\\bin\\ffmpeg.exe"

# Function to run FFmpeg commands with suppressed output (only for merging if necessary)

def process_video(input_file, output_file):
    try:
        # Ensure the input file exists before proceeding
        
        if not os.path.exists(input_file):
            print(f"Input file does not exist: {input_file}")
            return
        
        # Run the ffmpeg command to process the video with suppressed output
        
        subprocess.run([ffmpeg_path, "-i", input_file, output_file], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Video processed successfully: {output_file}")
    except Exception as e:
        print(f"An error occurred while processing the video: {e}")

def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  
            'ffmpeg_location': ffmpeg_path,  
            'postprocessors': [{ 
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Video downloaded successfully to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory(title="Select Folder to Save Video")
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
        print("Download and merging completed successfully.")
    else:
        print("Invalid save location.")
