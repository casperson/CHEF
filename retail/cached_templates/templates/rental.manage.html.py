# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428385416.244299
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/rental.manage.html'
_template_uri = 'rental.manage.html'
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
        lineitems = context.get('lineitems', UNDEFINED)
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
        lineitems = context.get('lineitems', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <h3 style="text-decoration: underline">Rented Items</h3>\r\n\r\n        <a href="/retail/product.overduereport/" class="btn btn-primary" pull-right>See All Overdue Rentals</a>\r\n        <br/><br/>\r\n        <form id="search" method="post" action="rental.search">\r\n            <input type="text" placeholder=" Search"/>\r\n        </form>\r\n        <br/>\r\n        <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>Quantity</th>\r\n            <th>Rental Price</th>\r\n            <th>Price Per Day</th>\r\n            <th>Date Due</th>\r\n            <th>Renter</th>\r\n            <th></th>\r\n        </tr>\r\n')
        for lineitem in lineitems:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( lineitem.rental_line_item.rentable_item.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.quantity ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.rental_line_item.rentable_item.rental_price ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.rental_line_item.rentable_item.price_per_day ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.rental_line_item.date_due ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.user.get_full_name() ))
            __M_writer('</td>\r\n                <td><button data-rid="')
            __M_writer(str( lineitem.rental_line_item.id ))
            __M_writer('" type="button" class="btn btn-success return_lineitem">Return Item</button></td>\r\n            </tr>\r\n')
        __M_writer('         </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rental.manage.html", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/rental.manage.html", "line_map": {"64": 30, "65": 31, "66": 31, "67": 32, "68": 32, "69": 35, "75": 69, "27": 0, "35": 1, "45": 3, "52": 3, "53": 24, "54": 25, "55": 26, "56": 26, "57": 27, "58": 27, "59": 28, "60": 28, "61": 29, "62": 29, "63": 30}, "source_encoding": "ascii"}
__M_END_METADATA
"""
