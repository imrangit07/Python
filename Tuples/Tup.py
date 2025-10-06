# List is mutable, mutable means it can be changed
# tuple is immutable, immutable means it cannot be changed
my_list = [1,2,3,5]
my_tuple = (1,2,3,5) 
my_tuple1 = (5,10,20,40) 

all_tuple = my_tuple + my_tuple1;

my_list[3]=4 
# my_tuple[3]=4  TypeError: 'tuple' object does not support item assignment

print(my_list[3])
print(my_tuple[3])

print(all_tuple)

if 30 in all_tuple : 
    print("yes")
else: print("no")

print(all_tuple.count(5))

print(type(all_tuple))
    

