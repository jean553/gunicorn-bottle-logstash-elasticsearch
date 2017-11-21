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
    '''
    Route to check if the service is alive.
    '''
    logger = KibanaLogger(
        {
            'api_call': 'ping',
            'method': 'get',
        }
    )
    logger.info({'step': 'end'})

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
