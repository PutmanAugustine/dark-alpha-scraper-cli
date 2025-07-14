import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter import ttk

# Global variables declaration at module level
url_entry = None
file_entry = None
text_field = None

from .scraper import scrape

def make_rounded(widget, radius=10, bg='#333333', fg='#ffffff'):
    # Create a frame with rounded corners
    frame = Frame(widget.master, bg=bg, bd=0)
    
    # Place the original widget inside
    widget.pack(in_=frame, fill=BOTH, expand=True, padx=radius//2, pady=radius//2)
    
    # Draw rounded rectangle
    canvas = Canvas(frame, bg=frame['bg'], highlightthickness=0, bd=0)
    canvas.pack(fill=BOTH, expand=True)
    
    def update_rounding(event=None):
        canvas.delete("all")
        w, h = frame.winfo_width(), frame.winfo_height()
        canvas.create_rounded_rect(0, 0, w, h, radius=radius, fill=bg, outline='#555555')
    
    frame.bind("<Configure>", update_rounding)
    return frame

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def on_scrape():
    url = url_entry.get()
    file_path = file_entry.get()
    text = text_field.get().strip()
    
    if not url or not file_path or not text:
        messagebox.showerror("Error", "All fields must be filled out.")
        return
    
    scrape(url, file_path, text)

def open_new_window(root):
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(pady=20)



def start():
    global url_entry, file_entry, text_field
    
    # GUI Setup
    root = tk.Tk()
    root.title("Dark Alpha Capital Deal Scraper")
    root.geometry("800x600")  # Increased initial size
    root.minsize(600, 500)  # Minimum window size
    root.configure(bg="#1a1a1a")
    
    # Configure grid for root window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    # Main container
    main_frame = tk.Frame(root, bg="#1a1a1a", padx=40, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Configure main frame grid
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)
    
    # Title
    title_frame = tk.Frame(main_frame, bg="#1a1a1a")
    title_frame.pack(fill=tk.X, pady=(0, 30))
    
    tk.Label(
        title_frame,
        text="Welcome to the Dark Alpha Capital Webscraper",
        font=("Arial", 32, "bold"),  # Slightly smaller font for better responsiveness
        fg="#ffffff",
        bg="#1a1a1a",
        wraplength=700  # Allows text to wrap on smaller windows
    ).pack(fill=tk.X)
    
    # Form container
    form_frame = tk.Frame(main_frame, bg="#1a1a1a")
    form_frame.pack(fill=tk.BOTH, expand=True)
    
    # URL Entry
    url_frame = tk.Frame(form_frame, bg="#1a1a1a")
    url_frame.pack(fill=tk.X, pady=(0, 20), expand=True)
    
    tk.Label(
        url_frame,
        text="Enter URL:",
        font=("Arial", 10),
        fg="#aaaaaa",
        bg="#1a1a1a",
        anchor="w"
    ).pack(fill=tk.X, pady=(0, 5))
    
    url_entry = tk.Entry(
        url_frame,
        font=("Arial", 10),
        fg="#ffffff",
        bg="#333333",
        insertbackground="#ffffff",
        relief=tk.FLAT
    )
    url_entry.pack(fill=tk.X, ipady=5)
    
    # File Selection
    file_frame = tk.Frame(form_frame, bg="#1a1a1a")
    file_frame.pack(fill=tk.X, pady=(0, 20), expand=True)
    
    tk.Label(
        file_frame,
        text="Select File (leave blank to default to your desktop):",
        font=("Arial", 10),
        fg="#aaaaaa",
        bg="#1a1a1a",
        anchor="w"
    ).pack(fill=tk.X, pady=(0, 5))
    
    file_entry_frame = tk.Frame(file_frame, bg="#1a1a1a")
    file_entry_frame.pack(fill=tk.X)
    
    file_entry = tk.Entry(
        file_entry_frame,
        font=("Arial", 10),
        fg="#ffffff",
        bg="#333333",
        insertbackground="#ffffff",
        relief=tk.FLAT
    )
    file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
    
    browse_button = tk.Button(
        file_entry_frame,
        text="Browse",
        command=browse_file,
        font=("Arial", 10),
        fg="#ffffff",
        bg="#4a4a4a",
        activeforeground="#ffffff",
        activebackground="#555555",
        relief=tk.FLAT,
        padx=15
    )
    browse_button.pack(side=tk.RIGHT, padx=(10, 0))
    
    # Name of firm
    firm_frame = tk.Frame(form_frame, bg="#1a1a1a")
    firm_frame.pack(fill=tk.X, pady=(0, 30), expand=True)
    
    tk.Label(
        firm_frame,
        text="Enter Name of Firm:",
        font=("Arial", 10),
        fg="#aaaaaa",
        bg="#1a1a1a",
        anchor="w"
    ).pack(fill=tk.X, pady=(0, 5))
    
    text_field = tk.Entry(
        firm_frame,
        font=("Arial", 10),
        fg="#ffffff",
        bg="#333333",
        insertbackground="#ffffff",
        relief=tk.FLAT
    )
    text_field.pack(fill=tk.X, ipady=5)
    
    # Button container
    button_frame = tk.Frame(form_frame, bg="#1a1a1a")
    button_frame.pack(fill=tk.X, pady=(20, 0))
    
    scrape_button = tk.Button(
        button_frame,
        text="Scrape",
        command=on_scrape,
        font=("Arial", 12, "bold"),
        fg="#ffffff",
        bg="#0066cc",
        activeforeground="#ffffff",
        activebackground="#0077dd",
        relief=tk.FLAT,
        padx=20,
        pady=10
    )
    scrape_button.pack(pady=(10, 0))
    
    # Make all entry widgets expand with window
    for entry in [url_entry, file_entry, text_field]:
        entry.bind("<Configure>", lambda e: e.widget.configure(width=e.widget.winfo_width()//10))

    # Add a button to open a new window
    # Button to open a new window
    open_button = tk.Button(main_frame, text="Open New Window", command=lambda: open_new_window(root))
    open_button.pack(pady=50)

    
    print(tk.TkVersion)
    print(tk.TclVersion)
        
    root.mainloop()

if __name__ == "__main__":
    start()


# def start():
#     global url_entry, file_entry, text_field
    
#     # GUI Setup
#     root = tk.Tk()
#     root.title("Dark Alpha Capital Deal Scraper")
#     root.geometry("500x400")

#     # Title
#     tk.Label(root, text="Welcome to the Dark Alpha Capital Webscraper.").pack(pady=(10,0))

#     # URL Entry
#     tk.Label(root, text="Enter URL:").pack(pady=(10, 0))
#     url_entry = tk.Entry(root, width=60)
#     url_entry.pack(pady=(0, 10))

#     # File Selection
#     tk.Label(root, text="Select File (leave blank to default to your desktop):").pack()
#     file_frame = tk.Frame(root)
#     file_frame.pack(pady=(0, 10))
#     file_entry = tk.Entry(file_frame, width=45)
#     file_entry.pack(side=tk.LEFT, padx=(0, 5))
#     browse_button = tk.Button(file_frame, text="Browse", command=browse_file)
#     browse_button.pack(side=tk.LEFT)

#     # Name of firm
#     tk.Label(root, text="Enter Name of Firm:").pack()
#     text_field = tk.Entry(root, width=60)
#     text_field.pack(pady=(0, 10))

#     # Scrape Button
#     scrape_button = tk.Button(root, text="Scrape", command=on_scrape, bg="blue", fg="white")
#     scrape_button.pack(pady=(10, 20))

#     root.mainloop()