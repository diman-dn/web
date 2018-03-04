from cgi import parse_qs

def app(environ, start_response):
	query = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
	body = []
	for key, value in query.items():
		for item in value:
			body.append(key + "=" + item + "\r\n")

	status = '200 OK'
	headers = [
		('Content-type', 'text-plain')
	]
	start_response(status, headers)
	return body
