from flask import Flask,render_template,request,url_for,redirect
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import random
from flask.ext.mongoengine import MongoEngine
import string

#init the Flask app
app   	  						      = Flask(__name__,template_folder="../templates/")

# True means any error will be appeared to the users
app.debug 	    					  = True

# this should be changed to something encrypted
app.secret_key  					  = "Blah blah"

# init the DB
app.config["MONGODB_SETTINGS"] = {'DB': "Codes"}
database = MongoEngine(app)
from app import views,models