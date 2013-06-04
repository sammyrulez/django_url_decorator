django_url_decorator
====================

Django url decorator

	Install:
	pip install -e git+https://github.com/sammyrulez/django_url_decorator.git#egg=django_url_decorator

    Usage:
    @url(r'^users$')
    def get_user_list(request):
        ...
        
    @url(r'^info/(.*)/$', name="url-name") 
    def wiki(request, title=''):
        ...
        
        
    @simple_url('/users/{id}')
    def get_user_detail(request,id):
        ...
