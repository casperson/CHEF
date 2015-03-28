# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426355148.503341
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.detail.html'
_template_uri = 'product.detail.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n            <thead>\r\n                <th>Picture</th>\r\n                <th>Name</th>\r\n                <th>Description</th>\r\n                <th>Price</th>\r\n                <th>Quantity Available</th>\r\n                <th>Quantity</th>\r\n                <th>Add to Cart</th>\r\n            </thead>\r\n            <tbody>\r\n')
        for product in products:
            __M_writer('                <tr>\r\n                    <div>\r\n                        <td> <img class="description" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('retail/media/')
            __M_writer(str( product.name ))
            __M_writer('.jpg/"></td>\r\n                    </div>\r\n                    <td>')
            __M_writer(str( product.name))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( product.description ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( product.price ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( product.qty_on_hand ))
            __M_writer('</td>\r\n                    <td> <input id="qty-input"/> </td>\r\n                    <td><button data-pid="')
            __M_writer(str( product.id ))
            __M_writer('" id="shopping_cart_dialog" class="btn btn-warning">Add to Cart</button></td>\r\n                 </tr>\r\n')
        __M_writer('        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.detail.html", "uri": "product.detail.html", "line_map": {"64": 23, "65": 24, "66": 24, "67": 25, "68": 25, "69": 27, "70": 27, "71": 30, "77": 71, "27": 0, "36": 1, "46": 3, "54": 3, "55": 17, "56": 18, "57": 20, "58": 20, "59": 20, "60": 20, "61": 22, "62": 22, "63": 23}}
__M_END_METADATA
"""
