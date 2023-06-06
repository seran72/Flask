from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['POST'])
def receive_stream():
    data = request.get_data().decode('utf-8')
    print(data)
    
    # Save the data to a text file
    with open('received_data.txt', 'w') as file:
        file.write(data)
    
    return "Data received and saved"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
