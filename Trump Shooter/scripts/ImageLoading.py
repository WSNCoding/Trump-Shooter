import tkinter
def hideBG():
    global state
    if state == "Hidden":
        background_label.pack()
        state = "Showing"

    elif state == "Showing":
        background_label.pack_forget()
        state = "Hidden"




window = tkinter.Tk()

background_image=tkinter.PhotoImage(file="Example.png")
background_label = tkinter.Label(window, image=background_image)

hideBttn = tkinter.Button(window, text="Hide Background", command=hideBG)
state = "Showing"

hideBttn.pack()
background_label.pack()

window.mainloop()
