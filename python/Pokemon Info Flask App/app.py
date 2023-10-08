from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Function to get Pokémon names from the PokéAPI
def get_pokemon_names():
    url = "https://pokeapi.co/api/v2/pokemon?limit=2000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [pokemon['name'] for pokemon in data['results']]
    return []

# Function to get Pokémon data from the PokéAPI
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon_data = None
    pokemon_names = get_pokemon_names()

    if request.method == "POST":
        pokemon_name = request.form.get("pokemon_name").lower()
        if pokemon_name in pokemon_names:
            # Fetch Pokémon data from the PokéAPI
            pokemon_data = get_pokemon_data(pokemon_name)
        else:
            # Handle the case where the Pokémon name is not found
            pokemon_data = {"name": "Not Found"}

    return render_template("index.html", pokemon_data=pokemon_data, pokemon_names=pokemon_names)

if __name__ == "__main__":
    app.run(debug=True)
