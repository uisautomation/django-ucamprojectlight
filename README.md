# If your Project Light page uses tabs as part of its subheading (like the "search" page)
# define them here, along with their destinations, and then add
# TEMPLATE_CONTEXT_PROCESSORS = ('myapp.campl_context_processors.tabs',)
# to your settings.py
def tabs(request):
    tabs = {}
    tabs[0] = dict(name="Main",url='index')
    tabs[1] = dict(name="Example",url='example')
    tabs[2] = dict(name="Test",url='test')
    return {'tabs': tabs}
    
    
def example(request, active_tab_name):
    breadcrumbs = {}
    # This is just a demo.
    # See campl-page-header.html for more information about how to use breadcrumbs.
    breadcrumbs[0] = dict(name="Breadcrumb", url='http://www.cam.ac.uk/')
    return render_to_response('campl.html', {'breadcrumbs':breadcrumbs, 'active_tab_name':active_tab_name},context_instance=RequestContext(request))
    
    
# BEGIN campl common settings
# campl needs to be able to find templates
import os.path
TEMPLATE_DIRS += (
    os.path.join(os.path.dirname(__file__), 'campl-templates').replace('\\','/'),
)

# make static files work in development
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATICFILES_DIRS += (
    PROJECT_ROOT + '/campl-static/',
)
# END campl common settings

# Now, whatever app you are running, you'll need a copy of this in it if you want to use tabs. That means
# physically copying it into your project folder, and updating the path. I haven't worked out a way around
# this yet. -rwhb2

# campl tabs requires a new context preprocessor
TEMPLATE_CONTEXT_PROCESSORS = ('campl.campl_context_processors.tabs',)