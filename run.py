from asyncio.windows_events import NULL
from flask import Flask, render_template, abort, request, redirect, url_for

app = Flask(__name__)


# initial rendering page - details.html
@app.route('/')
def index():
    #displaying the details.html
    return render_template("details.html")

#Custom error pages

#Handling 404 Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Handling 400 Error
@app.errorhandler(400)
def page_not_found(e):
    return render_template("400.html"), 400

# takes name entered in details.html and renders display.html by passing  the name that user entered.
@app.route('/get_name/', methods=['POST'])
def get_details():
    error = None
    #method - POST - posting the data entered to the display.html 
    if request.method =='POST':
        #checking if username id from html exists.
        if 'username' in request.form:
            if len(request.form['username'])==0:
            #saving the name that user entered into a variable
                msg = "Please enter a Name"
                return render_template('details.html',msg=msg)
            elif request.form['username'].isalpha() != True:
                msg = "Please enter a name with only alphabets"
                return render_template('details.html',msg=msg)
            else:
                uname = request.form['username']
                return render_template('display.html',uname=uname)
        else:
            abort(400)
             
    # rendering template by passing the name entered by user        


#code added to run the flask application
if __name__ == '__main__':
    app.debug = False 
    app.run()
