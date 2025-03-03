from flask import Flask, jsonify
import quantumrandom

app = Flask(__name__)

#convert numbers to "heads" and "tails"
def convert_to_heads_tails(numbers):
    return ["heads" if num == 1 else "tails" for num in numbers]

#determine changing lines
def changing_lines(line):
    return line.count("heads") == 3 or line.count("tails") == 3

#generate reading
@app.route('/generate', methods=['GET'])
def iching_reading():
    lines = {}
    for i in range(1, 7):
        raw_line = [quantumrandom.randint(1, 2) for _ in range(3)]
        converted_line = convert_to_heads_tails(raw_line)
        changing = changing_lines(converted_line)
        lines(f'line_{i}'] = {
            'raw': raw_line,
            'converted': converted_line,
            'changing': changing
            'type': 'yin' if converted_line.count("heads") == 1 else 'yang'
        })

#map the lines to the correct I ching reading (1-64)
#still need to figure this part out.
    
    return jsonify({
        'Your reading': lines,
        'hexagram': hexagram_number
    })

    

if __name__ == '__main__':
    app.run(debug=True)