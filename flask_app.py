from flask import Flask, render_template, request

import Robust_hashing
from main import main_algo_flow
from test_evaluations import test_image

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    BF = main_algo_flow()
    app.config["bf"] = str(BF);
    items=[
        {
            'id':'1',
            'title': 'hello',
            'description': 'ok ok',
            'created_date': '2018-09-09'
        },
        {
            'id':'2',
            'title': 'hello 2',
            'description': 'ok ok 2',
            'created_date': '2018-10-09'
        }
    ]
    columns= [ 'id', 'title', 'description', 'created_date']
    return render_template('success.html', bf=str(BF), column=columns, rows=items)


@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        selected_test = request.form.get('test_choice')
        result = test_image(selected_test)
    return render_template('success.html', bf=app.config["bf"], result=str(result))


if __name__ == "__main__":
    app.run()
