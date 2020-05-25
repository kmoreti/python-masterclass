try:
    import tkinter                  # python 3
except ImportError:
    import Tkinter as tkinter       # python 2

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')
mainWindow.mainloop()
