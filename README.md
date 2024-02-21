# List abs paths to "hi-res" flac files found in a directory structure

sample rate > 44100 Hz and bit depth > 16

## Flow

`arg 1` is the path to starting directory

`is_highres_audio` function return value possibilities based on script design:

1.  **Single 'Audio' Track (Most Common Case)**:
    
    *   If there's only one audio track, and it meets the high-resolution criteria (sample rate > 44100 Hz and bit depth > 16), the function returns `True`.
    *   If the audio track does not meet these criteria, it returns `False`.
2.  **Multiple Tracks Including Multiple 'Audio' Tracks**:
    
    *   If there are multiple audio tracks, it checks each track until it finds the first 'Audio' track and returns `True` or `False` based on this track's properties.
    *   You can change the script if want to consider a file high-resolution only if all audio tracks meet the criteria, you would need to modify the function to check each audio track and return `True` only if all of them meet the high-resolution criteria.
3.  **Non-Audio Tracks (Metadata, etc.)**:
    
    *   The function will skip these tracks and only evaluate the 'Audio' type tracks.
4.  **No 'Audio' Tracks**:
    
    *   If the file does not contain any 'Audio' tracks (which is unusual for a FLAC file but theoretically possible), the function will return `False`.
5.  **Error or Exception Cases**:
    
    *   If an error occurs during the processing of the tracks (e.g., a track's properties cannot be read), the errors are not handled.
