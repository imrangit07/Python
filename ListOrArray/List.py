shoes = ['Nike', 'Adidas', 'Reebok', 'campus']

print(shoes[0:3]) # shows ['Nike', 'Adidas', 'Reebok']

shoes[1:2] = ["Zara"]
print(shoes)
shoes.append("Puma")
shoes[0]='adidas'

# if "Zara" in shoes: print("Yes")

shoes.pop()
shoes.insert(1,"kick")
shoes.remove('Zara')
print(shoes) 

shoes_copy = shoes.copy()
shoes.pop()
print(shoes)
print(shoes_copy)


squared_nums = [i**2 for i in range(1, 11)]
print(squared_nums)


