try:
    import tkinter                  # python 3
except ImportError:
    import Tkinter as tkinter       # python 2

main_window = tkinter.Tk()

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

main_window_padding = 8
main_window.title("Calculator")
main_window.geometry('640x480-8-200')
main_window['padx'] = main_window_padding

result = tkinter.Entry(main_window)
result.grid(row=0, column=0, sticky='nsew')

key_pad = tkinter.Frame(main_window)
key_pad.grid(row=1, column=0, sticky='nsew')

row = 0
for key_row in keys:
    col = 0
    for key in key_row:
        tkinter.Button(key_pad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

main_window.update()
main_window.minsize(key_pad.winfo_width() + main_window_padding, result.winfo_height() + key_pad.winfo_height())
main_window.maxsize(key_pad.winfo_width() + main_window_padding, result.winfo_height() + key_pad.winfo_height())
main_window.mainloop()
