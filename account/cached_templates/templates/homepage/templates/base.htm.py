# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427992256.319116
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n\n')
        __M_writer("        <link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,700,300,100' rel='stylesheet' type='text/css'>\n        <link href='http://fonts.googleapis.com/css?family=Libre+Baskerville:400,400italic,700' rel='stylesheet' type='text/css'>\n        <link href='http://fonts.googleapis.com/css?family=Crimson+Text:400,600' rel='stylesheet' type='text/css'>\n        <link href='http://fonts.googleapis.com/css?family=Pinyon+Script' rel='stylesheet' type='text/css'>\n\n")
        __M_writer('        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\n\n')
        __M_writer('        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n\n\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n    </head>\n\n    <body>\n\n        <header>\n            <link rel="icon" type="image/x-icon" href="/static/homepage/media/colonial_flag.jpg" />\n            <div id="div-head"></div>\n            <div class="container-fluid">\n                <div class="col-xs-3" >\n                    <img src="/static/homepage/media/ch_logo.png" height="75">\n                </div>\n                <div class="col-xs-2"></div>\n                <div class="col-xs-7" style="text-align: right;margin-top: 20px">\n')
        if request.user.is_authenticated():
            __M_writer('                        Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer('\n                        <a role="logout"><a class="btn btn-danger btn-s" href="/homepage/logout/">Log Out</a>\n')
        else:
            __M_writer('                        <button id="show_login_dialog" class="btn btn-success">Login</button>\n                        <button id="create_account_btn" class="btn btn-warning">Create Account</button>\n')
        __M_writer('                    <ul class="nav nav-tabs">\n                        <li role="menu"><a href="/homepage/index/">Home</a></li>\n                        <li role="phone"><a href="/retail/product/">Product List</a></li>\n')
        if request.user.is_authenticated():
            __M_writer('                            <li role="person"><a href="/account/user/">Users</a></li>\n                            <li role="rentals"><a href="/retail/rental/">Rentable Items</a></li>\n                            <li role="venue"><a href="/venue/venue/">Venues</a></li>\n                            <li role="menu"><a href="/homepage/item/">Inventory</a></li>\n                            <li><a href="/../account/account/">My Account</a></li>\n                            <li><button class="btn btn-warning" id="shopping_cart_dialog2"><i class="fa fa-shopping-cart"></i> Shopping Cart</button></li>\n                            <br/>\n')
        else:
            pass
        __M_writer('                    </ul>\n                </div>\n            </div>\n            <div style="background-color: #A41425; height: 2px"></div>\n        </header>\n\n        <div class="container-fluid base-body">\n            <div class="col-xs-1" style="background-color: navy; height: 1000px">\n\n            </div>\n            <div class="col-xs-10">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\n            </div>\n            <div class="col-xs-1" style="background-color: navy; height: 1000px">\n\n            </div>\n        </div>\n\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF/homepage/templates/base.htm", "line_map": {"64": 89, "65": 89, "71": 79, "77": 79, "16": 4, "18": 0, "83": 77, "28": 2, "29": 4, "30": 5, "34": 5, "35": 13, "36": 16, "37": 22, "38": 27, "39": 27, "40": 27, "41": 28, "42": 28, "43": 32, "44": 32, "45": 32, "46": 47, "47": 48, "48": 48, "49": 48, "50": 50, "51": 51, "52": 54, "53": 57, "54": 58, "55": 65, "57": 68, "62": 81, "63": 89}, "uri": "/homepage/templates/base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
