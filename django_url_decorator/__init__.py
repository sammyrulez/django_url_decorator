from django.core.urlresolvers import RegexURLResolver
import sys
from django.conf.urls import patterns
from django.conf.urls import url as dcud_url


def include_urlpatterns(regex, module):
    """
    Usage:
    
    # in top-level module code:
    urlpatterns = include_urlpatterns(r'^profile/', 'apps.myapp.views.profile')
    """
    return [RegexURLResolver(regex, module)]

#
# Annotate a view with the URL that points to it
#

def url(pattern, *args, **kwargs):
    """
    Usage:
    @url(r'^users$')
    def get_user_list(request):
        ...
        
    @url(r'^info/(.*)/$', name="url-name") 
    def wiki(request, title=''):
        ...
    """
    caller_filename = sys._getframe(1).f_code.co_filename
    module = None
    for m in sys.modules.values():
        if m and '__file__' in m.__dict__ and m.__file__.startswith(caller_filename):
            module = m
            break
    def _wrapper(f):
        if module:
            if 'urlpatterns' not in module.__dict__:
                module.urlpatterns = []
            module.urlpatterns += patterns('', dcud_url(pattern, f, *args, **kwargs))
        return f
    return _wrapper

def simple_url(pattern, *args, **kwargs):
    """
    Usage:
    @url('/users/{id}')
    def get_user_detail(request,id):
        ...
        
   
    """
    url_regxp_pattern = r'^'+pattern[1:].replace('{','(?P<').replace('}','>\w+)') + '$'
    
    caller_filename = sys._getframe(1).f_code.co_filename
    module = None
    for m in sys.modules.values():
        if m and '__file__' in m.__dict__ and m.__file__.startswith(caller_filename):
            module = m
            break
    def _wrapper(f):
        if module:
            if 'urlpatterns' not in module.__dict__:
                module.urlpatterns = []
            module.urlpatterns += patterns('', dcud_url(url_regxp_pattern, f, *args, **kwargs))
        return f
    return _wrapper