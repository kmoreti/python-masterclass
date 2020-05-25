# jabber = open("/home/kmoreti/IdeaProjects/python-masterclass/sample.txt", 'r')
jabber = open("sample.txt", 'r')
for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()
print("=" * 50)

# Pythonic way
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')
print("=" * 50)

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

print("=" * 50)

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
for line in lines:
    print(line, end='')

print("=" * 50)

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
for line in lines[::-1]:
    print(line, end='')

print("=" * 50)

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()
for line in lines[::-1]:
    print(line, end='')