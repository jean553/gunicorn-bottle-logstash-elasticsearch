'''
Main handler
'''

from bottle import (
    route,
    post,
    default_app,
)

from kibana_logger import KibanaLogger


@route('/ping')
def ping():
    return 'OK'


@post('/post-data')
def post_data():
    '''
    Logs some data into Logstash.
    '''
    logger = KibanaLogger(
        {
            'api_call': 'post-data',
            'method': 'post',
        }
    )
    logger.info({'step': 'end'})


# hook for gunicorn
app = default_app()
