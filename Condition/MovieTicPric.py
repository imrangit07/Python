

age = int(input("Enter your age: "))
day="Wednesday"

price=12 if age>=18 else 8

if day == "Wednesday":
    price=price-2
print(f"Ticket Price For You: {price}$")
