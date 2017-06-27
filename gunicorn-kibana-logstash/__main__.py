'''
Main handler
'''

from bottle import route, run

@route('/ping')
def ping():
    return 'OK'

def main():
    run()

if __name__ == '__main__':
    main()
