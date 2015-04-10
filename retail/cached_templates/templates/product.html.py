# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428646445.024032
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
        __M_writer('\r\n\r\n    <div>\r\n        <h2 style="text-decoration: underline">Products</h2>\r\n        <a href="/retail/product/" class="btn btn-success"><i class="fa fa-plus"></i> Request Custom Product</a>\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n        <div class="pull-right">\r\n            <input placeholder=" Search Products" id="search"/>\r\n        </div>\r\n\r\n        <ul id="product_list">\r\n')
        for product in products:
            __M_writer('            <li>\r\n                <div>\r\n                    <img class="description product-image" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('retail/media/')
            __M_writer(str( product.name ))
            __M_writer('.jpg/">\r\n                </div>\r\n                <div>\r\n                    <a href="/retail/product.detail/')
            __M_writer(str( product.id ))
            __M_writer('/">')
            __M_writer(str( product.name ))
            __M_writer('</a>\r\n                </div>\r\n                    <p>$')
            __M_writer(str( product.price ))
            __M_writer('</p>\r\n')
            __M_writer('            </li>\r\n')
        __M_writer('        </ul>\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 24, "65": 24, "66": 24, "27": 0, "36": 1, "69": 32, "68": 26, "76": 70, "70": 34, "46": 3, "67": 26, "54": 3, "55": 9, "56": 12, "57": 18, "58": 19, "59": 21, "60": 21, "61": 21, "62": 21, "63": 24}, "uri": "product.html", "source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.html"}
__M_END_METADATA
"""
