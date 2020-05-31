# It is annoying, but ingredients and instructions are not really in order
# Recognized it quite late..


import json
import re


class Recipes:

    def __init__(self, search_name='', search_ingredients=[]):

        # Opening and reading json file in
        with open('recipes.json') as f:

            self.recipe = json.load(f)

        # Defining them separately
        self._ingredients = []
        self._instructs = []
        self._names = []
        self._url = []

        for i in self.recipe:
            self._ingredients.append(i['Ingredients'])
            self._instructs.append(i['Instructions'])
            self._names.append(i['Name'])
            self._url.append(i['Url'])

        # Search terms are optional
        self.search_name = search_name
        self.search_ingredients = search_ingredients

    def foo(self):
        print(self.recipe)


    def find_rec(self):
        # We need index to get other belongings
        index = 0

        # If there are no search parameters -> error
        if self.search_name == '' and self.search_ingredients == []:
            print('\n[!] No terms given.\n')
            return

        for name in range(len(self._names)):
            if self._names[name] == self.search_name:
                index = name
        return index

    def __call__(self):

        idx = self.find_rec()
        print(idx)

        print(f'\nRezept für: {self._names[idx]}\n')
        print('\n Zutaten: ')

        for ings in self._ingredients[idx]:
            print(ings)

        print(f'\nAnweisungen: \n {self._instructs[idx]}\n')
        print(f'Find the recipe on: {self._url[idx]}\n')
