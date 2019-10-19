import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps =[]

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("Executables","*.exe"),("All Files","*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame,text=app,fg="#ffffff",bg="#3285a8", padx=10, pady=5,bd=2, relief="groove")
        label.pack()
def runApps():
    for app in apps:
        if app:
            os.startfile(app)

canvas = tk.Canvas(root, width=700, height=700, bg="#3285a8")
canvas.pack()

frame = tk.Frame(root, bg="#a83234")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="#ffffff", bg="#3285a8",bd=2, relief="groove",command=addApp)
openFile.place(rely=0.79,relx=0.45)
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="#ffffff", bg="#3285a8",bd=2, relief="groove",command=runApps)
runApps.place(rely=0.85,relx=0.45)

for app in apps:
    label = tk.Label(frame,text=app,fg="#ffffff",bg="#3285a8", padx=10, pady=5,bd=2, relief="groove")
    label.pack()


root.mainloop()
   
with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')
