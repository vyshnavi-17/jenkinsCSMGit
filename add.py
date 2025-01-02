from flask import Flask
import os

# Create a Flask app instance
app = Flask(_name_)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, Greatcoders team, How are you team"

# Run the application
if _name_ == '_main_':
    port=int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
