from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import json

clips_folder = input("Clips source folder: ")
with open(f"{clips_folder}/clips.json") as f:
    data = json.loads(f.read())

clip_id = 0
for item in data['clips']:
    try:
        clip_id += 1
        ffmpeg_extract_subclip(f"{clips_folder}/{item['video_title']}.mp4", item['start_time'], item['end_time'], targetname=f"{clips_folder}/processed/{item['video_title']}_{clip_id}.mp4")
    except Exception as e:
        print(e)
        
