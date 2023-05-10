from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    file.save('uploads/' + file.filename)
    return 'File saved!'

@app.route('/', methods=['GET'])
def welcome():
    return 'Api Works'

app.run()

#comments