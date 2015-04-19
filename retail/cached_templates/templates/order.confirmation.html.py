# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428660626.460792
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/order.confirmation.html'
_template_uri = 'order.confirmation.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rentalitems = context.get('rentalitems', UNDEFINED)
        total = context.get('total', UNDEFINED)
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        resp = context.get('resp', UNDEFINED)
        today = context.get('today', UNDEFINED)
        subtotal = context.get('subtotal', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        __M_writer = context.writer()
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentalitems = context.get('rentalitems', UNDEFINED)
        total = context.get('total', UNDEFINED)
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context)
        resp = context.get('resp', UNDEFINED)
        today = context.get('today', UNDEFINED)
        subtotal = context.get('subtotal', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <div class="email-header">\r\n            <p class="col-md-6"></p>\r\n            <h2 class="col-md-3 right-align">Order Confirmation</h2>\r\n        </div>\r\n        <div class="email-body">\r\n            <h3>Hello ')
        __M_writer(str( user.first_name ))
        __M_writer(',</h3>\r\n            <p>Thank you for shopping with us. Below are the details for your purchase on ')
        __M_writer(str( today ))
        __M_writer('.</p>\r\n            <h3>Details</h3>\r\n            <p>Order #: ')
        __M_writer(str( resp['ID'] ))
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
            __M_writer(' </td>\r\n                    <td><input class="col-md-2" type="text"  value="1" disabled/></td>\r\n                    <td><input class="col-md-3" type="text" value="')
            __M_writer(str( lineitem.product_price() ))
            __M_writer('" disabled/></td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n          </table>\r\n\r\n        <br/>\r\n            <h3>Rental Items</h3>\r\n            <table class="table table-condensed receipt-table">\r\n            <thead>\r\n                <tr>\r\n                    <th>Photo</th>\r\n                    <th>Name</th>\r\n                    <th>Description</th>\r\n                    <th>Quantity</th>\r\n                    <th>Price</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for rentalitem in rentalitems:
            __M_writer('                    <tr>\r\n                        <td><img style="max-width: 150px;" src=""\r\n                             alt="Picture" class="description"/>\r\n                        </td>\r\n                        <td>')
            __M_writer(str( rentalitem.rental_item_name() ))
            __M_writer(' </td>\r\n                        <td>')
            __M_writer(str( rentalitem.rental_item_description() ))
            __M_writer(' </td>\r\n                        <td><input class="col-md-2" type="text"  value="1" disabled/></td>\r\n                        <td><input class="col-md-3" type="text" value="')
            __M_writer(str( rentalitem.rental_item_price() ))
            __M_writer('" disabled/></td>\r\n                    </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n        <div class="right-align receipt">\r\n            <p>Subtotal: $')
        __M_writer(str( subtotal ))
        __M_writer('</p>\r\n            <p>Tax (6.5%): $')
        __M_writer(str( tax ))
        __M_writer('</p>\r\n            <p  class="receipt">Total: $')
        __M_writer(str( total ))
        __M_writer('</p>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/order.confirmation.html", "source_encoding": "ascii", "uri": "order.confirmation.html", "line_map": {"64": 26, "65": 27, "66": 27, "67": 27, "68": 27, "69": 30, "70": 30, "71": 31, "72": 31, "73": 33, "74": 33, "75": 36, "76": 52, "77": 53, "78": 57, "79": 57, "16": 0, "81": 58, "82": 60, "83": 60, "84": 63, "85": 66, "86": 66, "87": 67, "88": 67, "89": 68, "90": 68, "96": 90, "80": 58, "41": 1, "56": 1, "57": 8, "58": 8, "59": 9, "60": 9, "61": 11, "62": 11, "63": 25}}
__M_END_METADATA
"""
