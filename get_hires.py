import os
import sys
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import torchaudio

def is_highres_audio(file_path):
    """Check if a FLAC file is high-resolution audio."""
    try:
        info = torchaudio.info(file_path)
        return info.sample_rate > 44100 and info.bits_per_sample > 16
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
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
