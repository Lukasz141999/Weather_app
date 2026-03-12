from flask import Flask, render_template, request, redirect, url_for
from weather import get_weather
from db import create_table, save_weather, get_weather_history
app = Flask(__name__)
weather_data = None

@app.route("/", methods=["GET", "POST"])
def index():
    global weather_data

    if request.method == "POST":
        action = request.form.get("action")
        if action == "get_weather":
            city = request.form.get("city")
            weather_data = get_weather(city)
        elif action == "save_weather":
            if weather_data:
                save_weather(weather_data)
        elif action == "weather_history":
            return redirect(url_for("history"))  # <-- tutaj przekierowanie

    return render_template("index.html", weather=weather_data)

# NOWY ENDPOINT
@app.route("/history")
def history():
    data = get_weather_history()
    return render_template("history.html", weather_history=data)

if __name__ == "__main__":
    create_table()
    app.run(host="0.0.0.0", port=5000, debug=True)