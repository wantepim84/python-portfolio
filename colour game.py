# import the modules
import tkinter
import random

# list of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

# Initialize game variables
score = 0
timeleft = 30
current_colour = ""
current_word = ""

# Function to start the game
def startGame(event=None):
    global timeleft
    global score
    if timeleft == 30:
        countdown()  # Start the countdown timer
    nextColour()

# Function to choose and display the next colour
def nextColour():
    global score
    global current_colour
    global current_word

    # If a game is currently in play
    if timeleft > 0:
        # Check if the input matches the current colour
        if e.get().lower() == current_colour.lower():
            score += 1

        # Clear the text entry box and shuffle the colours
        e.delete(0, tkinter.END)
        random.shuffle(colours)

        # Set the new word and colour
        current_word = colours[0]
        current_colour = colours[1]

        # Update the label to show the next colour to guess
        label.config(fg=current_colour, text=current_word)

        # Update the score label
        scoreLabel.config(text="Score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft

    if timeleft > 0:
        # Decrement the timer
        timeleft -= 1

        # Update the time left label
        timeLabel.config(text="Time left: " + str(timeleft))

        # Run the function again after 1 second
        timeLabel.after(1000, countdown)
    else:
        # Display final score when time is up
        resultLabel.config(
            text=f"Time's up! Your final score is {score}\nPress 'Restart' to play again")

# Function to restart the game
def restartGame():
    global timeleft
    global score
    global current_colour
    global current_word

    # Reset the game variables
    score = 0
    timeleft = 30
    current_colour = ""
    current_word = ""
    scoreLabel.config(text="Score: " + str(score))
    timeLabel.config(text="Time left: " + str(timeleft))
    resultLabel.config(text="")  # Clear any result message
    nextColour()  # Set the first word and colour
    countdown()  # Start the countdown timer

# Create a GUI window
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x250")  # Increased height to accommodate resultLabel

# Add an instructions label
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# Add a score label
scoreLabel = tkinter.Label(
    root, text="Press Enter to Start", font=('Helvetica', 12))
scoreLabel.pack()

# Add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Add a result label for displaying final score and restart prompt
resultLabel = tkinter.Label(root, text="", font=('Helvetica', 12))
resultLabel.pack()

# Add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Add a text entry box for typing in colours
e = tkinter.Entry(root)
e.pack()
e.focus_set()

# Add a restart button
restartButton = tkinter.Button(
    root, text="Restart", command=restartGame, font=('Helvetica', 12))
restartButton.pack()

# Bind the Enter key to start the game
root.bind('<Return>', startGame)

# Start the GUI loop
root.mainloop()
