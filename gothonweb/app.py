from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

@app.route("/")
def index():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))
    # takes the FUNCTION name

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # why is there here? do you need it?' - in case no session
            # if they somehow went straight to the game without starting at start
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room: 
                session['room_name'] = planisphere.name_room(room)
                # if action isn't valid path, nothing given to next_room
                # so just stay in current room
                
                return render_template("repeat_room.html", room=room)
                
            else:
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))
        # The reason we redirect is so browsers don't freak out over refreshes.

# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run() # may need threaded=true


# ***from flask import request***
# http://flask.pocoo.org/docs/1.0/quickstart/#accessing-request-data
# https://www.tutorialspoint.com/flask/flask_request_object.htm
# https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request

# The current request method is available by using the method attribute. 

# To access form data (data transmitted in a POST or PUT request) you can use the
# form attribute. 

# request.form: the key/value pairs in the body, from a HTML post form
# using .get because it's a dictionary



# ***from flask import session***
# allows you to store information specific to a user from one request to the next

# This is implemented on top of cookies for you and signs the cookies 
# cryptographically. What this means is that the user could look at the contents 
# of your cookie but not modify it, unless they know the secret key used for signing.
# In order to use sessions you have to set a secret key.

# Unlike a Cookie, Session data is stored on server. Session is the time 
# interval when a client logs into a server and logs out of it. The data, 
# which is needed to be held across this session, is stored in a temporary
# directory on the server.

# A session with each client is assigned a Session ID. The Session data is stored 
# on top of cookies and the server signs them cryptographically. For this encryption, 
# a Flask application needs a defined SECRET_KEY.

# Session object is also a dictionary object containing key-value pairs of session 
# variables and associated values.


# ***from flask import url_for***
# flask.url_for(endpoint, **values)

# http://flask.pocoo.org/docs/1.0/quickstart/
# To build a URL to a specific function, use the url_for() function
# It accepts the name of the function as its first argument and any number of 
# keyword arguments, each corresponding to the variable part of URL.
# which will also be inputs to the function

# https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for
# url_for in Flask is used for creating a URL to prevent the overhead of having
# to change URLs throughout an application (including in templates). Without 
# url_for, if there is a change in the root URL of your app then you have to
# change it in every page where the link is present.


# ***redirect***
# http://flask.pocoo.org/docs/1.0/api/#flask.redirect
# https://www.tutorialspoint.com/flask/flask_redirect_and_errors.htm

# Here we're using with with url_for
# url_for expects the function name and creates the address, 
# redirect just expects the address.


# ***escape***
# 
# Convert the characters &, <, >, ‘, and ” in string s to HTML-safe sequences.
# Use this if you need to display text that might contain such characters in HTML. 
# Marks return value as markup string.
#
# http://flask.pocoo.org/docs/1.0/quickstart/
# return 'Logged in as %s' % escape(session['username'])


# ***render_template***
# https://www.tutorialspoint.com/flask/flask_templates.htm

# instead of: return '<html><body><h1>'Hello World'</h1></body></html>'
# Do: return render_template(‘hello.html’)

# generating HTML content from Python code is cumbersome, especially when 
# variable data and Python language elements like conditionals or loops need
# to be put. This would require frequent escaping from HTML.

# This is where one can take advantage of Jinja2 template engine, on which Flask 
# is based. Instead of returning hardcode HTML from the function, a HTML file
#  can be rendered by the render_template() function.

# Jinga2 instead lets you escape from HTML in your own HTML scripts
# rather than in your HTML within your python which is messy.

# Flask will try to find the HTML file in the templates folder, in the same 
# folder in which this script is present.

# http://flask.pocoo.org/docs/1.0/quickstart/
# To render a template you can use the render_template() method. All you 
# have to do is provide the name of the template and the variables you want 
# to pass to the template engine as keyword arguments
 
# return render_template('hello.html', name=name)


# Inside templates you also have access to the request, session and g 
# objects as well as the get_flashed_messages() function.

# Automatic escaping is enabled, so if name contains HTML it will be 
# escaped automatically


# *** template inheratence ***
# http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/#template-inheritance


# He prints out debugging stuff from app.py into powershell