# Weather App

A simple and responsive weather application built with Python (Flask), HTML, and CSS. It fetches real-time weather data using an external API and displays the results in a clean web interface.

## Features

- Get current weather by city name
- Uses external Weather API (OpenWeatherMap)
- API key stored securely using .env file
- Responsive frontend with HTML & CSS
- Easy to run and extend

## Requirements

- Python 3.x
- Flask
- Requests

## Creating a Virtual Environment

To keep dependencies isolated, it's recommended to use a Python virtual environment.

## Step 1: Create a virtual environment
python -m venv .venv

## Step 2: Activate the environment
## 👉 For Windows (Command Prompt)
.venv\Scripts\activate

## 👉 For Windows PowerShell
.venv\Scripts\Activate.ps1

## 👉 For macOS/Linux
source .venv/bin/activate

## Step 3: Install all dependencies
pip install -r requirements.txt

## Environment Variables

To run this project, create a `.env` file in the root folder with the following content:

API_KEY=your_api_key_here

Replace `your_api_key_here` with your actual API key.

## How to Get an OpenWeatherMap API Key

1. Visit https://home.openweathermap.org/users/sign_up  
2. Create a free account
3. After verifying your email, go to the "API keys" tab
4. Copy the **default key** or create a new one
5. Paste it into your `.env` file like this:

API_KEY=your_actual_key_here

You’re now ready to run the app!

## How to Run

Click Run python file in VS code 

Then open your browser and go to:  
http://127.0.0.1:8000  or  localhost:8000


## License

MIT License

## Author

Developed by Subhashinee S R  
Feel free to fork, star ⭐, and contribute!
