# Lab 2: Tkinter Basics
import tkinter  # Tkinter module

window = tkinter.Tk()            # create window
window.title("My Window")        # window title
window.geometry("500x350")       # window size

# Text label
my_label = tkinter.Label(
    window,
    text="Hello World",
    font="DejaVuSerif 18",
    justify="left",   # text alignment
    bg="yellow",       # background color
    fg="black",       # text color
    wraplength=200    # wrap text after 200px
)
my_label.grid(row=0, column=0)   # place label

# Load image file and attach to a Label
# feather_image = tkinter.PhotoImage(file="student_folder/img/feather.png")
# image_label = tkinter.Label(window, image=feather_image)
# image_label.grid(row=1, column=1)

window.mainloop()                # run window