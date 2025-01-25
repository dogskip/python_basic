instructions = [
    "Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.",
    "Knead the dough for 10 minutes.",
    "Add 3g of Salt.",
    "Leave to rise for 2 hours.",
    "Bake at 200 degrees C for 30 minutes."
]
numbered_instructions = [f"{i+1}. {text}" for i, text in enumerate(instructions)]
print('\n'.join(numbered_instructions))

# name = input("what is your name")
# print("hello " + name)
#print(len(input("Enter your name: ")))
# print("Hello"[0])
#print("123"+"345")
# print(123,456,789)
#print(123_456_789)
print(3*3+3/3-3)
print(type("d"))
print(type(123))
print(type(123.4))
print(type(True))
print(type(int("123")))
print(int("123")+int("345"))
print(type(6/3),6/3)
print(type(6//3),6//3)
print(type(4**3),4**3)

print(type(True**3),True**3)
print(type(False**3),False**3)

ddd = 12.34
print(round(ddd))
print(round(ddd,1))
print(round(ddd,2))

print(8/3)
print(round(8/3))
print(round(8/3,2))
print(8//3)
print(8%3)
