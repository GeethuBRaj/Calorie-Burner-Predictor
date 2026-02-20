# Calorie-Burner-Predictor
A machine learning application that predicts the number of calories burned during exercise based on user inputs such as weight, exercise duration, exercise type, and gender. Built with Python, Decision Tree Regression, and a Streamlit web interface for easy interaction.
---

## Table of Contents
- [Project Overview](#project-overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Model Details](#model-details)  
- [User Interface](#user-interface)  
- [Screenshots](#screenshots)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview
The Calorie Burner Predictor helps users estimate the **calories burned during exercise**. It leverages a **Decision Tree Regression model** trained on sample data of weight, exercise type, duration, and gender. This project provides a **user-friendly interface** for real-time predictions.

---

## Features
- Predict calories burned using your **weight, duration, exercise type, and gender**.  
- Simple **web-based UI** built with Streamlit.  
- Quick and accurate predictions powered by a **Decision Tree model**.  
- Supports **multiple exercise types**: Running, Walking, Yoga, Cycling.  
- Reset button to **clear inputs**.  

---
Usage

Run the Streamlit app:

streamlit run pred.py

A web interface will open in your browser.

Enter your details:

Weight (kg)

Exercise Duration (minutes)

Exercise Type (Running, Walking, Yoga, Cycling)

Gender (Male/Female)

Click Predict Calories Burned to see the estimated calories.

Click Reset to clear the inputs.

Model Details

Algorithm: Decision Tree Regression

Target Variable: Calories Burned

Features: Weight, Duration, Exercise Type, Gender

Training Metrics:

Training MSE: 0.0

Training R²: 0.9925

Testing MSE: 118.18

Testing R²: 0.99116

The model was trained on sample exercise data and generalizes well on test data.

User Interface

The UI is designed for simplicity and usability.

Input Fields:

Weight (kg)

Duration of exercise (minutes)

Exercise Type (dropdown)

Gender (radio buttons)

Predict Button:

Click to see predicted calories burned instantly.

Optional Reset Button:

Clears all input fields to default values.

Layout Example:

+-----------------------------------------+
|       🔥 Calorie Burn Predictor         |
+-----------------------------------------+
| Weight (kg): [ 70 ]                     |
| Duration (min): [ 30 ]                  |
| Exercise Type: [ Running ▼ ]            |
| Gender: [ Male ○ Female ● ]             |
+-----------------------------------------+
|           [ Predict Calories ]          |
+-----------------------------------------+
| Calories Burned: 250 kcal               |
+-----------------------------------------+
