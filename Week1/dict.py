my_dict = {
    "key": "value",
    "key2": "2nd_value",
    "key3": "3rd_value",
}
print(my_dict)


# How to acess to my dict

for key,value in my_dict.items():
    print(key, value)


# Let's talk about lists

my_list = [1, 2, 3, 4]
for new_values in range(5,10):
    my_list.append(new_values)
    print(my_list)

# Storing data Data structures & Algorithms example

paths = {
    "Home": ["Store A", "Store B", "Intersection"],
    "Store A": ["Home", "Store B"],
    "Store B": ["School"],
    "Intersection": ["School"],
}
print(paths)

list_paths = [["Home", "Store A"], ["Store A", "Home"], ["Home", "Store B"]]

for key, value in paths.items():
    print(key, value)


