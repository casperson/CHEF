# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422159968.100728
_enable_loop = True
_template_filename = 'C:\\Users\\Garrett\\PycharmProjects\\CHEF\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>homepage</title>\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer("        <link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,700,300,100' rel='stylesheet' type='text/css'>\r\n        <link href='http://fonts.googleapis.com/css?family=Libre+Baskerville:400,400italic,700' rel='stylesheet' type='text/css'>\r\n        <link href='http://fonts.googleapis.com/css?family=Crimson+Text:400,600' rel='stylesheet' type='text/css'>\r\n        <link href='http://fonts.googleapis.com/css?family=Pinyon+Script' rel='stylesheet' type='text/css'>\r\n\r\n")
        __M_writer('        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\r\n\r\n\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n    </head>\r\n\r\n    <body>\r\n\r\n        <header>\r\n            <link rel="icon" type="image/x-icon" href="/static/homepage/media/colonial_flag.jpg" />\r\n            <div id="div-head"></div>\r\n            <div class="container-fluid">\r\n                <div class="col-xs-3" >\r\n                    <img src="/static/homepage/media/ch_logo.png" height="75">\r\n                </div>\r\n                <div class="col-xs-4"></div>\r\n                <div class="col-xs-5" style="text-align: right;margin-top: 20px">\r\n                    <ul class="nav nav-tabs">\r\n                        <li role="menu"><a href="/homepage/index/">Home</a></li>\r\n                        <li role="log_in"><a href="/homepage/log_in/">Log In</a></li>\r\n                        <li role="event"><a href="/homepage/event/">Event</a></li>\r\n')
        __M_writer('                        <li role="menu"><a href="/homepage/inventory/">Inventory</a></li>\r\n                    </ul>\r\n                </div>\r\n            </div>\r\n            <div style="background-color: #A41425; height: 2px"></div>\r\n        </header>\r\n\r\n        <div class="container-fluid base-body">\r\n            <div class="col-xs-1" style="background-color: navy; height: 1000px">\r\n')
        __M_writer('            </div>\r\n            <div class="col-xs-10">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div class="col-xs-1" style="background-color: navy; height: 1000px"></div>\r\n        </div>\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Garrett\\PycharmProjects\\CHEF\\homepage\\templates/base.htm", "line_map": {"33": 5, "34": 15, "35": 18, "36": 24, "37": 31, "38": 31, "39": 31, "40": 52, "41": 71, "61": 73, "46": 75, "47": 81, "16": 4, "49": 81, "18": 0, "67": 61, "48": 81, "55": 73, "27": 2, "28": 4, "29": 5}, "uri": "base.htm"}
__M_END_METADATA
"""
