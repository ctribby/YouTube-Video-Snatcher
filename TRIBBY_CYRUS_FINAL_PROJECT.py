# Program: TRIBBY_CYRUS_FINAL_PROJECT.py
# Author: Cyrus Tribby
# Date: 14 December 2021
# Summary: This program will allow users to download Youtube videos so they can view it later offline.

# Importing necessary packages

import tkinter as tk
from tkinter import ttk, messagebox    # These are all of the packages that much be imported for this program to work
from tkinter import *
from pytube import YouTube


# Main Screen
root = tk.Tk()
root.geometry("750x520")       # This is all the pertinent information about the GUI window.
root.resizable(True, True)
root.title("YouTube Video Snatcher")
root.config(background="khaki")

# Header
Label(root, text="Youtube Snatcher", font="Arial 24").pack()

# Link Entry
# This is the text box where the user will paste the URL for the YouTube video they wish to save
Label(root, text="Please paste (CTRL + V) your link here: ", font="Arial 14").pack()
link = StringVar()
link_entry = Entry(root, textvariable=link, width=60).pack()

# Forgot URL
urlErr = Label(root, font="Arial 12", bg="khaki", fg="red")   # This message will appear if the user does not paste an
urlErr.pack()                                                 # URL in the Link Entry box.

# Video Quality
Label(root, text="Please select what quality you would like your video", font="Arial 12").pack(pady=10)
choices = ["low", "high"]   # There is a drop-down box with these options
ytbChoices = ttk.Combobox(root, values=choices)
ytbChoices.pack()

# Storage Location
# Where the files will be saved at. The user MUST manually input where they want to save the videos here inside the
# parentheses.

storageLOC = "C:\Downloads"

# Download Button


def Download():   # Download code
    quality = ytbChoices.get()
    url = link.get()
    if len(url) > 0:
        msg["text"] = "Processing video from YouTube to Download...."  # Initial Message that will change to Line 53
        ytb_url = YouTube(url, on_progress_callback=progressBar)

# These lines help sort the stream to allow for the best quality to be downloaded
        video = ytb_url.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc()
        msg["text"] = "Downloading " + ytb_url.title   # This will be shown as the video is downloading
        if quality == choices[0]:
            video.last()
        else:
            video.first()

# This is shown after the video has downloaded successfully
        msg["text"] = "Video Downloaded Successfully!!"
        messagebox.showinfo("Awesome!!", "Your video downloaded and is saved at " + storageLOC)
    else:
        urlErr["text"] = "Don't forget the URL!!"   # This is the message referred to in Line 30


download_b = Button(root, text="Download the Video", command=Download, bg="LightGray", fg="black",
                    width=17, height=2).pack(pady=5)   # Actual Download button


# Progress Bar
def progressBar(stream, bytes_remaining):   # This shows the progress bar moving as the download progresses
    progress = int(((stream.filesize - bytes_remaining) / stream.filesize) * 100)
    bar["value"] = progress


bar = ttk.Progressbar(root, length=250)   # Bar display
bar.pack(pady=15)

# Downloading Message
msg = Label(root, font="Arial 12", bg="khaki", fg="black")   # Message that appears after successful download
msg.pack()

root.mainloop()
