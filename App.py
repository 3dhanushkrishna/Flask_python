from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/home')
def home():
    return 'welcome to home page'

@app.route('/gallery')
def gallery():
    return 'Gallery page'

if __name__=="__main__":
    app.run()