# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428647162.976791
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF/homepage/templates/base.htm'
_template_uri = 'homepage/templates/base.htm'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer("        <link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,700,300,100' rel='stylesheet' type='text/css'>\r\n        <link href='http://fonts.googleapis.com/css?family=Libre+Baskerville:400,400italic,700' rel='stylesheet' type='text/css'>\r\n        <link href='http://fonts.googleapis.com/css?family=Crimson+Text:400,600' rel='stylesheet' type='text/css'>\r\n        <link href='http://fonts.googleapis.com/css?family=Pinyon+Script' rel='stylesheet' type='text/css'>\r\n\r\n")
        __M_writer('        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n    </head>\r\n\r\n    <body>\r\n\r\n        <header>\r\n            <link rel="icon" type="image/x-icon" href="/static/homepage/media/colonial_flag.jpg" />\r\n            <div id="div-head"></div>\r\n            <div class="container-fluid">\r\n                <div class="col-xs-3" >\r\n                    <a href=/homepage/index/>\r\n                        <img src="/static/homepage/media/ch_logo.png" height="75">\r\n                    </a>\r\n                </div>\r\n                <div class="col-xs-2"></div>\r\n                <div class="col-xs-7" style="text-align: right;margin-top: 20px">\r\n')
        if request.user.is_authenticated():
            __M_writer('                        Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer('\r\n                        <a role="logout"><a class="btn btn-danger btn-xs" href="/account/account.logout_user/">Log Out</a>\r\n')
        else:
            __M_writer('                        <button id="show_login_dialog" class="btn btn-success">Login</button>\r\n                        <button id="create_account_btn" class="btn btn-warning">Create Account</button>\r\n')
        __M_writer('                    <ul class="nav nav-tabs">\r\n')
        if request.user.is_authenticated() and request.user.groups.filter(name='Admins').exists():
            __M_writer('                            <li role="presentation" class="dropdown">\r\n                                <a class="dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-expanded="false">\r\n                                  Manage <span class="caret"></span>\r\n                                </a>\r\n                                <ul class="dropdown-menu" role="menu">\r\n                                    <li role="person"><a href="/account/user/">Users</a></li>\r\n                                    <li role="festivals"><a href="/homepage/events.manage/">Festivals</a></li>\r\n                                    <li role="Inventory"><a href="/retail/rental.manageitems/">Rentable Items</a></li>\r\n                                    <li role="Product"><a href="/retail/product.manage">Products</a></li>\r\n                                    <li role="manage rentals"><a href="/retail/rental.manage">Rented Items</a></li>\r\n                                </ul>\r\n                            </li>\r\n                            <li role="phone"><a href="/retail/product/">Product List</a></li>\r\n                            <li role="rentals"><a href="/retail/rental/">Rentable Items</a></li>\r\n                            <li role="festivals"><a href="/homepage/events/">Festivals</a></li>\r\n                            <li><a href="/account/account/">My Account</a></li>\r\n                            <li><button class="btn btn-warning" id="shopping_cart_dialog2"><i class="fa fa-shopping-cart"></i> Shopping Cart</button></li>\r\n                            <br/>\r\n')
        elif request.user.is_authenticated():
            __M_writer('                           <li role="phone"><a href="/retail/product/">Product List</a></li>\r\n                           <li role="rentals"><a href="/retail/rental/">Rentable Items</a></li>\r\n                           <li role="festivals"><a href="/homepage/events.view/">Festivals</a></li>\r\n                           <li><a href="/account/account/">My Account</a></li>\r\n                           <li><button class="btn btn-warning" id="shopping_cart_dialog2"><i class="fa fa-shopping-cart"></i> Shopping Cart</button></li>\r\n')
        else:
            __M_writer('                            <li role="festivals"><a href="/homepage/events/">Festivals</a></li>\r\n')
        __M_writer('                    </ul>\r\n                </div>\r\n            </div>\r\n            <div style="background-color: #A41425; height: 2px"></div>\r\n        </header>\r\n\r\n        <div class="container-fluid base-body">\r\n            <div class="col-xs-1 side-div">\r\n\r\n            </div>\r\n            <div class="col-xs-10">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div class="col-xs-1 side-div">\r\n\r\n            </div>\r\n        </div>\r\n\r\n')
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
{"filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF/homepage/templates/base.htm", "line_map": {"64": 98, "65": 106, "66": 106, "67": 106, "73": 96, "79": 96, "16": 4, "18": 0, "85": 79, "28": 2, "29": 4, "30": 5, "34": 5, "35": 13, "36": 16, "37": 22, "38": 27, "39": 27, "40": 27, "41": 28, "42": 28, "43": 32, "44": 32, "45": 32, "46": 49, "47": 50, "48": 50, "49": 50, "50": 52, "51": 53, "52": 56, "53": 57, "54": 58, "55": 76, "56": 77, "57": 82, "58": 83, "59": 85}, "source_encoding": "ascii", "uri": "homepage/templates/base.htm"}
__M_END_METADATA
"""
