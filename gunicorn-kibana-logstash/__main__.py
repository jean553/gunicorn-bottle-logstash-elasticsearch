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
    '''
    Inserts posted content into ES
    '''
    data = request.json

    date = datetime.datetime.now()
    index = date.strftime('data-%Y-%m-%d-%H')

    es_client = Elasticsearch(hosts=['elasticsearch'],)
    helpers.bulk(
        es_client,
        [{
            '_type': 'data',
            '_index': index,
            '_timestamp': datetime.datetime.now(),
            'message': data['message'],
            'status': data['status'],
        }],
    )

if __name__ == '__main__':
    run()

# hook for gunicorn
app = default_app()
