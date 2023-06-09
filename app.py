from predict import predict 

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/process_list', methods=['POST'])
def process_list():
    print("~" * 80, '\n')
    data = request.json['list']
    print("~" * 80, '\n', request.json['list'])
    # Assuming the input is a JSON object with a "list" key containing the list
    input_list = data

    # Perform any processing on the list if needed

    return jsonify({'result': predict(input_list).tolist()})

if __name__ == '__main__':
    app.run()

