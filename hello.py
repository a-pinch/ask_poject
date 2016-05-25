def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [.join(env['QUERY_STRING'].splitlines(True))]
