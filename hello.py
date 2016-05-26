def application(env, start_response):
	resp = env['QUERY_STRING']
	print('1:\n')
	print(resp)
	resp = ''.join(resp)
	print('2:\n)
	print(resp)
	resp = resp.split('&')
	print('3:\n)
	print(resp)
	resp = [item+'\r\n' for item in resp]
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return ['resp']
