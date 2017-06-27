'''
Main handler
'''

from bottle import route, run, default_app

@route('/ping')
def ping():
    return 'OK'

if __name__ == '__main__':
    run()

# hook for gunicorn
app = default_app()
