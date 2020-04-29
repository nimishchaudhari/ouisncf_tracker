from flask import Flask
app = Flask(__name__)
from flask import request
import thecode as tc

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

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
    # the code below is executed if the request method
    # was GET or the credentials were invalid


@app.route('/cheapest_train', methods=['POST'])
def cheapest_train():
    return tc.cheapest_ticket(request.form['Dept_stat'],
                       request.form['Arr_stat'],
                       request.form['from_datetime'],
                       request.form['till_datetime']
                       )

if __name__ == '__main__':
    app.run()
