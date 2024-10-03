from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    value1 = data.get('value1')
    value2 = data.get('value2')
    # Here, you can connect to the database to insert the data
    return jsonify({'message': 'Data received successfully', 'value1': value1, 'value2': value2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
