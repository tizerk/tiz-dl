from PIL import Image
import customtkinter as ctk
import tkinter as tk
import os
import main
import video
import audio


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x250")

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


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
        self.button = ctk.CTkButton(
            self.entry_frame,
            text="Continue",
            command=lambda: self.video_data(
                title_var,
                creator_var,
                date_var,
                video_resolution_variable,
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
        audio_format_variable = ctk.IntVar(value=0)
        for i in range(len(audio_formats)):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"{audio_formats[i]}",
                value=i,
                variable=audio_format_variable,
            )
            radiobutton.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_buttons.append(radiobutton)

        self.button = ctk.CTkButton(
            self,
            text="Start!",
            command=lambda: self.download(
                audio_format_variable.get(),
                video_format_variable.get(),
                video_resolution_variable.get(),
                audio_formats,
                video_formats,
            ),
        )
        self.button.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.grid_columnconfigure(0, weight=1)
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
            ".WEBM",
            ".MOV",
            ".MKV",
            ".AVI",
            ".WMV",
            ".FLV",
            ".3GP",
        ]
        video_format_variable = ctk.IntVar(value=0)
        for i in range(len(video_formats)):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"{video_formats[i]}",
                value=i,
                variable=video_format_variable,
            )
            radiobutton.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_buttons.append(radiobutton)
        self.radio_var = ctk.IntVar(value=0)
        video_resolution_variable = ctk.StringVar(value="2160p")
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.tabview.tab("Video"), label_text="Resolution"
        )
        self.scrollable_frame.grid(
            row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_buttons = []

    def test(self):
        print("button pressed")

    def rc_popup(self, e):
        self.rc_menu.tk_popup(e.x_root, e.y_root)

    def right_click(self):
        self.entry.insert(0, self.clipboard_get())

    def resolution_buttons(
        self,
        video_resolution_variable,
        resolution_choices,
    ):
        self.scrollable_frame_buttons = []
        for i in range(len(resolution_choices)):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"{resolution_choices[len(resolution_choices) - 1 - i]['format_note']}",
                value=f"{resolution_choices[len(resolution_choices) - 1 - i]['format_note']}",
                variable=video_resolution_variable,
            )
            radiobutton.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_buttons.append(radiobutton)
        return resolution_choices

    def video_data(
        self,
        title_var,
        creator_var,
        date_var,
        video_resolution_variable,
    ):
        self.resolution_buttons(
            video_resolution_variable,
            main.get_video_data(
                self.entry.get(),
                title_var,
                creator_var,
                date_var,
            ),
        )

    def open_toplevel(self, message):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            self.toplevel_window.label.configure(text=message)
        else:
            self.toplevel_window.focus()

    def download(
        self,
        audio_choice,
        video_format_choice,
        video_resolution_choice,
        audio_formats,
        video_formats,
    ):
        if main.url_check(self.entry.get()):
            if self.tabview.get() == "Video":
                print(int(video_resolution_choice[:-1]))
                video.download_video(
                    self.entry.get(),
                    int(video_resolution_choice[:-1]),
                    video_formats[video_format_choice],
                )
            else:
                audio.download_audio(self.entry.get(), audio_formats[audio_choice])
        else:
            self.open_toplevel("URL not found!  Please re-enter the URL.")


app = App()
app.mainloop()
