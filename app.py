from flask import Flask,request,jsonify

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    return "Hello world"

    
    return jsonify({'placement':str(cgpa)})
if __name__ == '__main__':
    app.run()