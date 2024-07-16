from flask import Flask, jsonify, request
from gettoke import uploadFile
import os
app = Flask(__name__)
counter = 0
lis_ofvids=[i for i in os.listdir() if i.endswith('.mp4')]
list_oftxts=[i for i in os.listdir() if i.endswith('.txt')]

@app.route('/get_token', methods=['GET'])
def get_token():
    #file_name = request.args.get('file_name')
    global counter
    token = uploadFile(lis_ofvids[counter])
    #read file and get number of boxes in it
    boxes=0
    with open(list_oftxts[counter]) as f:
        boxes = f.read()
    counter += 1
    if counter == len(lis_ofvids):
        counter = 0
    return jsonify({'token': token, 'boxes': boxes})

if __name__ == '__main__':
    app.run(debug=True)
