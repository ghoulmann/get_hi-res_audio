import os
import sys
from pymediainfo import MediaInfo

def is_highres_audio(file_path):
    """Check if a FLAC file is high-resolution audio using pymediainfo."""
    media_info = MediaInfo.parse(file_path)
    for track in media_info.tracks:
        if track.track_type == 'Audio':
            sample_rate = int(track.sampling_rate) if track.sampling_rate else 0
            bit_depth = int(track.bit_depth) if track.bit_depth else 0
            return sample_rate > 44100 and bit_depth > 16
    return False

def find_highres_flac_files(directory):
    """Recursively find high-resolution FLAC files in a directory."""
    highres_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.flac'):
                file_path = os.path.abspath(os.path.join(root, file))
                if is_highres_audio(file_path):
                    highres_files.append(file_path)
    return highres_files

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory_to_search = sys.argv[1]
    if not os.path.isdir(directory_to_search):
        print(f"The provided path '{directory_to_search}' is not a valid directory.")
        sys.exit(1)

    highres_flac_files = find_highres_flac_files(directory_to_search)
    for file in highres_flac_files:
        print(file)
