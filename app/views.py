from app import *
from app import forms
from app import models
# home page where you can add a new code
@app.route("/index")
@app.route("/")
def index():
	form   = forms.f(request.form)
	return render_template("index.html",form=form)

#add new query to the DB
@app.route("/add",methods=['POST'])
def login():
	form = forms.f(request.form)
	if request.method == "POST" and form.validate():
		try:
			generator = id_generator()
			add = models.Post(form.title.data,form.PL.data,form.code.data,generator)
			add.save()
		except:
			return "Something went wrong"
		return redirect(url_for("show",gen=generator))

	else:
		return "<h4>Please fill in all forms</h4> <a href='index'>home</a>"

#Show the pages
@app.route("/<gen>")
def show(gen):
	query = models.Post.objects.get_or_404(ID=gen)
	lexer     = get_lexer_by_name(query.PL, stripall=True)
	formatter = HtmlFormatter(linenos=True, cssclass="highlight")
	result 	  = highlight(query.code, lexer, formatter)
	return render_template("show.html",query=query,result=result)

	
# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

# Custom 405 page
@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html')    

# a function that generates random chars
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))    