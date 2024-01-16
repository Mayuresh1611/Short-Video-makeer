import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
from moviepy.editor import VideoClip, concatenate_videoclips, VideoFileClip , CompositeAudioClip , AudioFileClip
from moviepy.video import fx
from moviepy.audio import  AudioClip
from TextProcessing import putText
from random import randint
from os import listdir , remove
from shutil import move

quotes = ["Take control or be controlled.",
"Your life, your rules.",
"Own your story, dictate your destiny.",
"Don't just exist, live with intent.",
"Your life is your canvas; paint it with purpose.",
"Seize the day, control your destiny.",
"The power to change is within you.",
"You are not a product of your circumstances; you are a product of your decisions.",
"Embrace the uncertainty, control the outcome.",
"Don't let the noise of others drown out your inner voice."
]

theme =  AudioFileClip("theme.mp3")
theme = CompositeAudioClip([theme])

imgs = listdir("images")

for quote in quotes:
    print(quote)
    
    nameList = [imgs[randint(0 , 23)] , imgs[randint(24 , 47)]]
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
        img = putText(img, text, ImageFont.truetype("consola.ttf", 50),
                    alignV=alignment, color=(255, 255, 255), letterSpacing=2)

        def make_frame(t):
            # Note: Using t to interpolate frames over time
            frame = img.copy()
            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            return frame_rgb

        duration = 3
        fade_duration = 1

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

    final_clip = concatenate_videoclips(clips)
    output = f"{quote[:10]}.mp4"
    final_clip.write_videofile(output, fps=24, codec="libx264")

    move(output , "output/"+ output)

    for name in nameList:
        remove(f"{name}.mp4")

