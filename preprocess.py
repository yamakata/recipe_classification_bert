import json


with open('data/recipe_name_cat_469.json') as f:
    data = json.load(f)
labels = []
with open('data/FLD469_FoodList_new.csv', 'r', encoding='utf-8') as fi:
    for line in fi:
        labels.append(line.rstrip('\n').split(',')[1])
print(labels)
