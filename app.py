from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Kampala Talent Show! All talents allowed!"

@app.route("/talents")
def talents():
    return "Singing, Dancing, Comedy, Rapping - Show us your talent!"

if __name__ == "__main__":
    app.run(debug=True)