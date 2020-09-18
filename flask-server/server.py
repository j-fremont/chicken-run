from flask import Flask, request, send_file 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/get_image", methods = ['GET'])
def get_image():
	if request.method == 'GET':
       		return send_file('/tmp/image.jpg', mimetype='image/jpg')

if __name__ == '__main__':
     app.run(host='0.0.0.0',port='5000',debug=True)
