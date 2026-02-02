from moviepy import VideoFileClip

video=input("Enter path of video: ")
name=input("Enter the name you want to save the gif as: ")
videoClip = VideoFileClip(video)
videoClip.write_gif(name+".gif")