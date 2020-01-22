from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def bot():
    url = 'https://thecocktaildb.com/api/json/v1/1/random.php'
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        recipe = data["drinks"]
        name = item['strDrink'] for item in recipe
    else:
        name = "I could not retrieve your recipe"
    return str(name)

if __name__ == "__main__":
    app.run()