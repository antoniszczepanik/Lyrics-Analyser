import tkinter as tk
from tkinter import ttk
from functions import *
import time


# All constants in GUI
TITLE_FONT = ("Verdana", 20)
MAIN_FONT = ("Verdana", 10)
INFO_FONT = ("Verdana", 8)
INFO = "Version: 0.0.1 \n\n" \
       "Author: Antoni Szczepanik \n\n"\
       "If you have any feedback please feel free to contact me at szczepanik.antoni@gmail.com"
WHAT = "This app let's you find top 10 most popular nouns and adjectives used by a specified author. It uses \n" \
       "LyricWiki as a source and it works only for english lyrics. Enjoy!"
RESULT_FIELD_TEXT = "Your results will be displayed here. \n\n" \
                    "Please be patient, downloading lyrics may take up to 45 seconds."
WINDOW_SIZE = "600x650"


class Words(tk.Tk):

    # Initialize MainFrame for all pages.
    # Pages are stored in tuple, inside a loop.

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Most popular lyrics words")
        tk.Tk.geometry(self, WINDOW_SIZE)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames ={}

        for Frame in (MainPage, InfoPage, WhatPage):

            frame = Frame(container, self)
            self.frames[Frame] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    # Function that shows frames

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

# Main page of the app
class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title label
        label = tk.Label(self, text="Most popular lyrics words", font=TITLE_FONT)
        label.pack(pady=10, padx=10)

        # Entry box
        self.input_artist = tk.StringVar()
        artist_name = tk.Entry(self, textvariable=self.input_artist)
        artist_name.pack(pady=10, padx=10)

        # Buttons
        go_button = ttk.Button(self, text="Let's go!",
                              command=lambda: self.result_getter())
        go_button.pack(pady=10, padx=10)
        info_button = ttk.Button(self, text="What is this all about?",
                                command=lambda: controller.show_frame(WhatPage))
        info_button.pack(pady=10, padx=10)
        info_button = ttk.Button(self, text="More info",
                                command=lambda: controller.show_frame(InfoPage))
        info_button.pack(pady=10, padx=10)

        # Results label
        self.result_label = tk.Label(self, text=RESULT_FIELD_TEXT, font=INFO_FONT)
        self.result_label.pack(pady=10, padx=10)

        # Runtime display label
        self.time_label = tk.Label(self, text="", font=INFO_FONT)
        self.time_label.pack(pady=10, padx=10)

        # Number of words display label
        self.number_of_words_label = tk.Label(self, text="", font=INFO_FONT)
        self.number_of_words_label.pack(pady=10, padx=10)

    # This function gets results and displays them in to the correct labels
    def result_getter(self):

        # Starting the timer
        start = time.time()

        self.result_label.configure(text=RESULT_FIELD_TEXT)
        text = self.input_artist.get()
        # If user typed something proceed, else, display cannot find message
        if len(text) > 0:
            try:
                # Getting results
                lyrics, number = get_lyrics(text)
                processed = process_lyrics(lyrics)
                noun_result = get_top(processed, "NOUN")
                adj_result = get_top(processed, "ADJ")
                # Configuring labels
                self.result_label.configure(
                    text=(str(noun_result) + "\n ------------------------- \n\n" + str(adj_result)))
                # Stoping the timer
                calc_time = time.time() - start
                self.time_label.configure(text="The operation took " + str(calc_time)[0:5] + " seconds.")
                self.number_of_words_label.configure(text="Found " + str(number) + " songs for specified artist.")

            except Exception:
                # Display cannot find message
                self.result_label.configure(text="I can not find this artist. Are you sure you typed it right?")
                self.time_label.configure(text="")
                self.number_of_words_label.configure(text="")
        else:
            # Display cannot find message
            self.result_label.configure(text="Input field is empty. You need to give me name of the artist!")
            self.time_label.configure(text="")
            self.number_of_words_label.configure(text="")


# A page with info about what this app does
class WhatPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # Info label
        label = tk.Label(self, text=WHAT, font=INFO_FONT)
        label.pack(pady=10, padx=10)

        # Go back button
        back_button = ttk.Button(self, text="Ok, I got it!",
                                command=lambda: controller.show_frame(MainPage))
        back_button.pack()


# A page with other informations
class InfoPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # Info label
        label = tk.Label(self, text=INFO, font=INFO_FONT)
        label.pack(pady=10, padx=10)

        # Go back button
        back_button = ttk.Button(self, text="Let's go back",
                                command=lambda: controller.show_frame(MainPage))
        back_button.pack()







