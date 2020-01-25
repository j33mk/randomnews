#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request,jsonify
import random
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os
import requests
from bs4 import BeautifulSoup

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


# @app.route('/')
# def home():
#     return render_template('pages/placeholder.home.html')
@app.route('/')
def news():
    return render_template('pages/placeholder.news.html')
@app.route('/randomnews')
def randomnews():
    html = requests.get('http://www.dawn.com')
    soup = BeautifulSoup(html.text, 'html5lib')
    h2 = soup.find_all('h2', {'data-layout': 'story'})
    news = []
    for link in h2:
        mylink = BeautifulSoup(str(link), 'html.parser')
        gettinglink = mylink.find('a', href=True)
        newsarray = []
        newsarray.append(str(gettinglink.find(text=True)))
        newsarray.append(str(gettinglink['href']))
        news.append(newsarray)
    response = jsonify({
        'data':random.choice(news),
        'status':'awesome'
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response,200

@app.route('/fortune', methods=['GET'])
def fortune():
    fortunes = [
      'A feather in the hand is better than a bird in the air. ',
      'A golden egg of opportunity falls into your lap this month.',
      'Bide your time, for success is near.',
      'Curiosity kills boredom. Nothing can kill curiosity.',
      'Disbelief destroys the magic.',
      'Dont just spend time. Invest it.',
      'Every wise man started out by asking many questions.',
      'Fortune Not Found: Abort, Retry, Ignore?',
      'Good to begin well, better to end well.',
      'How many of you believe in psycho-kinesis? Raise my hand.',
      'Imagination rules the world.',
      'Keep your face to the sunshine and you will never see shadows.',
      'Listen to everyone. Ideas come from everywhere.',
      'Man is born to live and not prepared to live.',
      'No one can walk backwards into the future.',
      'One of the first things you should look for in a problem is its positive side.',
      'Pick battles big enough to matter, small enough to win.',
      'Remember the birthday but never the age.',
      'Success is failure turned inside out.',
      'The harder you work, the luckier you get.',
      'Use your eloquence where it will do the most good.',
      'What is hidden in an empty box?',
      'Your reputation is your wealth.'
    ]
    response = jsonify({
        'data':random.choice(fortunes),
        'status':'awesome'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response,200


# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
