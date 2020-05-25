try:
    import tkinter                  # python 3
except ImportError:
    import Tkinter as tkinter       # python 2

main_window = tkinter.Tk()

main_window.title("Hello World")
main_window.geometry('640x480+8+400')

label = tkinter.Label(main_window, text="Hello World!")
label.pack(side='top')

left_frame = tkinter.Frame(main_window)
left_frame.pack(side='left', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
canvas.pack(side='left', ancho='n')

right_frame = tkinter.Frame(main_window)
right_frame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

main_window.mainloop()
