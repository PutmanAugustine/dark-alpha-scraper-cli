import tkinter as tk
from tkinter import filedialog, messagebox
from .scraper import scrape

# Global variables
url_entry = None
file_entry = None
text_field = None

# # from .scraper import scrape  # Uncomment and implement your scrape function
# def scrape(url, file_path, text):
#     print(f"Scraping URL: {url}, saving to: {file_path}, for firm: {text}")
#     messagebox.showinfo("Success", "Scraping started!")

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

    scrape(text, url, file_path)

def open_form_window(root):
    global url_entry, file_entry, text_field

    form_window = tk.Toplevel()
    form_window.title("Dark Alpha Capital Deal Scraper")
    screen_width = form_window.winfo_screenwidth()
    screen_height = form_window.winfo_screenheight()
    form_window.geometry(f"{screen_width}x{screen_height}+0+0")

    form_window.configure(bg="#F7FAFC")  # Light gray
    form_window.state('zoomed')

    def on_close():
        root.destroy()

    form_window.protocol("WM_DELETE_WINDOW", on_close)

    main_frame = tk.Frame(form_window, bg="#F7FAFC", padx=300, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(
        main_frame,
        text="Dark Alpha Capital Deal Scraper",
        font=("DejaVu Sans", 28, "bold"),
        fg="#2D3748",
        bg="#F7FAFC",
        wraplength=700
    ).pack(fill=tk.X, pady=(0, 30))

    form_frame = tk.Frame(main_frame, bg="#F7FAFC")
    form_frame.pack(fill=tk.BOTH, expand=True)

    # URL Entry
    url_frame = tk.Frame(form_frame, bg="#F7FAFC")
    url_frame.pack(fill=tk.X, pady=(0, 20), expand=True)

    tk.Label(
        url_frame,
        text="Enter URL:",
        font=("DejaVu Sans", 10),
        fg="#718096",
        bg="#F7FAFC",
        anchor="w"
    ).pack(fill=tk.X, pady=(0, 5))

    url_entry = tk.Entry(
        url_frame,
        font=("DejaVu Sans", 10),
        fg="#2D3748",
        bg="#FFFFFF",
        insertbackground="#2D3748",
        relief=tk.FLAT,
        highlightthickness=1,             # border width
        highlightbackground="#000000",   # border color (normal)
        highlightcolor="#000000"         # border color (focus)
    )
    url_entry.pack(fill=tk.X, ipady=5)

    # File Selection
    file_frame = tk.Frame(form_frame, bg="#F7FAFC")
    file_frame.pack(fill=tk.X, pady=(0, 20), expand=True)

    tk.Label(
        file_frame,
        text="Select File (leave blank to save it to your desktop by default):",
        font=("DejaVu Sans", 10),
        fg="#718096",
        bg="#F7FAFC",
        anchor="w"
    ).pack(fill=tk.X, pady=(0, 5))

    file_entry_frame = tk.Frame(file_frame, bg="#F7FAFC")
    file_entry_frame.pack(fill=tk.X)

    file_entry = tk.Entry(
        file_entry_frame,
        font=("DejaVu Sans", 10),
        fg="#2D3748",
        bg="#FFFFFF",
        insertbackground="#2D3748",
        relief=tk.FLAT,highlightthickness=1,             # border width
        highlightbackground="#000000",   # border color (normal)
        highlightcolor="#000000"         # border color (focus)
    )
    file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)

    browse_button = tk.Button(
        file_entry_frame,
        text="Browse",
        command=browse_file,
        font=("DejaVu Sans", 10),
        fg="#FFFFFF",
        bg="#1A202C",
        activeforeground="#FFFFFF",
        activebackground="#2D3748",
        relief=tk.FLAT,
        padx=15
    )
    browse_button.pack(side=tk.RIGHT, padx=(10, 0))

    # Firm Name
    firm_frame = tk.Frame(form_frame, bg="#F7FAFC")
    firm_frame.pack(fill=tk.X, pady=(0, 30), expand=True)

    tk.Label(
        firm_frame,
        text="Enter Name of Firm:",
        font=("DejaVu Sans", 10),
        fg="#718096",
        bg="#F7FAFC",
        anchor="w"
    ).pack(fill=tk.X, pady=(0, 5))

    text_field = tk.Entry(
        firm_frame,
        font=("DejaVu Sans", 10),
        fg="#2D3748",
        bg="#FFFFFF",
        insertbackground="#2D3748",
        relief=tk.FLAT,
        highlightthickness=1,             # border width
        highlightbackground="#000000",   # border color (normal)
        highlightcolor="#000000"         # border color (focus)
    )
    text_field.pack(fill=tk.X, ipady=5)

    # Scrape Button
    button_frame = tk.Frame(form_frame, bg="#F7FAFC")
    button_frame.pack(fill=tk.X, pady=(20, 0))

    scrape_button = tk.Button(
        button_frame,
        text="Start Scraping!",
        command=on_scrape,
        font=("DejaVu Sans", 12, "bold"),
        fg="#FFFFFF",
        bg="#1A202C",
        activeforeground="#FFFFFF",
        activebackground="#2D3748",
        relief=tk.FLAT,
        padx=20,
        pady=10
    )
    scrape_button.pack(pady=(10, 0))


def start():
    root = tk.Tk()
    root.title("Dark Alpha Capital Webscraper")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.configure(bg="#F7FAFC")
    root.state('zoomed')

    title_label = tk.Label(
        root,
        text="Welcome to the Dark Alpha Capital Webscraper",
        font=("DejaVu Sans", 32, "bold"),
        fg="#2D3748",
        bg="#F7FAFC",
        wraplength=700
    )
    title_label.pack(padx=20, pady=(80, 10))
    
    text_label = tk.Label(
        root,
        text="Streamline your deal flow with our scraping tool",
        font=("DejaVu Sans", 20, "bold"),
        fg="#718096",
        bg="#F7FAFC"
    )
    text_label.pack(pady=(5, 20))

    text_label2 = tk.Label(
        root,
        text="Use this tool to scrape information from websites — just enter the URL, specify where to save the scraped data, and you’re all set!",
        font=("DejaVu Sans", 14),
        fg="#2D3748",
        bg="#F7FAFC",
        wraplength=700,
        justify="center"
    )
    text_label2.pack(pady=(20, 30))

    continue_button = tk.Button(
        root,
        text="Explore Raw Deals",
        command=lambda: [open_form_window(root), root.withdraw()],
        font=("DejaVu Sans", 14, "bold"),
        fg="#FFFFFF",
        bg="#1A202C",
        activeforeground="#FFFFFF",
        activebackground="#2D3748",
        padx=20,
        pady=14
    )
    continue_button.pack()

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
