import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from .scraper import scrape

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def on_scrape():
    url = url_entry.get()
    file_path = file_entry.get()
    text = text_field.get("1.0", tk.END).strip()
    if not url or not file_path or not text:
        messagebox.showerror("Error", "All fields must be filled out.")
        return
    scrape(url, file_path, text)

def start():
    # GUI Setup
    root = tk.Tk()
    root.title("Dark Alpha Capital Deal Scraper")
    root.geometry("500x400")

    # Title
    tk.Label(root, text="Welcome to the Dark Alpha Capital Webscraper.").pack(pady=(10,0))

    # URL Entry
    tk.Label(root, text="Enter URL:").pack(pady=(10, 0))
    url_entry = tk.Entry(root, width=60)
    url_entry.pack(pady=(0, 10))

    # File Selection
    tk.Label(root, text="Select File (leave blank to default to your desktop):").pack()
    file_frame = tk.Frame(root)
    file_frame.pack(pady=(0, 10))
    file_entry = tk.Entry(file_frame, width=45)
    file_entry.pack(side=tk.LEFT, padx=(0, 5))
    browse_button = tk.Button(file_frame, text="Browse", command=browse_file)
    browse_button.pack(side=tk.LEFT)

    # Name of firm
    tk.Label(root, text="Enter Name of Firm:").pack()
    text_field = tk.Entry(root, height=0, width=60)
    text_field.pack(pady=(0, 10))

    # Scrape Button
    scrape_button = tk.Button(root, text="Scrape", command=on_scrape, bg="blue", fg="white")
    scrape_button.pack(pady=(10, 20))

    root.mainloop()
