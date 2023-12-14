names = ["Vincent","debbie","Joe"]
name_caps = [n.capitalize() if n.islower() else "Relax " + n.capitalize() for n in names]
print(name_caps)

my_string = "hii442nm233ag2"

new_string = ["d" if i == "4" else "e" if i == "2" else "S" if i == "3" else i for i in my_string ]

print(new_string)

fruits = ["apples","bananas","straberries"]
[print(fruit) for fruit in fruits]

bits = [True,False,False,True,False]
new_bits = [1 if bit == True else 0 for bit in bits]
print(new_bits)

my_name = "HelloMyNameIsVincent"
new_name = "".join([i if i.islower() else " " + i for i in my_name])
print(new_name)