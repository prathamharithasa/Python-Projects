import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

SAVE_FILE = "sticky_notes_data.json"
DARK_MODE = False
current_note_id = None
notes = {}

# -----------------------------
# Save and Load Note Functions
# -----------------------------
def save_note():
    global current_note_id
    if current_note_id is None:
        messagebox.showwarning("No Note", "Please create or select a note first")
        return
    
    notes[current_note_id] = {
        "text": text_box.get("1.0", tk.END),
        "geometry": root.geometry(),
        "timestamp": datetime.now().isoformat(),
        "bg_color": text_box.cget("bg"),
        "fg_color": text_box.cget("fg"),
        "font_size": current_font_size[0]
    }
    save_all_notes()
    update_timestamp_label()
    update_word_count()

def save_all_notes():
    with open(SAVE_FILE, "w") as f:
        json.dump(notes, f)

def load_all_notes():
    global notes
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            notes = json.load(f)
    refresh_note_list()

def load_note(note_id):
    global current_note_id
    current_note_id = note_id
    text_box.delete("1.0", tk.END)
    
    if note_id in notes:
        data = notes[note_id]
        text_box.insert("1.0", data.get("text", ""))
        root.geometry(data.get("geometry", "350x400"))
        text_box.config(bg=data.get("bg_color", "#ffffff"), fg=data.get("fg_color", "#000000"))
        font_size = data.get("font_size", 11)
        change_font_size(font_size)
    
    update_timestamp_label()
    update_word_count()
    root.title(f"Sticky Note - {note_id}")

def create_new_note():
    note_name = tk.simpledialog.askstring("New Note", "Enter a name for the new note:")
    if note_name:
        if note_name in notes:
            messagebox.showwarning("Exists", "A note with this name already exists!")
            return
        
        notes[note_name] = {
            "text": "",
            "geometry": "350x400",
            "timestamp": datetime.now().isoformat(),
            "bg_color": "#ffffff",
            "fg_color": "#000000",
            "font_size": 11
        }
        save_all_notes()
        load_note(note_name)
        refresh_note_list()
        messagebox.showinfo("Success", f"Note '{note_name}' created!")

def refresh_note_list():
    note_list_menu.delete(0, tk.END)
    for note_name in sorted(notes.keys()):
        note_list_menu.add_command(label=note_name, command=lambda n=note_name: load_note(n))

def delete_current_note():
    global current_note_id
    if current_note_id is None:
        messagebox.showwarning("No Note", "Please select a note first")
        return
    
    if messagebox.askyesno("Delete", f"Delete note '{current_note_id}'?"):
        del notes[current_note_id]
        save_all_notes()
        text_box.delete("1.0", tk.END)
        current_note_id = None
        root.title("📝 Sticky Note")
        refresh_note_list()
        messagebox.showinfo("Deleted", "Note deleted successfully!")

def update_timestamp_label():
    if current_note_id and current_note_id in notes:
        timestamp = notes[current_note_id].get("timestamp", "")
        if timestamp:
            dt = datetime.fromisoformat(timestamp)
            timestamp_label.config(text=f"Last saved: {dt.strftime('%m/%d %H:%M')}")

# Word Count Function
def update_word_count():
    text = text_box.get("1.0", tk.END).strip()
    char_count = len(text)
    word_count = len(text.split()) if text else 0
    word_count_label.config(text=f"Words: {word_count} | Chars: {char_count}")

# UI Functions
def change_color(color):
    text_box.config(bg=color)
    root.config(bg=color)
    timestamp_label.config(bg=color)
    word_count_label.config(bg=color)

def change_text_color(color):
    text_box.config(fg=color)

current_font_size = [10]  # Using list to allow modification in nested functions

def change_font_size(size):
    current_font_size[0] = size
    text_box.config(font=("Comic Sans MS", size))

def toggle_dark_mode():
    global DARK_MODE
    DARK_MODE = not DARK_MODE
    if DARK_MODE:
        root.config(bg="#2d2d2d")
        text_box.config(bg="#1e1e1e", fg="#e0e0e0")
        timestamp_label.config(bg="#2d2d2d", fg="#b0b0b0")
        word_count_label.config(bg="#2d2d2d", fg="#b0b0b0")
    else:
        root.config(bg="#fffacd")
        text_box.config(bg="#ffffff", fg="#000000")
        timestamp_label.config(bg="#fffacd", fg="#666666")
        word_count_label.config(bg="#fffacd", fg="#666666")

def toggle_bold():
    try:
        current_tags = text_box.tag_names("sel.first")
        if "bold" in current_tags:
            text_box.tag_remove("bold", "sel.first", "sel.last")
        else:
            text_box.tag_add("bold", "sel.first", "sel.last")
    except tk.TclError:
        messagebox.showwarning("No Selection", "Please select text to make it bold")

def clear_note():
    if messagebox.askyesno("Clear Note", "Are you sure you want to clear all text?"):
        text_box.delete("1.0", tk.END)
        update_word_count()

def on_closing():
    if messagebox.askyesno("Save Note", "Save before closing?"):
        save_note()
    root.quit()

# Import for dialog
from tkinter import simpledialog

# Main App Window
root = tk.Tk()
root.title("📝 Sticky Notes")
root.config(bg="#d6f0ff")
root.geometry("500x500")

root.attributes('-alpha', 0.95)

# Text area
text_box = tk.Text(root, bg="#ffffff", font=("Comic Sans MS", 10), wrap=tk.WORD, bd=0)
text_box.pack(expand=True, fill="both", padx=5, pady=5)

text_box.tag_configure("bold", font=("Comic Sans MS", 10, "bold"))
text_box.bind("<KeyRelease>", lambda e: update_word_count())

# Word count label
word_count_label = tk.Label(root, text="Words: 0 | Chars: 0", font=("Comic Sans MS", 8), fg="#666666", bg="#d6f0ff")
word_count_label.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=1)

# Timestamp label
timestamp_label = tk.Label(root, text="", font=("Comic Sans MS", 8), fg="#666666", bg="#d6f0ff")
timestamp_label.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=2)

# Menu
menu = tk.Menu(root)

# Color Menu
color_menu = tk.Menu(menu, tearoff=0)
color_menu.add_command(label="White", command=lambda: change_color("#ffffff"))
color_menu.add_command(label="Blue", command=lambda: change_color("#d6f0ff"))
color_menu.add_command(label="Red", command=lambda: change_color("#ffcccc"))
color_menu.add_command(label="Green", command=lambda: change_color("#ccffcc"))
color_menu.add_command(label="Yellow", command=lambda: change_color("#fffacd"))
color_menu.add_command(label="Pink", command=lambda: change_color("#ffd1dc"))

# Text Color Menu
text_color_menu = tk.Menu(menu, tearoff=0)
text_color_menu.add_command(label="White", command=lambda: change_text_color("#ffffff"))
text_color_menu.add_command(label="Black", command=lambda: change_text_color("#000000"))
text_color_menu.add_command(label="Blue", command=lambda: change_text_color("#0000ff"))
text_color_menu.add_command(label="Red", command=lambda: change_text_color("#ff0000"))
text_color_menu.add_command(label="Green", command=lambda: change_text_color("#008000"))
text_color_menu.add_command(label="Purple", command=lambda: change_text_color("#800080"))

# Font Size Menu
font_menu = tk.Menu(menu, tearoff=0)
font_menu.add_command(label="Small (10)", command=lambda: change_font_size(10))
font_menu.add_command(label="Medium (12)", command=lambda: change_font_size(12))
font_menu.add_command(label="Large (14)", command=lambda: change_font_size(14))
font_menu.add_command(label="Extra Large (16)", command=lambda: change_font_size(16))

# Note Menu
note_menu = tk.Menu(menu, tearoff=0)
note_menu.add_command(label="Create New Note", command=create_new_note)
note_menu.add_separator()
note_list_menu = tk.Menu(note_menu, tearoff=0)
note_menu.add_cascade(label="Open Note", menu=note_list_menu)
note_menu.add_command(label="Delete Current Note", command=delete_current_note)

menu.add_cascade(label="Notes", menu=note_menu)
menu.add_cascade(label="Background Color", menu=color_menu)
menu.add_cascade(label="Text Color", menu=text_color_menu)
menu.add_cascade(label="Font Size", menu=font_menu)
menu.add_command(label="Bold (Ctrl+B)", command=toggle_bold)
menu.add_separator()
menu.add_command(label="Save (Ctrl+S)", command=save_note)
menu.add_command(label="Clear", command=clear_note)
menu.add_command(label="Dark Mode", command=toggle_dark_mode)
menu.add_separator()
menu.add_command(label="Exit", command=on_closing)

root.config(menu=menu)

# Keyboard shortcuts
root.bind("<Control-s>", lambda e: save_note())
root.bind("<Control-b>", lambda e: toggle_bold())

# Load previous notes
load_all_notes()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
