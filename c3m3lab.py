# Dog Class Challenge (Deep Copy)
import copy  # for deepcopy

# Dog class with name and breed
class Dog:
    def __init__(self, name, breed):
        self.name = name        # string
        self.breed = breed      # string
    
    def bark(self):
        print("Woof, woof!")

# Instantiate dog1
dog1 = Dog("Marceline", "German Shepherd")

# Deep copy dog1 → dog2
dog2 = copy.deepcopy(dog1)

# Modify dog2 attributes
dog2.name = "Cajun"
dog2.breed = "Belgian Malinois"

# Print results
print(dog1.name, dog1.breed)   # original
print(dog2.name, dog2.breed)   # modified copy

# Instantiate my_dog
my_dog = Dog("Brutus", "Pomeranian")

my_dog.bark()

# Lab 1: Post Class
# Define Post object with all required attributes
class Post:
    """Create a post object for the fictitious social network Photogram"""
    def __init__(self, username, user_id, media, avatar,
                 comment_button, caption, likes, comments, like_button):
        self.username = username            # string
        self.user_id = user_id              # int
        self.media = media                  # path string
        self.avatar = avatar                # path string
        self.comment_button = comment_button  # path string
        self.caption = caption              # string
        self.likes = likes                  # int
        self.comments = comments            # list of strings
        self.like_button = like_button      # path string

# Instantiate post1 with variables
username = "Sally_17"
user_id = 112010
media = "student_folder/img/photogram/waterfall.png"
avatar = "student_folder/img/photogram/avatar_icon.png"
comment_button = "student_folder/img/photogram/add_comment.png"
caption = "First time at Yosemite. It has surpassed all of my expectations."
likes = 23
comments = ["Beautiful!", "I wish I was there too.", "Is that Nevada Falls?"]
like_button = "student_folder/img/photogram/likes_icon.png"

post1 = Post(username, user_id, media, avatar, comment_button,
             caption, likes, comments, like_button)

# Print all attributes to verify
print(post1.username)     # Sally_17
print(post1.user_id)      # 112010
print(post1.media)        # student_folder/img/photogram/waterfall.png
print(post1.avatar)       # student_folder/img/photogram/avatar_icon.png
print(post1.comment_button) # student_folder/img/photogram/add_comment.png
print(post1.caption) # First time at Yosemite. It has surpassed all of my expectations.
print(post1.likes)   # 23
print(post1.comments) # ['Beautiful!', 'I wish I was there too.', 'Is that Nevada Falls?']
print(post1.like_button) # student_folder/img/photogram/likes_icon.png

# Print a few attributes to verify
print(post1.username, post1.user_id, post1.caption, post1.likes)
   # Sally_17 112010 First time at Yosemite. It has surpassed all of my expectations. 23

# Lab 3: Photogram Window Setup
import tkinter

# Post class placeholder (already defined in Lab 1)
# class Post:
#    """Create a post object for Photogram"""
    ##########
    # The rest of the Post class code goes here
    ##########

# Window setup
window = tkinter.Tk()
window.title("Photogram")
window.geometry("800x500")
window.configure(background="white")

# Column weight configuration
window.grid_columnconfigure(1, weight=0)
window.grid_columnconfigure(2, weight=1)

# window.mainloop()

# Lab 3: add Photo Variables + Main Photo
# import tkinter

# -----------------------------------------
# Post class (already defined in Lab 1)
# -----------------------------------------
# class Post:
#     """Create a post object for Photogram"""
#     def __init__(self, username, user_id, media, avatar,
#                  comment_button, caption, likes, comments, like_button):
#         self.username = username
#         self.user_id = user_id
#         self.media = media
#         self.avatar = avatar
#         self.comment_button = comment_button
#         self.caption = caption
#         self.likes = likes
#         self.comments = comments
#         self.like_button = like_button

# -----------------------------------------
# post1 instantiation (already done in Lab 1)
# -----------------------------------------
# post1 = Post(username, user_id, media, avatar, comment_button,
#              caption, likes, comments, like_button)

# Window setup
# window = tkinter.Tk()
# window.title("Photogram")
# window.geometry("800x500")
# window.configure(background="white")

# Column weight configuration
# window.grid_columnconfigure(1, weight=0)
# window.grid_columnconfigure(2, weight=1)

# Now load images and place widgets
# Photo commented out 
# photo = tkinter.PhotoImage(file=post1.media)
# Commented out since photo is not available
# comment_button_img = tkinter.PhotoImage(file=post1.comment_button)
# avatar_img = tkinter.PhotoImage(file=post1.avatar)
# like_button_img = tkinter.PhotoImage(file=post1.like_button)

# Main photo label
# Commented out
# image = tkinter.Label(
#    window,
#    image=photo,
#    bg="white"
#)
# image.grid(
#    row=0,
#    column=0,
#    rowspan=10,   # span 10 rows
#    sticky="W"    # stick left
# )

# window.mainloop()

# Lab 4: Avatar, Username, Caption, Comment Button
# Avatar label
user_avatar = tkinter.Label(
    window,
#    image=avatar_img,
    width=30,
    bg="white"
)
user_avatar.grid(row=0, column=1, sticky="W")

# Username label
user_name = tkinter.Label(
    window,
    text=post1.username,
    font="DejaVuSans 14 bold",
    justify="left",
    bg="white"
)
user_name.grid(row=0, column=2, sticky="W")

# Caption label
caption_label = tkinter.Label(
    window,
    text=post1.caption,
    font="DejaVuSans 14",
    wraplength=300,
    justify="left",
    bg="white"
)
caption_label.grid(row=1, column=1, columnspan=2, sticky="NW")

# Comment button label
comment_icon = tkinter.Label(
    window,
#    image=comment_button_img,
    bg="white",
    justify="center"
)
comment_icon.grid(row=2, column=1, columnspan=2)

# Lab 5: Comments + Likes
# Loop through comments list
for comment in post1.comments:
    tkinter.Label(
        window,
        text=comment,
        font="DejaVuSans 14",
        wraplength=300,
        justify="left",
        bg="white"
    ).grid(
        row=post1.comments.index(comment) + 3,  # row offset
        column=1,
        columnspan=5,
        sticky="NW"
    )

# Like icon
likes_icon = tkinter.Label(
    window,
#    image=like_button_img,
    bg="white",
    justify="center"
)
likes_icon.grid(row=9, column=1)

# Likes count
likes_count = tkinter.Label(
    window,
    font="DejaVuSans 14",
    text=post1.likes,
    bg="white",
    justify="left"
)
likes_count.grid(row=9, column=2, sticky="W", columnspan=2)

# -----------------------------------------
# Final mainloop
# -----------------------------------------
window.mainloop()

