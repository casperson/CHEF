# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428001216.379685
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.shoppingcart.html'
_template_uri = 'product.shoppingcart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        lineitems = context.get('lineitems', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentalitems = context.get('rentalitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('retail/scripts/product.shoppingcart.js"></script>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        lineitems = context.get('lineitems', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentalitems = context.get('rentalitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div id="shoppingcartform">\r\n        <h3>Sale Items</h3>\r\n        <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n            <thead>\r\n                <th>Picture</th>\r\n                <th>Name</th>\r\n                <th>Price</th>\r\n                <th>Quantity</th>\r\n                <th>Delete</th>\r\n            </thead>\r\n            <tbody>\r\n')
        for lineitem in lineitems:
            __M_writer('                <tr>\r\n                    <div>\r\n                        <td> <img class="description" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('retail/media/')
            __M_writer(str( lineitem.product_name() ))
            __M_writer('.jpg/"></td>\r\n                    </div>\r\n                    <td>')
            __M_writer(str( lineitem.product_name() ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( lineitem.product_price() ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( lineitem.quantity ))
            __M_writer('</td>\r\n                    <td>\r\n                        <div class="btn-group" role="group" aria-label="...">\r\n                        <a type="button" class="btn btn-default" href="/retail/product.edit_line_item/')
            __M_writer(str( lineitem.id ))
            __M_writer('/"><i class="fa fa-edit"></i></a>\r\n')
            __M_writer('                        <button data-pid="')
            __M_writer(str( lineitem.id ))
            __M_writer('"  class="btn btn-danger delete_line_item">Delete</button>\r\n')
            __M_writer('                        </div>\r\n                    </td>\r\n                </tr>\r\n')
        __M_writer('        </table>\r\n        <br/><br/>\r\n    <h3>Rental Items</h3>\r\n        <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n            <thead>\r\n                <th>id</th>\r\n                <th>Rental Item Name</th>\r\n                <th>Price</th>\r\n                <th>Quantity</th>\r\n                <th>Delete</th>\r\n            </thead>\r\n            <tbody>\r\n')
        for rentalitem in rentalitems:
            __M_writer('                <tr>\r\n                    <th>')
            __M_writer(str( rentalitem.id ))
            __M_writer('</th>\r\n                    <td>')
            __M_writer(str( rentalitem.rental_item_name() ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( rentalitem.rental_item_price() ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( rentalitem.quantity ))
            __M_writer('</td>\r\n                    <td>\r\n                        <div class="btn-group" role="group" aria-label="...">\r\n                        <a type="button" class="btn btn-default" href="/retail/product.edit_line_item/')
            __M_writer(str( rentalitem.id ))
            __M_writer('/"><i class="fa fa-edit"></i></a>\r\n')
            __M_writer('                        <button data-rid="')
            __M_writer(str( rentalitem.id ))
            __M_writer('"  class="btn btn-danger delete_rental_item">Delete</button>\r\n')
            __M_writer('                        </div>\r\n                    </td>\r\n                </tr>\r\n')
        __M_writer('        </table>\r\n\r\n        <a href="/retail/checkout.checkout/" type="submit" class="btn btn-warning">Checkout</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.shoppingcart.html", "line_map": {"64": 21, "65": 23, "66": 23, "67": 24, "68": 24, "69": 25, "70": 25, "71": 28, "72": 28, "73": 30, "74": 30, "75": 30, "76": 48, "77": 52, "78": 64, "79": 65, "80": 66, "81": 66, "82": 67, "83": 67, "84": 68, "85": 68, "86": 69, "87": 69, "88": 72, "89": 72, "90": 74, "27": 0, "92": 74, "93": 92, "94": 96, "91": 74, "100": 94, "37": 1, "38": 4, "39": 4, "49": 5, "58": 5, "59": 18, "60": 19, "61": 21, "62": 21, "63": 21}, "uri": "product.shoppingcart.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
