from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/total', methods=['POST'])
def total():
    numbers_list = json.loads(request.form['numbers_to_add'])
    total = sum(numbers_list)
    print({'total': total})
    return {'total': total}

if __name__ == '__main__':
    app.run(debug=True)
