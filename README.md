# Spreadsheet App

This is a web-based spreadsheet application that allows users to perform various operations on a set of values (e.g., SUM, AVERAGE, FIND AND REPLACE, etc.). The app is built using HTML, CSS, JavaScript (jQuery), and Python (Flask) for the backend. It offers a dynamic, interactive interface to perform operations on data entered by the user.

## Features

- **SUM**: Calculates the sum of the values.
- **AVERAGE**: Computes the average of the values.
- **MAX**: Finds the maximum value.
- **MIN**: Finds the minimum value.
- **COUNT**: Counts the number of values.
- **TRIM**: Trims any leading or trailing spaces from string values.
- **UPPER**: Converts all string values to uppercase.
- **LOWER**: Converts all string values to lowercase.
- **FIND AND REPLACE**: Finds and replaces specific values.
- **REMOVE DUPLICATE**: Removes duplicate values while keeping the order.

## Technologies Used

- **Frontend**: 
 - HTML
 - CSS (Responsive design)
 - JavaScript (jQuery for dynamic operations)
 
- **Backend**: 
 - Python (Flask framework)
 
- **Database**: None (Data is stored temporarily in the application state)

## How to Run

### 1. Clone the repository

Clone the repository to your local machine using the following command:

bash
git clone https://github.com/your-username/spreadsheet-app.git


### 2. Install Dependencies

Ensure you have Python 3 installed. Navigate to the project folder and install the required dependencies:

bash
cd spreadsheet-app
pip install -r requirements.txt


If you don't have a `requirements.txt`, you can manually install the required packages:

bash
pip install flask


### 3. Run the Flask Server

To run the Flask server, use the following command:

bash
python app.py


The app will run on `http://127.0.0.1:5000/` by default.

### 4. Access the Web App

Open your web browser and go to `http://127.0.0.1:5000/` to use the Spreadsheet App.

## File Structure


spreadsheet-app/
├── app.py # Flask backend script
├── templates/
│ └── index.html # HTML frontend template
├── static/
│ └── style.css # Custom CSS for styling the app
└── README.md # Project documentation


## Project Demo

Here is a preview of the features of the app:

1. Enter a comma-separated list of values.
2. Choose an operation (e.g., SUM, AVERAGE, etc.).
3. View the result of the operation.
4. Use the 'Find and Replace' or 'Remove Duplicate' options to manipulate the data.

