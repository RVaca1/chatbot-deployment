from flask import Flask, render_template, request, jsonify
from chat import get_response  # Assuming get_response is a function in your chat.py

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_get():
    return render_template('base.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ensure that the request body contains valid JSON
    try:
        data = request.get_json()  # Parse incoming JSON
        if not data:
            return jsonify({"error": "No JSON received or invalid JSON"}), 400
        
        text = data.get('message')  # Get the message from JSON data
        if not text:
            return jsonify({"error": "'message' key is missing in the request"}), 400
        
        # Get the response from your chatbot function
        response = get_response(text)
        return jsonify({'answer': response})

    except Exception as e:
        # Log the exception (you can print it to the console or log it to a file)
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
