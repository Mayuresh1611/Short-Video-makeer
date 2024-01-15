import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
from moviepy.editor import VideoClip, concatenate_videoclips, VideoFileClip , CompositeAudioClip , AudioFileClip
from moviepy.video import fx
from moviepy.audio import  AudioClip
from TextProcessing import putText

nameList = ["img1.jpg", "img2.jpg"]
clips = []

# for name in nameList:
#     img = cv.imread(name)
#     img = cv.resize(img, (1080, 1920))

#     text = "Only you can make it through"
#     # Assuming you have the `putText` function implemented in TextProcessing module
#     img = putText(img, text, ImageFont.truetype("fonts/BungeeSpice-Regular.ttf", 60),
#                   alignV="bottom", color=(255, 0, 0), glow=False, letterSpacing=20)

#     def make_frame(t):
#         # Note: Using t to interpolate frames over time
#         frame = img.copy()
#         frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
#         return frame_rgb

#     duration = 10
#     fade_duration = 2

#     # Create a new VideoClip for each image
#     video_clip = VideoClip(make_frame, duration=duration)

#     # Apply fadein and fadeout effects separately
#     video_clip = fx.all.fadein(video_clip, fade_duration)
#     video_clip = fx.all.fadeout(video_clip, fade_duration)
#     video_clip.write_videofile(f"{name}.mp4", fps=24, codec="libx264")


clips = []

for file in nameList:
    file += ".mp4"
    clips.append(VideoFileClip(file))
final_clip = concatenate_videoclips(clips)
theme =  AudioFileClip("theme.mp3")
theme = CompositeAudioClip([theme])
final_clip.audio = theme
final_clip.write_videofile("output_video.mp4", fps=24, codec="libx264")
