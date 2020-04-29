from flask import Flask
app = Flask(__name__)
from flask import request
import thecode as tc
import requests




@app.route('/')
def hello():
    return "Hello World!"

@app.route('/train', methods=['POST'])
def findtrain():
    #error = None
    if request.method == 'POST':
        return tc.find_train(request.form['Dept_stat'],
                    request.form['Arr_stat'],
                    request.form['from_datetime'],
                    request.form['till_datetime']
                    )


@app.route('/cheapest_train', methods=['POST'])
def cheapest_train():
    return tc.cheapest_ticket(request.form['Dept_stat'],
                    request.form['Arr_stat'],
                    request.form['from_datetime'],
                    request.form['till_datetime']
                    )

if __name__ == '__main__':
    app.run()
