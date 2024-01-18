import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
from moviepy.editor import VideoClip, concatenate_videoclips, VideoFileClip , CompositeAudioClip , AudioFileClip
from moviepy.video import fx
from moviepy.audio import  AudioClip
from TextProcessing import putText
from random import randint
from os import listdir , remove
from shutil import move

quotes = [
"Turn your can'ts into cans and your dreams into plans.",
"Bold decisions create powerful stories.",
"Every moment is a fresh beginning; take control and make it count.",
"Don't be a passenger in your own life; be the driver.",
"Life is 10% what happens to us and 90% how we respond to it.",
"Rise above the storm, and you will find the sunshine.",
"Command your life, don't just demand from it.",
"Make your vision so clear that your fears become irrelevant.",
"The secret to getting ahead is getting started.",
"Control your mind, and you'll control your life."

]

themes = listdir("music")
Compthemes = []

for music in themes:
    theme = AudioFileClip("music/" + music)
    Compthemes.append(theme)



imgs = listdir("images")
outro = VideoFileClip("outro.mp4")
for quote in quotes:
    print(quote)
    
    nameList = [imgs[randint(0 , len(imgs) // 2) ] , imgs[randint(len(imgs) // 2 , len(imgs))]]
    clips = []

    for name in nameList:
        img = cv.imread("images/" + name)
        img = cv.resize(img, (1080, 1920))

        if name.startswith("top"):
            alignment = "top"
        elif name.startswith("bottom"):
            alignment = "bottom"
        else:
            alignment = "center"

        text = quote
        # Assuming you have the `putText` function implemented in TextProcessing module
        img = putText(img, text, ImageFont.truetype("consola.ttf", 60),
                    alignV=alignment, color=(255, 255, 255), letterSpacing=2)

        def make_frame(t):
            # Note: Using t to interpolate frames over time
            frame = img.copy()
            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            return frame_rgb

        duration = 5
        fade_duration = 1.5

        # Create a new VideoClip for each image
        video_clip = VideoClip(make_frame, duration=duration)

        # Apply fadein and fadeout effects separately
        video_clip = fx.all.fadein(video_clip, fade_duration)
        video_clip = fx.all.fadeout(video_clip, fade_duration)
        video_clip.write_videofile(f"{name}.mp4", fps=24, codec="libx264")


    clips = []
    for file in nameList:
        file += ".mp4"
        clips.append(VideoFileClip(file))

    clips.append(outro)
    final_clip = concatenate_videoclips(clips)
    final_clip.audio = Compthemes[randint(0 , len(Compthemes) - 1)]
    output = f"{quote[:10]}.mp4"
    final_clip.write_videofile(output, fps=24, codec="libx264")

    move(output , "output/"+ output)

    for name in nameList:
        remove(f"{name}.mp4")

