## This script will add a subtitle with highlighted text in your Video.

## How to use a video subtitle script
- Prerequisite: Following python libraries are required for Python3.5+.
    1. opencv-python
    2. moviepy
    3. ffmpeg

- Run a Script:
    python video-subtitle.py [source video name] [transcribe txt file] [audio file any name with extension] [output file name]

    Example: `python video-subtitle.py myinputvideo.mp4 mytranscribe.txt audionameany.mp3 final-output.mp4`
    
    Transcribe file should contain json data with start and end time with word:
    Example: `[{"text": "Hello", "start": 170, "end": 586},{"text": "MySelf", "start": 900, "end": 1350}, {"text": "Robert", "start": 1400, "end": 1460}, {"text": "Dean", "start": 1510, "end": 1586},
{"text": "I", "start": 1710, "end": 1886}, {"text": "am", "start": 1910, "end": 2186},
{"text": "a", "start": 2210, "end": 2586},{"text": "Software", "start": 2610, "end": 2786},
{"text": "Engineer", "start": 2810, "end": 3586},{"text": "Good", "start": 5810, "end": 6586},{"text": "Bye", "start": 2810, "end": 3586}]`


