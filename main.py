from customtkinter import *
from image_watermarker import watermark_image


def load_main():
    main_screen.pack(fill=BOTH, expand=True)
    start_screen.pack_forget()
    finish_screen.pack_forget()


def upload_file():
    filename = filedialog.askopenfilename(initialdir="~/", title="Select image", filetypes=(("png files", "*.png*"),
                                                                                            ("jpg files", "*.jpg*"),
                                                                                            ("jpeg files", "*.jpeg*"),
                                                                                            ("all files", "*.*")))
    if filename:
        watermark_image(filename, watermark_text.get())
        load_finish()


def load_finish():
    finish_screen.pack(fill=BOTH, expand=True)
    main_screen.pack_forget()


set_widget_scaling(1.3)
win = CTk()
win.title("Image Watermarker")
win.geometry("700x500")
win.config(padx=50, pady=50)

start_screen = CTkFrame(win)
main_screen = CTkFrame(win)
finish_screen = CTkFrame(win)

# Start Screen
start_screen.pack(fill=BOTH, expand=True)
welcome_label = CTkLabel(start_screen, text="Welcome to \nImage Watermarker", font=("Default", 30, "normal"))
welcome_label.pack(pady=70)

start_btn = CTkButton(start_screen, text="Start", command=load_main)
start_btn.pack()

# Main Screen
select_label = CTkLabel(main_screen, text="Select the image you want to watermark...", font=("Default", 20, "normal"))
select_label.pack(pady=40)

watermark_label = CTkLabel(main_screen, text="Enter text for watermark")
watermark_label.pack()
watermark_text = CTkEntry(main_screen)
watermark_text.pack(pady=20)

select_file_btn = CTkButton(main_screen, text="Upload Image",  command=upload_file)
select_file_btn.pack(pady=20)

# Finish Screen
finish_label = CTkLabel(finish_screen, text="Watermark Applied", text_color="green", font=("Default", 18, "normal"))
finish_label.pack(pady=70)

back_btn = CTkButton(finish_screen, text="⬅ Go Back", command=load_main)
back_btn.pack()

win.mainloop()
