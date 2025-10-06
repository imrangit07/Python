

# dic = {
#     "name":"imran",
#     "age":23,
#     "contact":"9090909090",
#     "address":{ "city":"bhopal","state":"MP"},
#     "corses":[ "python programming language", "java programming language"]
# }
# squared_num = {x:x**2 for x in range(5)}
# dic_copy = dic.copy();
# print(squared_num)
# # squared_num.clear()

# dic["email"]="imran@gmail.com"
# dic.pop('age')
# del dic["contact"]



# print(dic_copy["address"]["city"])

# # for obj in dic:
# #      print(f"{obj} : {dic[obj]}")


# for key, values in dic.items():
#      print(f"{key} : {values}")

# if "name" in dic:
#      print("Name is present", dic["name"])


keys = ["key1","key2","key3"];

default_value = "default value";

# new_dict = { key : default_value for key in keys}
# print(new_dict)

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
