from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json()
    name = request_data.get('name',"")
    return f'You entered: {name}'
    

if __name__ == '__main__':
    app.run(debug=True)
