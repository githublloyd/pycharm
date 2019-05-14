app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# run this file from the command line and then open the local lost address