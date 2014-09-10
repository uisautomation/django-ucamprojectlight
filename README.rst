Introduction
============

This app allows you to include the University of Cambridge's Project
Light theme to your Django apps in a very easy way.

Usage
-----

Yo only need to add to your settings.py this application.

.. code:: python

        INSTALLED_APPS = (
            ...
            'ucamprojectlight',
            ...
        )

Create a template that extends ucamprojectlight.html and customize it
using the corresponding blocks.

You can create a global template for your project with common
customizations to all your other templates. Therefore you will only need
to extend from this global common template instead of writting all the
customizations in each template.

It is worth to mention that even if you create a global customized
template and extend this template in all your other templates, you still
can modify the blocks that you modified in your global template in all
the temples that extend the global one.

.. code:: python

    {% extends 'ucamprojectlight.html' %}

Customization using blocks
--------------------------

-  campl\_block\_head: This block rewrites the whole head tag of the
   template.
-  head\_title: The full name of the site that will be shown in the
   browser toolbar.
-  additional\_head: This block is reserverd to load extra css or js in
   case you are using extensions to the base Project Light app template.
-  app\_head: If your application is using their own javascript and
   stylesheets, load them using this block.
-  campl\_page\_header: This block rewrites the whole page header of the
   template.
-  all\_breadcrumbs: This block rewrites the whole breadcrumb section in
   case you do not want to include it in your app.
-  static\_breadcrumbs: This block includes the fixed breadcrumbs of
   your application (those that will be always shown independent from
   the page/view). The default is:

   .. code:: html

       <li>
       <a href="http://www.cam.ac.uk/">University of Cambridge</a>
       </li>
       <li>
       <a href="http://www.cam.ac.uk/about-the-university/">My Django app</a>
       </li>

-  site\_name: The full name of the site to show it in the header of the
   page.
-  search\_bar: Overwrite this block in case you do not want a search
   box in your app.
-  search\_action: action propierty of the form tag of the search box.
   Shown inside search\_bar block.
-  campl\_tabs\_header: Overwrite this block in case that your app does
   not use tabs neither have a subtitle in the page header.
-  subtitle\_div: Overwrite this block in case you do not want to show a
   subtitle in the header. The subtitle is only shown if the
   campl\_tabs\_header has not been overwritten.
-  subtitle: A subtitle to be shown below the site\_name in the page
   header. Shown inside subtitle\_div block.
-  tabs: Overwrite this block in case that your app does not use tabs.
-  page\_content: In this block the page content should be written if
   you do not want to use the contant\_column blocks.
-  content\_column\_1..content\_column\_12: Project light is responsive
   and uses a 12 columns grid system (like twitter bootstrap). The
   django-ucamprojectlight offers 12 blocks in case you want to use up
   to 12 different columns. If you just want to use n columns because
   columns are wider than 1 unit, you can use the n blocks wanted.
-  local\_footer: This block rewrites the whole page footer. Half of the
   footer is ocuppied by the variable blurb, the other half is divided
   into two, footer1 and footer2.
-  blurb: The text shown in the footer. It uses the first half of the
   width of the footer.
-  footer1: Usually used for the Help link.
-  footer2: Usually used for the Privacy & cookie policy link.
-  global\_footer: This block contains the whole global footer.
-  campl\_foot\_js: A section a the end of the body tag to load lazy
   javascript files.

Breadcrumbs
-----------

The default template include breadcrumbs to help with the navigation in
the page. Application-specific breadcrumbs are handled by a dictionary
variable "breadcrumbs" passed to the template like:

.. code:: python

        breadcrumbs = {}
        breadcrumbs[0] = dict(name='Page of my cool app', url='http://my.cool.app/page/')
        breadcrumbs[1] = dict(name='Subpage of my cool app', url='http://my.cool.app/page/subthingy/')
        ...
        return render_to_response('ucamprojectlight.html', {'breadcrumbs':breadcrumbs, ...})

Tabs
----

If your Project Light page uses tabs as part of its subheading (like the
"search" page) define them in a python file, along with their
destinations, and then add this python file to
TEMPLATE\_CONTEXT\_PROCESSORS in your settings.py

.. code:: python

    def tabs(request):
        tabs = {}
        tabs[0] = dict(name="Main",url='index')
        tabs[1] = dict(name="Example",url='example')
        tabs[2] = dict(name="Test",url='test')
        return {'tabs': tabs}

.. code:: python

    TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + ('myapp.ucamprojectlight_context_processors.tabs',)

