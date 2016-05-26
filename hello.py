def application(environ, start_response):
    start_response('200 OK', [('content-type', 'text/plain')])
    return [environ['QUERY_STRING'].replace('&','\n')]
