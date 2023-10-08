# Pokémon Information Web App

This web application allows users to search for information about Pokémon, including their name, image, type, height, weight, and abilities. It uses data from the [PokéAPI](https://pokeapi.co/) to provide accurate and up-to-date information about Pokémon.

<img width=1000 src=screenshot.png>

## Features

1. **Pokémon Search**: Enter the name of a Pokémon in the search box and press the "Search" button to fetch and display information about that Pokémon.

2. **Autocomplete Suggestions**: As you type in the search box, the application provides autocomplete suggestions for Pokémon names to make searching easier.

3. **Detailed Pokémon Information**: The application displays detailed information about the Pokémon, including its name, image, type, height, weight, and abilities.

4. **No Image Handling**: In case a Pokémon does not have an available image, the application gracefully handles it by displaying a message.

## Technologies Used

- **Flask**: A Python web framework used for the server-side logic and routing.

- **HTML/CSS**: Used for creating the web page layout and styling.

- **JavaScript**: Used for client-side interactivity, including autocomplete suggestions.

- [**PokéAPI**](https://pokeapi.co/): Used to fetch Pokémon data and images.

## Getting Started

To run the application locally, follow these steps:

1. Clone this repository to your local machine.
    ```shell
    git clone https://github.com/shubham-indalkar-15/pokemon-info-flask-app.git
    ```

2. Navigate to the project directory.
    ```shell
    cd pokemon-info-flask-app
    ```

3. Install the required Python libraries.
    ```shell
    pip install flask
    ```

4. Start the Flask development server. 
    ```shell
    python app.py
    ```

5. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the Pokémon Information web app.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or create a pull request. We appreciate your feedback and contributions.

## Disclaimer

This project is not affiliated with or endorsed by Pokémon, Nintendo, or any related entities. Pokémon is a registered trademark of Nintendo, Game Freak, and Creatures.
