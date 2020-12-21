import os
import time

def solve_1(input):
    allergen_list = dict()
    all_ingredients = set()
    for food in input:
        f = food.replace("(","")
        f = f.replace(")","")
        ingredients, allergens = f.split(" contains ")
        ingredients_list = set(ingredients.split(" "))
        all_ingredients = all_ingredients.union(ingredients_list)
        for allergen in allergens.split(", "):
            if allergen not in allergen_list:
                allergen_list[allergen] = ingredients_list
            else:
                allergen_list[allergen] = allergen_list[allergen].intersection(ingredients_list)  
    
    ing_with_al = set()
    for al in allergen_list.values():
        ing_with_al = ing_with_al.union(al)
    
    in_without_al = all_ingredients - ing_with_al
    solution = 0
    for food in input:
        f = food.replace("(","")
        f = f.replace(")","")
        ingredients, allergens = f.split(" contains ")
        ingredients_list = set(ingredients.split(" "))
        for ing in ingredients_list:
            if ing in in_without_al:
                solution += 1
    print("part1", solution)

    replaced = True
    ings = set()
    ing_allergen = dict()
    while replaced:
        replaced = False
        for al,ing_l in allergen_list.items():
            if len(ing_l) == 1:
                ings.add(list(ing_l)[0])
                ing_allergen[al] = list(ing_l)[0]
                replaced = True

        for ing in ings:
            for ing_l in allergen_list.values():
                if ing in ing_l:
                    ing_l.remove(ing)
    
    dangerous_list = ""
    for al in sorted([key for key in ing_allergen.keys()]):
        dangerous_list += "," + ing_allergen[al]

    print(dangerous_list[1:])
    return None
   

def solve_2(input):
    pass

with open(os.path.dirname(__file__) + "/input", "r") as myInput:
    start_time = time.time()
    input = [line.strip() for line in myInput]
    print(solve_1(input))
    print(solve_2(input))
    print("--- Execution time %s s ---" % (time.time() - start_time))