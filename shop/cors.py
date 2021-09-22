from django.utils.deprecation import MiddlewareMixin

class CorsMiddleware(MiddlewareMixin):
	def process_response(self, req, response):
		response['Access-Control-Allow-Origin'] = "*"
		return response

