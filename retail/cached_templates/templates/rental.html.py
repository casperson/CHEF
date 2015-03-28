# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427257768.086595
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/rental.html'
_template_uri = 'rental.html'
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
        rentableitems = context.get('rentableitems', UNDEFINED)
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
        rentableitems = context.get('rentableitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <h3 style="text-decoration: underline">Rentable Items</h3>\r\n\r\n        <form id="search" method="post" action="rental.search">\r\n            <input type="text" placeholder=" Search"/>\r\n        </form>\r\n\r\n        <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n            <tr>\r\n                <th>Rentable Item ID</th>\r\n                <th>Name</th>\r\n                <th>Description</th>\r\n                <th>Rental Price</th>\r\n                <th>Price Per Day</th>\r\n                <th></th>\r\n            </tr>\r\n')
        for RentableItem in rentableitems:
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(str( RentableItem.id ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( RentableItem.name ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( RentableItem.description ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( RentableItem.rental_price ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( RentableItem.price_per_day ))
            __M_writer('</td>\r\n')
            __M_writer('                    <td>\r\n                        <a data-pid="')
            __M_writer(str( RentableItem.id ))
            __M_writer('"  class="btn btn-warning shopping_cart_dialog3">Add To Cart</a>\r\n                    </td>\r\n')
            __M_writer('                </tr>\r\n')
        __M_writer('        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 27, "65": 29, "66": 30, "67": 30, "68": 39, "69": 41, "75": 69, "27": 0, "35": 1, "45": 3, "52": 3, "53": 21, "54": 22, "55": 23, "56": 23, "57": 24, "58": 24, "59": 25, "60": 25, "61": 26, "62": 26, "63": 27}, "uri": "rental.html", "source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/rental.html"}
__M_END_METADATA
"""
