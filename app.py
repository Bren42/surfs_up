# #create a new flask instance
# #import your dependencies
from flask import Flask

app = Flask(__name__)

#create a root for our first route

@app.route('/')

def hello_world():
    return 'Hello World'



    

