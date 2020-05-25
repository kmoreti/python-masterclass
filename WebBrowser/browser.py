import webbrowser

webbrowser.open("https://www.python.org", new=1)

help(webbrowser)

firefox = webbrowser.get(using="firefox")
firefox.open_new("https://www.python.org")