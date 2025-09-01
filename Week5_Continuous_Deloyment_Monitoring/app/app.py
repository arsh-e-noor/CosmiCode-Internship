from flask import Flask, render_template, request, Response
import requests
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

API_KEY = "d21e18cf6ba98f9705ad06f4bd85d6a0" 

# Prometheus metrics
weather_requests_total = Counter('weather_requests_total', 'Total weather requests', ['status'])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        try:
            response = requests.get(url).json()
        except requests.exceptions.RequestException:
            weather_requests_total.labels(status="failed").inc()
            return render_template("index.html", error="Unable to connect to the weather service.")

        if response.get("cod") != 200:
            weather_requests_total.labels(status="failed").inc()
            return render_template("index.html", error=response.get("message", "City not found. Try again!"))

        weather_requests_total.labels(status="success").inc()
        weather = {
            "city": response["name"],
            "temp": response["main"]["temp"],
            "description": response["weather"][0]["description"],
            "icon": response["weather"][0]["icon"],
            "main": response["weather"][0]["main"].lower()  
        }
        return render_template("result.html", weather=weather)
    return render_template("index.html", error=None)

# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
