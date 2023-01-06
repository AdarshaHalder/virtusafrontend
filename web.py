import tkinter as tk
import webbrowser

def open_url():
    url = entry.get()
    webbrowser.open_new_tab(url)

# Create the main window
window = tk.Tk()
window.title("My Web Browser")

# Create a label and a text entry field
label = tk.Label(text="Enter a URL:")
entry = tk.Entry()

# Create a button to open the URL
button = tk.Button(text="Go", command=open_url)

# Add the widgets to the window
label.pack(side="left")
entry.pack(side="left")
button.pack(side="left")

# Run the main loop
window.mainloop()
