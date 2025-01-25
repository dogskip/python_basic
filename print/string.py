instructions = [
    "Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.",
    "Knead the dough for 10 minutes.",
    "Add 3g of Salt.",
    "Leave to rise for 2 hours.",
    "Bake at 200 degrees C for 30 minutes."
]
numbered_instructions = [f"{i+1}. {text}" for i, text in enumerate(instructions)]
print('\n'.join(numbered_instructions))
