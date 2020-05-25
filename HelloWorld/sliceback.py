letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1]
print(backwards)

backwards = letters[25:-27:-1]
print(backwards)

backwards = letters[-1:-27:-1]
print(backwards)

backwards = letters[16:13:-1] # qpo
print(backwards)

backwards = letters[4::-1] # edcba
print(backwards)

backwards = letters[25:17:-1] # last 8 chars, in reverse order
print(backwards)

backwards = letters[:-9:-1] # last 8 chars, in reverse order
print(backwards)

w = ""
print(w[:1]) # does NOT throw an error if the array is empty
