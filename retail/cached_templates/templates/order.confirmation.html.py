# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428192575.459863
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
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        today = context.get('today', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
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
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context)
        today = context.get('today', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <div class="email-header">\r\n            <img class="col-md-3" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/ch_logo.png" alt="Colonial Heritage Foundation"/>\r\n            <p class="col-md-6"></p>\r\n            <h2 class="col-md-3 right-align">Order Confirmation</h2>\r\n        </div>\r\n        <div class="email-body">\r\n            <h3>Hello ')
        __M_writer(str( user.first_name ))
        __M_writer(',</h3>\r\n            <p>Thank you for shopping with us. Below are the details for your purchase on ')
        __M_writer(str( today ))
        __M_writer('.</p>\r\n            <h3>Details</h3>\r\n            <p>Order #: 1996482235</p>\r\n        </div>\r\n        <h3>Sale Items</h3>\r\n        <table class="table table-condensed receipt-table">\r\n            <thead>\r\n                <tr>\r\n                    <th>Photo</th>\r\n                    <th>Name</th>\r\n                    <th>Description</th>\r\n                    <th>Quantity</th>\r\n                    <th>Price</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
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
        __M_writer('            </tbody>\r\n        </table>\r\n        <div class="right-align receipt">\r\n            <p>Subtotal: $345.00</p>\r\n            <p>Tax (6.5%): $22.43</p>\r\n            <p  class="receipt">Total: $367.43</p>\r\n        </div>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 32, "65": 34, "66": 34, "67": 37, "68": 53, "69": 54, "70": 58, "71": 58, "72": 59, "73": 59, "74": 61, "75": 61, "76": 64, "16": 0, "82": 76, "37": 1, "48": 1, "49": 4, "50": 4, "51": 9, "52": 9, "53": 10, "54": 10, "55": 26, "56": 27, "57": 28, "58": 28, "59": 28, "60": 28, "61": 31, "62": 31, "63": 32}, "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/order.confirmation.html", "uri": "order.confirmation.html"}
__M_END_METADATA
"""
