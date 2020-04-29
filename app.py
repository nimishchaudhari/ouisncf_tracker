from flask import Flask
app = Flask(__name__)
from flask import request
import thecode as tc
import requests
import eventlet
eventlet.monkey_patch()



@app.route('/')
def hello():
    return "Hello World!"

@app.route('/train', methods=['POST'])
def findtrain():
    #error = None
    with eventlet.Timeout(20):

        if request.method == 'POST':
            return tc.find_train(request.form['Dept_stat'],
                        request.form['Arr_stat'],
                        request.form['from_datetime'],
                        request.form['till_datetime']
                        )


@app.route('/cheapest_train', methods=['POST'])
def cheapest_train():
    with eventlet.Timeout(20):
        return tc.cheapest_ticket(request.form['Dept_stat'],
                        request.form['Arr_stat'],
                        request.form['from_datetime'],
                        request.form['till_datetime']
                        )

if __name__ == '__main__':
    app.run()
