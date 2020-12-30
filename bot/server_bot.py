import flask
from flask import request, jsonify

from data import kg
from data import fisgou
from data import linha

app = flask.Flask(__name__)
app.config["DEBUG"] = True


saco_bbox = (115,175,254,202)
line_bbox = (2141,917,2300,1014)
fisgar_pos = (2411, 953)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route("/")
def hello():
    return "Hello, World!"

# A route to return all of the available entries in our catalog.
@app.route('/books', methods=['GET'])
def api_all():
    return jsonify(books)    


# A route to return all of the available entries in our catalog.
@app.route('/books', methods=['GET'])
def api_all():
    return jsonify(books)    




if __name__ == '__main__':
    app.run()    