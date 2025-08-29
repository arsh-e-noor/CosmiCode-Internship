from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "d21e18cf6ba98f9705ad06f4bd85d6a0"  # Replace with your OpenWeather API key

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        if response.get("cod") != 200:
            return render_template("index.html", error="City not found. Try again!")

        weather = {
            "city": response["name"],
            "temp": response["main"]["temp"],
            "description": response["weather"][0]["description"],
            "icon": response["weather"][0]["icon"],
            "main": response["weather"][0]["main"].lower()  # for background theme
        }
        return render_template("result.html", weather=weather)
    return render_template("index.html")

if __name__ == "__main__":
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

