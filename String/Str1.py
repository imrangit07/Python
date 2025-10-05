# name = 'Imran Hussain'
# first_char = name[0]
# first_name = name[0:6]
# print(name)
# print(first_char)
# print(first_name)


# num ="0123456789"
# print(num[:]) # 0123456789
# print(num[0:]) # 0123456789
# print(num[:8]) # 01234567
# print(num[1:7]) # 123456
# print(num[0:9:2]) # 02468


# name = "        Imran Hussain"
# print(name.lower())
# print(name.upper())
# print(name.strip())
# print(name.replace("Imran", "Arman").strip())


# str = "imran, arman, jay, rocky"
# print(str.split(", "))
# print(str.find("jay"))  # if not found retrun -1
# print(str.count('a'))

# shoes = "Nike" 
# order = "I ordered {} shoes "
# print(order)
# print(order.format(shoes))
# order2 = f"I order {shoes} shoes " # Python 3.6+ only, not supported in Python 2.7 and below versions of the language.
# print(order2)


shoes = ['Nike', 'Adidas', 'Vans', 'Converse']
print(", ".join(shoes))

shoes1 = 'Adidas'

for p in shoes1:
    print(p)

path = r"c:\\user\imran" # r is used to indicate that the string literal contains raw strings.
print(path)
print("user" in path)