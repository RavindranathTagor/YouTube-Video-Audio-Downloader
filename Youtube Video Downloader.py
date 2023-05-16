import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")

        # Set background color of root window to white
        root.configure(background='#f6fff8')





        # Define YouTube color palette
        youtube_red = '#eaf4f4'  #directory and download selection inside box
        youtube_dark_gray = '#cce3de'  #selection outline box
        youtube_light_gray = '#a4c3b2'
        youtube_black = '#6b9080'  #text selction like resoultion and audio
        youtube_white = '#588b8b'   #text inside box

        # create a custom style for the GUI
        style = ttk.Style()
        style.configure('TLabel', background=youtube_dark_gray, foreground=youtube_white, font=('Roboto', 15,'bold'))
        style.configure('TButton', background=youtube_red, foreground=youtube_white, font=('Open Sans', 15, 'bold'))
        style.configure('TCombobox', background=youtube_light_gray, foreground=youtube_black, font=('Lato', 15,'bold'))
        style.configure('TEntry', background=youtube_light_gray, foreground=youtube_black, font=('Verdana ', 15,'bold'))

        # create URL entry field
        self.url_label = ttk.Label(root, text="Enter YouTube video URL:")
        self.url_label.pack(padx=10, pady=10)
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack(padx=10)

        # create download type selection field
        self.download_type_label = ttk.Label(root, text="Select download type:")
        self.download_type_label.pack(padx=10, pady=10)
        self.download_type_choices = ttk.Combobox(root, values=["Video (mp4)", "Audio"])
        self.download_type_choices.current(0)
        self.download_type_choices.pack(padx=10)

        # create format and resolution selection fields
        self.format_label = ttk.Label(root, text="Select format:")
        self.format_label.pack(padx=10, pady=10)
        self.format_choices = ttk.Combobox(root, values=["mp4", "audio(mp3)"])
        self.format_choices.current(0)
        self.format_choices.pack(padx=10)

        self.resolution_label = ttk.Label(root, text="Select resolution:")
        self.resolution_label.pack(padx=10, pady=10)
        self.resolution_choices = ttk.Combobox(root, values=["144p", "240p", "360p", "480p", "720p", "1080p"])
        self.resolution_choices.current(4)
        self.resolution_choices.pack(padx=10)

        # create directory selection button
        self.directory_button = ttk.Button(root, text="Select directory", command=self.select_directory)
        self.directory_button.pack(padx=10, pady=10)

        # create download button
        self.download_button = ttk.Button(root, text="Download", command=self.download)
        self.download_button.pack(padx=10, pady=10)

    def select_directory(self):
        # open file dialog to select download directory
        self.directory = filedialog.askdirectory()
        if self.directory:
            directory_label = ttk.Label(self.root, text=f"Download directory: {self.directory}")
            directory_label.pack(padx=10, pady=10)

    def download(self):
        # get video URL from entry field
        video_url = self.url_entry.get()

        # create YouTube object from video URL
        yt = YouTube(video_url)

        # filter available streams based on
        # filter available streams based on user input
        download_type_choice = self.download_type_choices.get()
        if download_type_choice == "Video (mp4)":
            format_choice = self.format_choices.get()
            resolution_choice = self.resolution_choices.get()
            streams = yt.streams.filter(progressive=True, file_extension=format_choice, res=resolution_choice)
            stream = streams.first()
        elif download_type_choice == "Audio":
            streams = yt.streams.filter(only_audio=True)
            stream = streams.first()

        # display selected video details
        title_label = ttk.Label(self.root, text=f"Title: {yt.title}")
        title_label.pack()
        filesize_label = ttk.Label(self.root, text=f"Filesize: {stream.filesize / (1024 * 1024):.2f} MB")
        filesize_label.pack()

        # download video or audio to selected directory
        if self.directory:
            stream.download(output_path=self.directory)
        else:
            stream.download()

        # display download complete message
        download_complete_label = ttk.Label(self.root, text="Yahooo...Download complete!")
        download_complete_label.pack(pady=10)

    # create GUI window
root = tk.Tk()
app = YouTubeDownloader(root)
root.mainloop()
