from flask import Flask, jsonify
import quantumrandom

app = Flask(__name__)

#generate quantum lottery numbers
@app.route('/generate', methods=['GET'])
def quantum_lottery():
    powerball_numbers = [quantumrandom.randint(1, 69) for _ in range(5)]
    powerball_powerball = quantumrandom.randint(1, 26)
    megamillions_numbers = [quantumrandom.randint(1, 70) for _ in range(5)]
    megamillions_megaball = quantumrandom.randint(1, 25)

    return jsonify({
        'powerball': {
            'numbers': powerball_numbers,
            'powerball': powerball_powerball
        },
        'megamillions': {
            'numbers': megamillions_numbers,
            'megaball': megamillions_megaball
        }
    })

if __name__ == '__main__':
    app.run(debug=True)