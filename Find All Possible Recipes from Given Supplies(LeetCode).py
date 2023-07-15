class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = set()
        supplies = set(supplies)
        product_to_recipes = dict(zip(recipes, ingredients))
        while True:
            new_supplies = False
            for recipe in set(product_to_recipes).difference(res):
                if recipe not in supplies and set(product_to_recipes[recipe]).issubset(supplies):
                    new_supplies = True
                    supplies.add(recipe)
                    res.add(recipe)
            if not new_supplies:
                    return res
        return res
