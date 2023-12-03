# final_assignment
import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Note Taking App")



#found out how to display warning message
def add_note():
    note_text = note_entry.get("1.0", tk.END).strip()
    if note_text:
        note_listbox.insert(tk.END, note_text)
        note_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a note.")



def remove_note():
    selected_index = note_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("warning", "Please select a note to remove.")
    else:
        note_listbox.delete(selected_index)


note_entry = tk.Text(window, height=5, width=30)
note_entry.pack(pady=10)

add_button = tk.Button(window, text="Add Note", command=add_note)
add_button.pack(pady=5)

note_listbox = tk.Listbox(window, height=10, selectmode=tk.SINGLE)
note_listbox.pack(pady=10)

remove_button = tk.Button(window, text="Remove Note", command=remove_note)
remove_button.pack(pady=5)

window.mainloop()

