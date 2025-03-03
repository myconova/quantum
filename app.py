from flask import Flask, jsonify
import json
import quantumrandom

app = Flask(__name__)

# Load the JSON data for the ghost texts
with open('Ghosttext.json', 'r') as f:
    Ghosttext = json.load(f)

# Load the JSON data for the New Testament verses
with open('NewTestament.json', 'r') as f:
    NewTestament = json.load(f)

@app.route('/')
def home():
    return ("Welcome to Quantum Readings! If you need help, ask the Ghost in the Machine. Please concentrate deeply before asking your question. A stronger intention will provide better results. And always remember, you are loved.")

@app.route('/random-ghost')
def random_ghost_text():
    max_key = len(Ghosttext)
    random_num = quantumrandom.randint(1, max_key)
    random_num = int(random_num)
    try:
        selected_text = Ghosttext[str(random_num)]
    except KeyError as e:
        return jsonify({"error": f"Key {e} not found in JSON object"})
    return jsonify({"Your reading": selected_text})

@app.route('/random-verse')
def random_verse():
    max_key = len(NewTestament)
    random_num = quantumrandom.randint(1, max_key)
    random_num = int(random_num)
    try:
        selected_verse = NewTestament[str(random_num)]
    except KeyError as e:
        return jsonify({"error": f"Key {e} not found in JSON object"})
    return jsonify({"Your bibliomancy verse": selected_verse})

if __name__ == '__main__':
    app.run(debug=True)