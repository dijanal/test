"""Flask app."""

from flask import Flask 
from models import Comment
from models import Table, Col


app = Flask(__name__)


@app.route("/")
def index():
    
    return "Welcome!"

@app.route('/comments')
def comments():
	page="""
	<DOCTYPE html>
	<html>
	<head>
	</head>
	<body>
	{}
	</body>
	</html>
	"""
	table = ItemTable(COMMENTS)
	return page.format(table)



