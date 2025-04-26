names = ("sara","amir","negin","bita")
print(f"orginal names: {names}")
print(f"the second name is {names[1]}")
print(f"the count of names is {len(names)}")
sara_is_or_not = "sara" in names
if sara_is_or_not:
    print("sara is in the tuple")
else:
    print("sara is not in the tuple")