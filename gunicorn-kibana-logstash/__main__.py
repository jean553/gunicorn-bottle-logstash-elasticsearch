'''
Main handler
'''

from bottle import route, post, run, default_app
from elasticsearch import helpers

@route('/ping')
def ping():
    return 'OK'

@post('/post-data')
def post_data():
    return 'OK'

if __name__ == '__main__':
    run()

# hook for gunicorn
app = default_app()
