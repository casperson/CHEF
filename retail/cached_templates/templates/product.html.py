# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427395997.006875
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.html'
_template_uri = 'product.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <h3 style="text-decoration: underline">Product List</h3>\r\n\r\n        <div class="text-right">\r\n            <a href="/homepage/product.create/" class="btn btn-success">Add New Product</a>\r\n        <a href="/retail/product.batch/" class="btn btn-primary">See Overdue Rentals</a>\r\n        </div>\r\n\r\n        <form id="search" method="post" action="product.search">\r\n            <input/>\r\n            <a href="/retail/product.search/" class="btn btn-info">Search Product</a>\r\n        </form>\r\n            <ul id="product_list">\r\n')
        for product in products:
            __M_writer('                <li>\r\n')
            __M_writer('                        <img class="description product-image" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('retail/media/')
            __M_writer(str( product.name ))
            __M_writer('.jpg/">\r\n                        <a href="/retail/product.detail/')
            __M_writer(str( product.id ))
            __M_writer('/">')
            __M_writer(str( product.name ))
            __M_writer('</a>\r\n                        <p>')
            __M_writer(str( product.price ))
            __M_writer('</p>\r\n')
            __M_writer('                </li>\r\n')
        __M_writer('            </ul>\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.html", "uri": "product.html", "line_map": {"64": 22, "65": 22, "66": 22, "27": 0, "36": 1, "69": 29, "68": 23, "41": 33, "76": 70, "70": 31, "47": 3, "67": 23, "55": 3, "56": 18, "57": 19, "58": 21, "59": 21, "60": 21, "61": 21, "62": 21, "63": 22}}
__M_END_METADATA
"""
