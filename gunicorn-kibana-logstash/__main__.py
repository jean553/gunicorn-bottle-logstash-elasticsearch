'''
Main handler
'''

import datetime

from bottle import route, post, run, request, default_app
from elasticsearch import Elasticsearch, helpers

from kibana_logger import KibanaLogger

@route('/ping')
def ping():
    return 'OK'

@post('/post-data')
def post_data():
    '''
    Inserts posted content into ES
    '''
    logger = KibanaLogger(
        {
            'api_call': 'post-data',
            'method': 'post',
        }
    )

    data = request.json

    date = datetime.datetime.now()
    index = date.strftime('data-%Y-%m-%d-%H')

    es_client = Elasticsearch(hosts=['elasticsearch'],)
    helpers.bulk(
        es_client,
        [{
            '_type': 'data',
            '_index': index,
            'timestamp': datetime.datetime.now(),
            'message': data['message'],
            'status': data['status'],
        }],
    )

    logger.info({'step': 'end'})

# hook for gunicorn
app = default_app()
