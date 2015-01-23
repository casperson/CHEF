# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421869996.135656
_enable_loop = True
_template_filename = 'C:\\Users\\Braden\\chef\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>homepage</title>\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer("        <link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,700,300,100' rel='stylesheet' type='text/css'>\r\n\r\n")
        __M_writer('        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n    </head>\r\n\r\n    <body>\r\n\r\n        <header>\r\n            <link rel="icon" type="image/x-icon" href="/static/homepage/media/colonial_flag.jpg" />\r\n            <div class="container-fluid">\r\n                <div class="col-xs-4" style="text-align: right" >\r\n                    <img src="/static/homepage/media/colonial_flag.jpg" alt="..." height="110" >\r\n                </div>\r\n                <div class="col-xs-6" style="text-align: left">\r\n                    <p class="row">Colonial Heritage Foundation</p>\r\n                    <p style="font-size: .5em" class="row">Preserving America&#39s Founding</p>\r\n                </div>\r\n                <div class="col-xs-2"></div>\r\n            </div>\r\n        </header>\r\n\r\n        <div class="container-fluid">\r\n            <div>\r\n                <ul class="nav nav-tabs">\r\n                    <li role="menu"><a href="/homepage/index/">Home</a></li>\r\n')
        __M_writer('                    <li role="menu"><a href="/homepage/about/">About</a></li>\r\n                    <li role="menu"><a href="/homepage/contact/">Contact</a></li>\r\n                    <li role="menu"><a href="/homepage/terms/">Terms of Service <span class="badge">Updated</span></a></li>\r\n                </ul>\r\n            </div>\r\n')
        __M_writer('            <div class="col-xs-10">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n\r\n')
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
        __M_writer('\r\n                    This is the center stuff!\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "filename": "C:\\Users\\Braden\\chef\\homepage\\templates/base.htm", "source_encoding": "ascii", "line_map": {"33": 5, "34": 15, "35": 18, "36": 21, "37": 25, "38": 25, "39": 25, "40": 51, "41": 68, "61": 69, "46": 71, "47": 76, "16": 4, "49": 76, "18": 0, "67": 61, "48": 76, "55": 69, "27": 2, "28": 4, "29": 5}}
__M_END_METADATA
"""
