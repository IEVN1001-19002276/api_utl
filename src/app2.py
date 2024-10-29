from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

from config import config



app = Flask(__name__)

con=Flask(__name__)


@app.route("/")
def index():
    
    return ''    


if __name__=="__main__":
    app.run(debug=True)