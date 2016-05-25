from cgi import parse_qs, escape

def application(env, start_response):
	d = parse_qs(env['QUERY_STRING'])
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [str(d)]
