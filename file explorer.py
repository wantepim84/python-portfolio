import tkinter as tk
from tkinter import filedialog

def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=[("Text files", "*.txt*"),
                                                     ("All files", "*.*")])
    # Update label with the selected file
    label_file_explorer.config(text=f"File Opened: {filename}")

# Create the root window
window = tk.Tk()
window.title('File Explorer')
window.geometry("400x200")
window.config(background="white")

# Create and place widgets using pack()
label_file_explorer = tk.Label(window, text="File Explorer using Tkinter",
                               width=50, height=4, fg="blue", bg="white")
label_file_explorer.pack()

button_explore = tk.Button(window, text="Browse Files", command=browse_files)
button_explore.pack(pady=10)

button_exit = tk.Button(window, text="Exit", command=window.quit)
button_exit.pack(pady=10)

# Start the GUI event loop
window.mainloop()


