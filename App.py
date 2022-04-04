from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my page'

@app.route('/contact')
def contact_page():
    return 'contact page'

@app.route('/home')
def home():
    return 'welcome to home page'

@app.route('/gallery')
def gallery():
    return 'Gallery page'

if __name__=="__main__":
    app.run()