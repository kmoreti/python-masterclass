import os


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        _files = os.listdir(d)
        for f in _files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print(s)
        dir_list(s)
    else:
        print(s + " does not exist")


listing = os.walk('.')
# listing = os.walk('/home/kmoreti/IdeaProjects/python-masterclass/ScopeAndNamespace')

for root, directories, files in listing:
    print(root)
    for directory in directories:
        print("\t", directory)
    for file in files:
        print("\t", file)

print("*" * 50)
list_directories('.')

