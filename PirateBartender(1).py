import random
import sys 

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin",],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon",],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel",],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola",],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top",]
}

def customer_preferences():
    preferences = {}
    for type, question in questions.items():
        print(question)
        preferences[type] = input().lower() in ["y", "yes"]
    return preferences

def make_order(preferences):
    order = []
    for ingredient_type, liked in preferences.items():
        if not liked:
            continue
        order.append(random.choice(ingredients[ingredient_type]))
    return order


def main():
    preferences = customer_preferences()
    order = make_order(preferences)
    print("Here is your order:")
    for ingredient in order:
        print("A {}".format(ingredient))
        
if __name__ == "__main__":
    main()