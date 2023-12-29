import os
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import torchaudio


from sys import argv

def is_highres_audio(file_path):
    """Check if a FLAC file is high-resolution audio."""
    info = torchaudio.info(file_path)
    sample_rate = int(info.sample_rate)
    bit_depth = int(info.bits_per_sample)
    return sample_rate > 44100 and bit_depth > 16

def find_highres_flac_files(directory):
    """Recursively find high-resolution FLAC files in a directory."""
    highres_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.flac'):
                file_path = os.path.join(root, file)
                if is_highres_audio(file_path):
                    highres_files.append(file_path)
    return highres_files

# Example usage

directory_to_search = argv[1]
highres_flac_files = find_highres_flac_files(directory_to_search)
for file in highres_flac_files:
    print(file)
