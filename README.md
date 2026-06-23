# AI Trip Planner ✈️

An AI-powered travel planning web application built using Flask and Groq AI. Users can enter their travel details, and the AI generates a personalized day-wise itinerary, budget suggestions, food recommendations, and travel tips.

---

## Features

- AI-generated travel itineraries
- Day-wise trip planning
- Budget-based recommendations
- Multiple travel styles (Budget, Luxury, Adventure, Family)
- Modern Bootstrap UI
- Instant AI responses using Groq API
- Responsive design

---

## Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### Backend
- Python
- Flask

### AI Integration
- Groq API
- Llama 3

### Version Control
- Git
- GitHub

---

## Project Structure

```text
AI-Trip-Planner/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
```

---

## How It Works

1. User enters:
   - Starting City
   - Destination
   - Budget
   - Number of Days
   - Travel Style

2. Flask receives the data.

3. A prompt is generated and sent to the Groq AI model.

4. The AI creates:
   - Trip Overview
   - Day-wise Itinerary
   - Budget Breakdown
   - Food Suggestions
   - Travel Tips

5. Results are displayed in a modern UI.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Amitsharma935/AI-trip-planner.git
cd AI-trip-planner
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Create Environment Variable

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Future Improvements

- Hotel recommendations
- Weather integration
- Maps integration
- PDF trip export
- User accounts
- Trip history
- Travel cost analytics

---

## Author

**Amit Sharma**

B.Tech IoT Student  
Madhav Institute of Technology and Science (MITS), Gwalior

---

## Project Goal

This project was built to learn:

- Flask Web Development
- API Integration
- Prompt Engineering
- AI Application Development
- Git & GitHub
- Deployment Workflows

---

## Live Demo

Coming Soon 🚀
