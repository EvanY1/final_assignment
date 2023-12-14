import tkinter as tk
from tkinter import messagebox

window = tk.Tk() #first window in which the program shows 
window.title("Note Taking App")#name of application



'''
Add note function- 
The function starts by taking the text from the note_entry text box and storing it in the note_text variable.
The function then uses a conditional to make sure the user actually enters text into the text box. If the user enters any kind of text in any amount, 
the conditional will insert the entire note stored in 'note_text' to 'note_llistbox' and remove the text entered into the ntoe_entry box. If the user 
If you don't enter any text into the 'note_entry' text box the conditional will return a warning message. 
'''
def add_note():
    note_text = note_entry.get("1.0", tk.END).strip()#stores all of text entered in note entry, removes all empty space on the edges.
    if note_text:
        note_listbox.insert(tk.END, note_text)
        note_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a note.")



'''
Remove note function-
The function starts by storing the selection of an index within the 'note_listbox' inside of the selected_index variable. 
The function then tests if there is an actual note selected. If a note is selected when the remove button is activated, 
the selected message will be expunged. If there isn't a note selected the program will give an error message. 
'''
def remove_note():
    selected_index = note_listbox.curselection()#gives variable to reference for selected index within the note_listbox 
    if not selected_index:
        messagebox.showwarning("Warning", "Please select a note to remove.")
    else:
        note_listbox.delete(selected_index)


'''
Edit note function-
The edit function begins by storing the selected index within the variable 'selected_index'. I then use a conditional to make sure the user has 
selected an index within the note_listbox. If the user has not selected a note, the program will display a warning message to the user. If a note is 
selected, the program will open a new window with the selected message in a text box which can be edited to the user's liking. 
''' 
def edit_note():
    selected_index = note_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select a note to edit.")
    else:
        selected_text = note_listbox.get(selected_index)#stores the selected index inside the note_listbox 
        edit_window = tk.Toplevel(window)#the secondary window for editing a note entry
        edit_window.title("Edit Note")#name of the secondary window 

        edit_label = tk.Label(edit_window, text="Edit Notes")#label for the edit_entry box 
        edit_label.pack(pady=5)

        edit_entry = tk.Text(edit_window, height=25, width=50)#edit entry box that user will make changes in
        edit_entry.insert(tk.END, selected_text)
        edit_entry.pack(pady=10)
        '''
        nested update note function 
        This function is used to update the text in the note_listbox with any changes made in the 'edit note' window. It stores the text 
        from the 'edit_entry' text box in the variable 'updated_text'. It then uses a conditional to make sure the user makes an input. 
        If an input is made the function will delete what was initially in the selected index inside of the 'note_listbox' and insert 
        what is stored in the 'updated_text'. 
        '''
        def update_note():
            updated_text = edit_entry.get("1.0", tk.END).strip()#stores any edits made inside the 'edit_entry' text box in the 'updated_text' variable
            if updated_text:
                note_listbox.delete(selected_index)
                note_listbox.insert(selected_index, updated_text)
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "Please enter a note.")

        update_button = tk.Button(edit_window, text="Update Note", command=update_note)#button on secondary window which makes call to the 'update_note' function
        update_button.pack(pady=5)


#Labels/buttons used to format program and make calls to function within the code

input_label = tk.Label(window, text="Input Notes")#label for the text input box
input_label.pack(pady=5)

note_entry = tk.Text(window, height=5, width=30)#text entry box where the notes are initially written
note_entry.pack(pady=10)

add_button = tk.Button(window, text="Add Note", command=add_note)#add_button makes call to the add_note function when pressed in the program 
add_button.pack(pady=5)

saved_notes_label = tk.Label(window, text="Saved Notes:")#label for the note_listbox 
saved_notes_label.pack(pady=5, anchor='w')

note_listbox = tk.Listbox(window, height=10, width=50, selectmode=tk.SINGLE)#the list box that stores info from the note_entry and can select an index within the list_box 
note_listbox.pack(pady=10)

remove_button = tk.Button(window, text="Remove Note", command=remove_note)#button which makes a call to the remove_note function when pressed
remove_button.pack(pady=5)

edit_button = tk.Button(window, text="Edit Note", command=edit_note)#edit_bnutton, makes a call to the edit_note function when pressed 
edit_button.pack(pady=5)

window.mainloop()

