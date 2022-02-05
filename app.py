"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from flask import Flask, render_template

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''
@app.route('/')
def home():
    return 'My home page'

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

"""Comments: in the instructions, where it said "run heroku master" I accidentally
wrote "run heroku" in the terminal and it still run and it still worked.
Also: I made changes to the text in the 404.html file just for fun"""

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
