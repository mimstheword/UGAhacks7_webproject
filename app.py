import flask

app = flask.Flask(__name__,template_folder="templates")


@app.route('/')
@app.route("/home")
@app.route("/Home")
@app.route("/index")
def home_builder():

    return flask.render_template("index.html")


app.run()