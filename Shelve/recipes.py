import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipes") as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # recipes["blt"].append("butter")     # Does NOT work
    # recipes["pasta"].append("tomato")   # Does NOT work
    #
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])

print("=" * 50)

# Less code, BUT heavy memory usage
with shelve.open("recipes", writeback=True) as recipes:
    # recipes["soup"].append("croutons")    # NOW IT WORKS!!! It requires opening the file with writeback=True

    for snack in recipes:
        print(snack, recipes[snack])
