import flask
from mlTest.model import checkSuicide

app = flask.Flask(__name__,template_folder="templates")


@app.route('/')
@app.route("/home")
@app.route("/Home")
@app.route("/index")
def home_builder():
    return flask.render_template("index.html")


@app.route('/parse_data',methods=['POST'])
def parse_data():
    if flask.request.method == "POST":
        #Run the logistic model and return true if ideation
        data = str(flask.request.form)
        return checkSuicide(data).to_dict()

        #else return false


if __name__ == "__main__":
	app.run(host="0.0.0.0")
