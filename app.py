from flask import Flask, render_template, request
from groq import Groq
import os 

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    source = request.form["source"]
    destination = request.form["destination"]
    budget = request.form["budget"]
    days = request.form["days"]
    style = request.form["style"]

    prompt = f"""
    You are an expert travel planner.

    Create a trip plan.

    Starting City: {source}
    Destination: {destination}
    Budget: {budget} INR
    Days: {days}
    Travel Style: {style}

    Return in this format:

    Trip Overview

    Day 1:
    ...

    Day 2:
    ...

    Budget Breakdown

    Food Suggestions

    Travel Tips
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    trip_plan = response.choices[0].message.content

    return render_template(
    "result.html",
    trip_plan=trip_plan
)

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )