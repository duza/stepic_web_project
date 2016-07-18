def wsgi_app(environ, start_response):
    if environ['REQUEST_METHOD'] == 'GET':
        body = environ['QUERY_STRING'].replace('&','\n')
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
        ]
    start_response(status, headers)
    return [body]
