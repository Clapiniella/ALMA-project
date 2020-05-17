from tkinter import *
from PIL import ImageTk
import PIL.Image
import src.video as vi
import src.webcam as we
from tkinter import filedialog
import src.report as re 

HEIGHT = 1000
WIDTH = 1000
window = Tk()
window.title("ALMA share")
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()
icon = PIL.Image.open("./images/icon.png")

# background
image = PIL.Image.open("./images/second.jpg")
background_image = ImageTk.PhotoImage(image)
background_label = Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# title
label = Label(window, text="ALMA",bg='#94b1ee',fg="black", width=200, font='Escalope 65 bold')
label.place(relx=0.5, rely=0.13, relwidth=1, relheight=0.15, anchor='n')
#label.config(font=("bold", 50))

# facial emotion recognition
label = Label(window, text="facial emotion recognition", fg="black",
                bg='#ffda00', width=200, font="Comfortaa 14 bold")
label.place(relx=0.5, rely=0.23, relwidth=0.3, relheight=0.04, anchor='n')

# choose
label = Label(window, text="Choose your own path", fg="black",
                bg='#94b1ee', width=200, font="Comfortaa 14 bold")
label.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.05, anchor='n')

# button - webcam
frame = Frame(window, bg='#94b1ee', bd=5)
frame.place(relx=0.3125, rely=0.45, relwidth=0.375,
            relheight=0.1, anchor='n')


button = Button(frame, cursor="heart", text="Webcam", font="Comfortaa 18 bold",command=lambda: we.webcam(counttoclose=0, idvideo=67))
button.place(relx=0, relheight=1, relwidth=1)
button.configure(foreground='black', relief='groove')


# button - video
frame = Frame(window, bg='#94b1ee', bd=5)
frame.place(relx=0.6875, rely=0.45, relwidth=0.375,
            relheight=0.1, anchor='n')

button = Button(frame, cursor="heart", text="Video", font="Comfortaa 18 bold", command=lambda: vi.video(idvideo=69))
button.place(relx=0, relheight=1, relwidth=1)
button.configure(foreground='black', relief='groove')

# separator
label = Label(window, bg='black', width=200)
label.place(relx=0.5, rely=0.5525, relwidth=0.75, relheight=0.005, anchor='n')

#thank you
label = Label(window, text="Thank you for using our services", fg="black",
                bg='#94b1ee', width=200, font="Comfortaa 12 bold")
label.place(relx=0.5, rely=0.56, relwidth=0.75, relheight=0.05, anchor='n')

label = Label(window, text="If you would like to get a report of what you've just seen, press the button below", fg="black",
                bg='#94b1ee', width=200, font="Comfortaa 10 bold")
label.place(relx=0.5, rely=0.60, relwidth=0.75, relheight=0.05, anchor='n')

# button - report
frame = Frame(window, bg='#94b1ee', bd=5)
frame.place(relx=0.5, rely=0.65, relwidth=0.75,
            relheight=0.1, anchor='n')


button = Button(frame, cursor="heart", text="Get your report", font="Comfortaa 18 bold",command=lambda: re.getReport(idvideo=69))
button.place(relx=0, relheight=1, relwidth=1)
button.configure(foreground='black', relief='groove')

window.mainloop()