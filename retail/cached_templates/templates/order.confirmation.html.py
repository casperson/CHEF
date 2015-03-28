# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427242721.504928
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/order.confirmation.html'
_template_uri = 'order.confirmation.html'
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
        __M_writer('\r\n    <div>\r\n        <div class="email-header">\r\n            <img class="col-md-3" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/ch_logo.png" alt="Colonial Heritage Foundation"/>\r\n            <p class="col-md-6"></p>\r\n            <h2 class="col-md-3 right-align">Order Confirmation</h2>\r\n        </div>\r\n        <div class="email-body">\r\n            <h3>Hello Daniel,</h3>\r\n            <p>Thank you for shopping with us. Below are the details for your purchase on 3/18/2015.</p>\r\n            <h3>Details</h3>\r\n            <p>Order #: 1996482235</p>\r\n        </div>\r\n        <table class="table table-condensed receipt-table">\r\n            <thead>\r\n                <tr>\r\n                    <th>Photo</th>\r\n                    <th>Name</th>\r\n')
        __M_writer('                    <th>Quantity</th>\r\n                    <th>Price</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for product in products:
            __M_writer('                <tr>\r\n                    <td><img style="max-width: 150px;" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('retail/media/')
            __M_writer(str( product.name ))
            __M_writer('.jpg/"\r\n                         alt="Picture" class="description"/>\r\n                    </td>\r\n                    <td>')
            __M_writer(str(product.name))
            __M_writer(' </td>\r\n')
            __M_writer('                    <td><input class="col-md-2" type="text"  value="1" disabled/></td>\r\n                    <td><input class="col-md-3" type="text" value="')
            __M_writer(str(product.price))
            __M_writer('" disabled/></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n        <div class="right-align receipt">\r\n            <p>Subtotal: $345.00</p>\r\n            <p>Tax (6.5%): $22.43</p>\r\n            <p  class="receipt">Total: $367.43</p>\r\n        </div>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/order.confirmation.html", "uri": "order.confirmation.html", "line_map": {"64": 32, "65": 32, "66": 34, "27": 0, "36": 1, "69": 38, "68": 35, "75": 69, "46": 3, "67": 35, "54": 3, "55": 6, "56": 6, "57": 22, "58": 27, "59": 28, "60": 29, "61": 29, "62": 29, "63": 29}, "source_encoding": "ascii"}
__M_END_METADATA
"""
