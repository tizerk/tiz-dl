from PIL import Image
import customtkinter as ctk
import tkinter as tk
import os
import video
import audio
import main


class RadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(
            self, text=self.title, fg_color="gray30", corner_radius=6
        )
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.title.grid_columnconfigure(0, weight=1)

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(
                self, text=value, value=value, variable=self.variable
            )
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("YTiz")
        self.geometry(f"{600}x{600}")

        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.grid(
            row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew"
        )
        self.entry_frame.grid_columnconfigure(0, weight=1)
        self.entry = ctk.CTkEntry(
            self.entry_frame,
            placeholder_text="Enter URL Here...",
        )
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.rc_menu = tk.Menu(self.entry, tearoff=False)
        self.rc_menu.add_command(label="Paste URL", command=self.right_click)
        self.entry.bind("<Button-3>", self.rc_popup)
        title_var = ctk.StringVar(self, "Title: ")
        creator_var = ctk.StringVar(self, "Creator: ")
        date_var = ctk.StringVar(self, "Upload Date: ")
        video_resolutions = []
        self.button = ctk.CTkButton(
            self.entry_frame,
            text="Continue",
            command=lambda: main.get_video_data(
                self.entry.get(), title_var, creator_var, date_var
            ),
        )
        self.button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.details_frame = ctk.CTkFrame(self)
        self.details_frame.grid_columnconfigure(0, weight=1)
        self.details_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.label = ctk.CTkLabel(
            self.details_frame,
            textvariable=title_var,
            fg_color="transparent",
            text_color="white",
        )
        self.label.grid(row=1, column=0, padx=(20, 0), pady=(10, 0), sticky="nsw")
        self.label = ctk.CTkLabel(
            self.details_frame,
            textvariable=creator_var,
            fg_color="transparent",
            text_color="white",
        )
        self.label.grid(row=2, column=0, padx=(20, 0), pady=0, sticky="nsw")
        self.label = ctk.CTkLabel(
            self.details_frame,
            textvariable=date_var,
            fg_color="transparent",
            text_color="white",
        )
        self.label.grid(row=3, column=0, padx=(20, 0), pady=(0, 10), sticky="nsw")

        self.tabview = ctk.CTkTabview(self, width=250)
        self.tabview.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview.add("Video")
        self.tabview.add("Audio")
        self.tabview.tab("Video").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Video").grid_columnconfigure(1, weight=1)
        self.tabview.tab("Audio").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Audio").grid_columnconfigure(1, weight=1)

        self.radio_var = ctk.IntVar(value=0)
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.tabview.tab("Video"), label_text="Resolution"
        )
        self.scrollable_frame.grid(
            row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_buttons = []
        resolution_options = []
        for i in range(len(resolution_options)):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"{resolution_options[i]}",
                value=i,
                variable=self.radio_var,
            )
            radiobutton.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_buttons.append(radiobutton)

        self.radio_var = ctk.IntVar(value=0)
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.tabview.tab("Video"), label_text="Format"
        )
        self.scrollable_frame.grid(
            row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_buttons = []
        video_formats = [
            ".MP4",
            ".MOV",
            ".WEBM",
            ".MKV",
            ".AVI",
            ".WMV",
            ".FLV",
            ".3GP",
            ".M4A",
        ]
        for i in range(len(video_formats)):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"{video_formats[i]}",
                value=i,
                variable=self.radio_var,
            )
            radiobutton.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_buttons.append(radiobutton)

        self.radio_var = ctk.IntVar(value=0)
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.tabview.tab("Audio"), label_text="Format"
        )
        self.scrollable_frame.grid(
            row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsw"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_buttons = []
        audio_formats = [
            ".MP3",
            ".FLAC",
            ".WAV",
            ".AAC",
            ".WEBM",
            ".MOV",
            ".OGG",
            ".OPUS",
            ".AIFF",
            ".M4A",
        ]
        for i in range(len(audio_formats)):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"{audio_formats[i]}",
                value=i,
                variable=self.radio_var,
            )
            radiobutton.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_buttons.append(radiobutton)

        self.button = ctk.CTkButton(self, text="Start!")
        self.button.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.grid_columnconfigure(0, weight=1)

    def test(self):
        print("button pressed")

    def rc_popup(self, e):
        self.rc_menu.tk_popup(e.x_root, e.y_root)

    def right_click(self):
        self.entry.insert(0, self.clipboard_get())


app = App()
app.mainloop()
