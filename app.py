import flask
from mlTest.model import checkSuicide

app = flask.Flask(__name__,template_folder="templates")


@app.route('/')
@app.route("/home")
@app.route("/Home")
@app.route("/index")
def home_builder():
    return flask.render_template("index.html")


@app.route('/parse_data',methods=["GET",'POST'])
def parse_data(data):
    if flask.request.method == "POST":
        #Run the logistic model and return true if ideation
        return checkSuicide(data)

        #else return false


app.run()