from PIL import Image
import customtkinter as ctk
import os
import video
import audio


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

        self.button = ctk.CTkButton(
            self.entry_frame,
            text="Continue",
        )
        self.button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.details_frame = ctk.CTkFrame(self)
        self.details_frame.grid_columnconfigure(0, weight=1)
        self.details_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.label = ctk.CTkLabel(
            self.details_frame,
            text="Title: ",
            fg_color="transparent",
            text_color="white",
        )
        self.label.grid(row=1, column=0, padx=(20, 0), pady=(10, 0), sticky="nsw")
        self.label = ctk.CTkLabel(
            self.details_frame,
            text="Creator: ",
            fg_color="transparent",
            text_color="white",
        )
        self.label.grid(row=2, column=0, padx=(20, 0), pady=0, sticky="nsw")
        self.label = ctk.CTkLabel(
            self.details_frame,
            text="Upload Date: ",
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

        # self.radiobutton_frame = RadiobuttonFrame(
        #     self.tabview.tab("Video"), "Resolution", [0, 1, 2, 3]
        # )
        # self.radiobutton_frame.grid(
        #     row=3, column=0, padx=10, pady=(10, 0), sticky="nsw"
        # )

        # self.radiobutton_frame = RadiobuttonFrame(
        #     self.tabview.tab("Video"), "Format", [0, 1, 2, 3]
        # )
        # self.radiobutton_frame.grid(
        #     row=3, column=1, padx=10, pady=(10, 0), sticky="nsw"
        # )

        # self.radiobutton_frame = RadiobuttonFrame(
        #     self.tabview.tab("Audio"), "Format", [0, 1, 2, 3]
        # )
        # self.radiobutton_frame.grid(
        #     row=3, column=0, padx=10, pady=(10, 0), sticky="nsw"
        # )

        self.radio_var = ctk.IntVar(value=0)
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.tabview.tab("Video"), label_text="Resolution"
        )
        self.scrollable_frame.grid(
            row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_buttons = []
        for i in range(10):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"Resolution {i}",
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
        for i in range(10):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"Format {i}",
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
        for i in range(10):
            radiobutton = ctk.CTkRadioButton(
                master=self.scrollable_frame,
                text=f"Format {i}",
                value=i,
                variable=self.radio_var,
            )
            radiobutton.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_buttons.append(radiobutton)

        self.button = ctk.CTkButton(self, text="Start!")
        self.button.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.grid_columnconfigure(0, weight=1)

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()
