from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
from urllib.parse import parse_qs

from webob.request import Request
from webob.response import Response
from webob.dec import wsgify
import flask


class Application:
    def __init__(self, name):
        self.name = name

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)

        # query_params = environ.get('QUERY_STRING')
        # method = environ.get('REQUEST_METHOD')
        # path = environ.get('PATH_INFO')
        # query_params_list = query_params.split('&')
        # query_params_dict = {}
        # if len(query_params) != 0:
        # query_params_list = query_params.split('&')
        # for query_param in query_params_list:
        #     k, _, v = query_param.partition('=')
        #     query_params_dict[k] = v

        # query_params_dict = {
        #     k: v for k, _, v in map(lambda x: x.partition('='), query_params_list)}
        # query_params_dict = parse_qs(query_params)

        request = Request(environ)

        print(request.path)
        print(request.params)
        print(request.method)
        print(request.url)

        response = Response(body=b'<h1>hello yamngmao web application!</h1>')
        return response(environ, start_response)


if __name__ == '__main__':
    with make_server('', 8000, Application('yangmao')) as httpd:
        print('Serving on 8000')
        httpd.serve_forever()
