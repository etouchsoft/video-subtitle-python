import cv2
import json
import argparse
import moviepy.editor as mp
import subprocess

parser = argparse.ArgumentParser(description='A Video subtitle adding program.')

parser.add_argument("source_video_name", help="Enter source video name.")
parser.add_argument("source_wordfile_name", help="Enter source transctibe word name.")
parser.add_argument("audio_file_name", help="Enter Extracted audio mp3 name.")
parser.add_argument("output_video_name", help="Enter output video name.")

args = parser.parse_args()

# Create a VideoCapture object from your mp4 video
cap = cv2.VideoCapture(args.source_video_name)
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)
 
# Define the codec and create VideoWriter object.
out = cv2.VideoWriter(args.output_video_name,cv2.VideoWriter_fourcc(*'MP4V'), fps, (frame_width,frame_height))
timestamps = [cap.get(cv2.CAP_PROP_POS_MSEC)]
calc_timestamps = [0.0]
ct = 0
second = 0

with open(args.source_wordfile_name, 'r') as f:
    data =f.read()
    try:
        data = json.loads(data)
    except:
        print("Your text file does not have a proper json format supported data")

while(True):
    ct += 1
    ret, frame = cap.read()
 
    if ret == True: 
    
        font = cv2.FONT_HERSHEY_SIMPLEX
        t = cap.get(cv2.CAP_PROP_POS_MSEC)
        i = 0
        for j in range(0,len(data)):
            if j%2 != 0:
                continue
            if i < len(data) - 1:
                ds = data[i]
                de = data[i+1]

                if ds['start'] < t < de['end']:
                    word = f"{ds['text']} {de['text']}"
                    col_string = ""
                    cv2.putText(frame,
                                word,
                                (50, frame_height - 50),
                                font, 1,
                                (0, 0, 0),
                                2,
                                cv2.LINE_4)
                    if data[j]['start'] < t < data[j]['end']:
                        color_word = data[j]['text']
                        col_string = ""
                        for w in word.split(" "):
                            if w == color_word:
                                col_string += color_word
                            else:
                                col_string += len(w)*" "

                        cv2.putText(frame,
                                    col_string,
                                    (50, frame_height - 50),
                                    font, 1,
                                    (0, 255, 255),
                                    2,
                                    cv2.LINE_4)

                    if data[j+1]['start'] < t < data[j+1]['end']:
                        color_word = data[j+1]['text']
                        col_string = ""
                        for w in word.split(" "):
                            if w == color_word:
                                col_string += " "+color_word
                            else:
                                col_string += len(w)*" "

                        cv2.putText(frame,
                                    col_string,
                                    (50, frame_height - 50),
                                    font, 1,
                                    (0, 255, 255),
                                    2,
                                    cv2.LINE_4)

            i = i+2
        # Display the resulting frame    
        cv2.imshow('frame',frame)

        # Write the frame into the output file.
        out.write(frame)
    
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
  # Break the loop
    else:
        break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows()

my_clip = mp.VideoFileClip(args.source_video_name)
my_clip.audio.write_audiofile(args.audio_file_name)

subprocess.call(f'ffmpeg -i {args.output_video_name} -i {args.audio_file_name}\
                -c copy -map 0:v:0 -map 1:a:0 final-{args.output_video_name}',shell=True)