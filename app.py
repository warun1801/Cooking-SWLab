from flask import Flask, render_template, request

import requests
app = Flask(__name__, template_folder='template')

url = "https://api.edamam.com/"
nut_url = "https://api.edamam.com/api/food-database/v2/parser"
headers = {

}
# GET /recipes/mealplans/generate?timeFrame=day&targetCalories=2000&diet=vegetarian&exclude=shellfish%2C%20olives HTTP/1.1
# X-Rapidapi-Key: e83a081f21msh7b1bc6b3ccc6f18p1302c9jsnaab174d2dcce
# X-Rapidapi-Host: spoonacular-recipe-food-nutrition-v1.p.rapidapi.com
# Host: spoonacular-recipe-food-nutrition-v1.p.rapidapi.com

random_joke = "food/jokes/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"
desiredRecipe = "/search"


@app.route('/')
def search_page():
    #joke_response = str(requests.request("GET", url + random_joke, headers=headers).json()['text'])
    return render_template('base.html', joke="What do you call a fake noodle? Impasta!")


@app.route('/recipes')
def get_recipes():
    if (str(request.args['ingredients']).strip() != ""):
        # If there is a list of ingredients -> list
        querystring = {"q": request.args['ingredients'], 'app_id': '1a0f5fe3',
                       'app_key': "d2bffdbb1cf7ddda6c0c82df2f82b530", }
        response = requests.request(
            "GET", url + desiredRecipe, headers=headers, params=querystring).json()
        print(response)
        return render_template('recipes.html', recipes=response)
    else:
        # Random recipes
        querystring = {"number": "5"}
        response = requests.request(
            "GET", url + randomFind, headers=headers, params=querystring).json()
        print(response['hits'])
        return render_template('recipes.html', recipes=response['hits'])


@app.route('/nutrition')
def get_nutrition():
    if (str(request.args['ingredients']).strip() != ""):
        # If there is a list of ingredients -> list
        querystring = {"ingr": request.args['ingredients'], 'app_id': '701bf358',
                       'app_key': "5cc7fec22b0bbf174f6e5c086154a3ca", }
        response = requests.request(
            "GET", nut_url, headers=headers, params=querystring).json()
        return render_template('nutrition.html', nutrition=response)


if __name__ == '__main__':
    app.run(debug=True, port='5000', threaded=True)
