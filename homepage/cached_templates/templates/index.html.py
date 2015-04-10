# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428640631.087628
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<head>\r\n    <meta name="description" content="The Colonial Heritage Foundation">\r\n    <meta name="keywords" content="Colonial Heritage, historical reenactment, american revolution, festival">\r\n    <meta name="author" content="The Colonial Heritage Foundation">\r\n</head>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div id="homeCarousel" class="carousel slide" data-ride="carousel">\r\n        <!-- Indicators -->\r\n        <ol class="carousel-indicators">\r\n            <li data-target="#homeCarousel" data-slide-to="0" class="active"></li>\r\n            <li data-target="#homeCarousel" data-slide-to="1"></li>\r\n            <li data-target="#homeCarousel" data-slide-to="2"></li>\r\n            <li data-target="#homeCarousel" data-slide-to="3"></li>\r\n        </ol>\r\n\r\n        <!-- Wrapper for slides -->\r\n        <div class="carousel-inner" role="listbox">\r\n            <div class="item active">\r\n                <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/chef_military.jpg" alt="...">\r\n                <div class="carousel-caption">\r\n                    <h2>The Military</h2>\r\n                </div>\r\n            </div>\r\n            <div class="item">\r\n                <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/chef_pottery.jpg" alt="...">\r\n                <div class="carousel-caption">\r\n                    <h2>The Potter</h2>\r\n                </div>\r\n            </div>\r\n            <div class="item">\r\n                <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/chef_peddler.jpg" alt="...">\r\n                <div class="carousel-caption">\r\n                    <h2>The Peddler</h2>\r\n                </div>\r\n            </div>\r\n                <div class="item">\r\n                <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/chef_cannon.jpg" alt="...">\r\n                <div class="carousel-caption">\r\n                    <h2>The Cannon</h2>\r\n                </div>\r\n            </div>\r\n        </div>\r\n\r\n        <!-- Controls -->\r\n        <a class="left carousel-control" href="#homeCarousel" role="button" data-slide="prev">\r\n            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>\r\n            <span class="sr-only">Previous</span>\r\n        </a>\r\n        <a class="right carousel-control" href="#homeCarousel" role="button" data-slide="next">\r\n            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>\r\n            <span class="sr-only">Next</span>\r\n        </a>\r\n    </div>\r\n    <div>\r\n        <h1>The Colonial Heritage Foundation</h1>\r\n        <p>The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America\'s founding. To accomplish this mission, the Foundation engages in a broad array of activities. Among these are the development and presentation of educational exhibits, the coordination of reading and discussion groups to encourage the study of America\'s historical writings, the presentation of lectures and seminars regarding America\'s founding era, the coordination of historical reenactments and skill demonstrations, and the coordination of internships and apprenticeships that teach the occupational skills of early America.</p>\r\n        <br/>\r\n        <h3>Education Exhibits</h3>\r\n        <p>At its heart, the Foundation is an educational institution.  One of its major undertakings is developing exhibits and programs that can help bring to life the history surrounding America\'s colonial period and is founding generation.  To this end, the Foundation has developed a variety of traveling exhibits.  One exhibit is focuses on the importance of the press in the American Revolution and of the continued importance of a free press in America today.  The central artifact of this exhibit is a replica of the Isaiah Thomas Press, an 18th century press that was influential building support for American independence.</p>\r\n        <br/>\r\n        <p>Another exhibit focuses on the early colonial period and the ides of self-government that were planted in Jamestowne and Plimoth.  At the center of this exhibit is a scale model of the Mayflower. The exhibit also includes replicas of various artifacts from the early colonial period.</p>\r\n        <br/>\r\n        <h3>Workshops, Lectures, and Seminars</h3>\r\n        <p>The Foundation sponsors lectures, seminars and workshops about the values, culture, skills, and history of America\'s founding era. Such events may be coordinated with universities and other educationally-focused organizations to educate adults about the sacrifices that early Americans made to provide today\'s population with the freedoms we enjoy. These events  seek to inspire individuals to engage in community-based educational activities to increase exposure an awareness of the history surrounding America\'s founding. Lectures, seminars and workshops are coordinated and presented year-round by Foundation volunteers. Depending on the venue, they are offered either free of charge or for a fee. </p>\r\n        <br/>\r\n        <h3>Reading and Discussion Groups</h3>\r\n        <p>The Foundation coordinates and helps to establish community groups to encourage the reading and discussion of America\'s historical documents. For example, the Federalist Papers and the Anti-federalist Papers were publications that made the argument for and against the adoption of America\'s current constitution. The study and discussion of these documents can help Americans today understand the issues that were of most concern to our founding generation regarding the establishment of a strong federal government. These documents were written in a language style that is foreign to most contemporary readers. By providing recommended reading schedules, discussion questions, and materials to help modern readers read and grasp federal-period writings, the Foundation hopes to encourage small, community-based groups to undertake independent study of such founding documents. These discussion groups will be conducted year-round by volunteers and held in homes or community meeting places throughout the nation. </p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "index.html", "line_map": {"66": 60, "35": 1, "45": 8, "27": 0, "52": 8, "53": 21, "54": 21, "55": 27, "56": 27, "57": 33, "58": 33, "59": 39, "60": 39}, "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/index.html"}
__M_END_METADATA
"""
