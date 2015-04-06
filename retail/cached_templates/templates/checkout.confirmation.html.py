# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428210393.172128
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/checkout.confirmation.html'
_template_uri = 'checkout.confirmation.html'
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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        total = context.get('total', UNDEFINED)
        today = context.get('today', UNDEFINED)
        rentalitems = context.get('rentalitems', UNDEFINED)
        user = context.get('user', UNDEFINED)
        resp = context.get('resp', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        subtotal = context.get('subtotal', UNDEFINED)
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
        def content_center():
            return render_content_center(context)
        total = context.get('total', UNDEFINED)
        today = context.get('today', UNDEFINED)
        rentalitems = context.get('rentalitems', UNDEFINED)
        user = context.get('user', UNDEFINED)
        resp = context.get('resp', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        subtotal = context.get('subtotal', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <div class="email-header">\r\n            <p class="col-md-6"></p>\r\n            <h2 class="col-md-3 right-align">Order Confirmation</h2>\r\n        </div>\r\n        <div class="email-body">\r\n            <h3>Success!</h3>\r\n            <p>Thank you for shopping with us ')
        __M_writer(str( user.first_name ))
        __M_writer('. Below are the details for your purchase on ')
        __M_writer(str( today ))
        __M_writer('.</p>\r\n            <h3>Details</h3>\r\n            <p>Order #: ')
        __M_writer(str( resp["ID"] ))
        __M_writer('</p>\r\n        </div>\r\n        <h3>Sale Items</h3>\r\n        <table class="table table-condensed receipt-table">\r\n            <thead>\r\n                <tr>\r\n                    <th>Photo</th>\r\n                    <th>Name</th>\r\n                    <th>Description</th>\r\n                    <th>Quantity</th>\r\n                    <th>Price</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for lineitem in lineitems:
            __M_writer('                <tr>\r\n                    <td><img style="max-width: 150px;" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('retail/media/')
            __M_writer(str( lineitem.product_name() ))
            __M_writer('.jpg/"\r\n                         alt="Picture" class="description"/>\r\n                    </td>\r\n                    <td>')
            __M_writer(str( lineitem.product_name() ))
            __M_writer(' </td>\r\n                    <td>')
            __M_writer(str( lineitem.product.description ))
            __M_writer(' </td>\r\n                    <td><input class="col-md-2" type="text"  value="')
            __M_writer(str( lineitem.quantity ))
            __M_writer('" disabled/></td>\r\n                    <td><input class="col-md-3" type="text" value="')
            __M_writer(str( lineitem.product_price() ))
            __M_writer('" disabled/></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n          </table>\r\n\r\n        <br/>\r\n            <h3>Rental Items</h3>\r\n            <table class="table table-condensed receipt-table">\r\n            <thead>\r\n                <tr>\r\n                    <th>Photo</th>\r\n                    <th>Name</th>\r\n                    <th>Description</th>\r\n                    <th>Quantity</th>\r\n                    <th>Price</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for rentalitem in rentalitems:
            __M_writer('                    <tr>\r\n                        <td><img style="max-width: 150px;" src=""\r\n                             alt="Picture" class="description"/>\r\n                        </td>\r\n                        <td>')
            __M_writer(str( rentalitem.rental_item_name() ))
            __M_writer(' </td>\r\n                        <td>')
            __M_writer(str( rentalitem.rental_item_description() ))
            __M_writer(' </td>\r\n                        <td><input class="col-md-2" type="text"  value="')
            __M_writer(str( rentalitem.quantity ))
            __M_writer('" disabled/></td>\r\n                        <td><input class="col-md-3" type="text" value="')
            __M_writer(str( rentalitem.rental_item_price() ))
            __M_writer('" disabled/></td>\r\n                    </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n        <div class="right-align receipt">\r\n            <p>Subtotal: $ ')
        __M_writer(str( subtotal ))
        __M_writer('</p>\r\n            <p>Tax (6.5%): $ ')
        __M_writer(str( tax ))
        __M_writer('</p>\r\n            <p  class="receipt">Total: $ ')
        __M_writer(str( total ))
        __M_writer('</p>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "checkout.confirmation.html", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/checkout.confirmation.html", "source_encoding": "ascii", "line_map": {"68": 3, "69": 11, "70": 11, "71": 11, "72": 11, "73": 13, "74": 13, "75": 27, "76": 28, "77": 29, "78": 29, "79": 29, "80": 29, "81": 32, "82": 32, "83": 33, "84": 33, "85": 34, "86": 34, "87": 35, "88": 35, "89": 38, "90": 54, "27": 0, "92": 59, "93": 59, "94": 60, "95": 60, "96": 61, "97": 61, "98": 62, "91": 55, "100": 65, "101": 68, "102": 68, "103": 69, "104": 69, "105": 70, "106": 70, "43": 1, "99": 62, "112": 106, "53": 3}}
__M_END_METADATA
"""
