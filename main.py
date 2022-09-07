from tkinter import *
import pandas
import random

# Background color hex code defined:
BACKGROUND_COLOR = "#B1DDC6"
# Create an empty dictionary to update the canvas text inside next_card and flip_card
current_card = {}
# Create empty words_to_learn dict to make sure app tries to read file before creating it
words_to_learn = {}

# Read the words_to_learn.csv if it exists
try:
    data = pandas.read_csv("data/words_to_learn.csv")
# If the words_to_learn.csv does not exist, read the french_words.csv to create words_to_learn.csv
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
# Convert the data to a dictionary using the pandas.DataFrame.to_dict() operation
# The dict created is in a weird format, convert to "records" orientation
# "records" orientation gives each column's values as a list
else:
    words_to_learn = data.to_dict(orient="records")


# Function for the button commands (known_button and unknown_button)
def next_card():
    global current_card, flip_timer
    # Invalidate the timer every time you click a button (known or unknown)
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# Function for flipping the card after 3 seconds on the French word
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="yellow")
    canvas.itemconfig(card_word, text=current_card["English"], fill="yellow")
    # After the card flip, change the canvas card_background to the green image to distinguish
    canvas.itemconfig(card_background, image=card_back_img)


# Function for pushing "known" button in order to remove word from list since it's already learned
def is_known():
    # Grab the data dict and remove the current_card which is already learned
    words_to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(words_to_learn)
    # index=False removes the new index column every time you read the words_not_learned.csv
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Create the GUI window
window = Tk()
window.title("Language Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Flip the card after 3 seconds to show English word
flip_timer = window.after(3000, func=flip_card)

# use tkinter.PhotoImage operation to load the card_front and card_back image up
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# Use the card_front_img as the window's canvas (widget) -> allows you to overlap images on top
canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=card_front_img)
# column span the canvas across the two columns for the known/unknown buttons below
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Add text widget to the canvas object (language and word)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Cross and Check Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()