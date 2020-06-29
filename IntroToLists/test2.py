result = "Correct"
other_result = result

print(id(result))
print(id(other_result))
print(result)
print(other_result)

print("-" * 50)
result = result + "ish"
print(id(result))
print(id(other_result))
print(result)
print(other_result)

print("=" * 50)
shopping_list = ["pasta", "cookies"]
other_shopping_list = shopping_list
print(id(shopping_list))
print(id(other_shopping_list))
print(shopping_list)
print(other_shopping_list)
print("-" * 50)
shopping_list += ["eggs"]
print(id(shopping_list))
print(id(other_shopping_list))
print(shopping_list)
print(other_shopping_list)
