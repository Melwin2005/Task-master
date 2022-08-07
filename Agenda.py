import tkinter
import tkinter.messagebox
import pickle

melwin = tkinter.Tk()
melwin.title("Agenda by Melwin")

def add_target():
    target = entry_target.get()
    if target != "":
        listbox_target.insert(tkinter.END, target)
        entry_target.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a target.")

def delete_target():
    try:
        target_index = listbox_target.curselection()[0]
        listbox_target.delete(target_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a target.")

def load_target():
    try:
        target = pickle.load(open("target.dat", "rb"))
        listbox_target.delete(0, tkinter.END)
        for target in target:
            listbox_target.insert(tkinter.END, target)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find target.dat.")

def save_target():
    target = listbox_target.get(0, listbox_target.size())
    pickle.dump(target, open("target.dat", "wb"))

def add_emoji(text):
    entry_target.insert(0,text)

# Create GUI
frame_target = tkinter.Frame(melwin)
frame_target.pack()

listbox_target = tkinter.Listbox(frame_target, height=10, width=50)
listbox_target.pack(side=tkinter.LEFT)

scrollbar_target = tkinter.Scrollbar(frame_target)
scrollbar_target.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_target.config(yscrollcommand=scrollbar_target.set)
scrollbar_target.config(command=listbox_target.yview)

entry_target = tkinter.Entry(melwin, width=50)
entry_target.pack()

button_add_emoji= tkinter.Button(melwin, text="♡", width=48,command=lambda:add_emoji("♡"))
button_add_emoji.pack()

button_add_emoji = tkinter.Button(melwin, text="😊", width=48,command=lambda:add_emoji("😊"))
button_add_emoji.pack()

button_add_target = tkinter.Button(melwin, text="Add target", width=48, command=add_target)
button_add_target.pack()

button_delete_target = tkinter.Button(melwin, text="Delete target", width=48, command=delete_target)
button_delete_target.pack()

button_load_target = tkinter.Button(melwin, text="Load target", width=48, command=load_target)
button_load_target.pack()

button_save_target = tkinter.Button(melwin, text="Save target", width=48, command=save_target)
button_save_target.pack()

melwin.mainloop()
