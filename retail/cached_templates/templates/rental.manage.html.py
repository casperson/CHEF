# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426970950.690777
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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        lineitems = context.get('lineitems', UNDEFINED)
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
        lineitems = context.get('lineitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <h3 style="text-decoration: underline">Rented Items</h3>\r\n\r\n        <a href="/retail/rental.batch/" class="btn btn-primary" pull-right>See All Overdue Rentals</a>\r\n        <br/><br/>\r\n        <form id="search" method="post" action="rental.search">\r\n            <input type="text" placeholder=" Search"/>\r\n        </form>\r\n        <br/>\r\n        <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>Quantity</th>\r\n            <th>Rental Price</th>\r\n            <th>Price Per Day</th>\r\n            <th>Date Due</th>\r\n            <th></th>\r\n        </tr>\r\n')
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
            __M_writer('</td>\r\n')
            __M_writer('                <td>\r\n                    <div class="btn-group" role="group" aria-label="...">\r\n                        <button type="button" data-toggle="modal" data-target="#form-modal" class="btn btn-success">Return Item</button>\r\n                            <div class="modal fade" id="form-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                                <div class="modal-dialog">\r\n                                    <div class="modal-content">\r\n                                        <div class="modal-header">\r\n                                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                                            <h4 class="modal-title">Return Item</h4>\r\n                                        </div>\r\n                                        <div id="form-modal-body" class="modal-body">\r\n                                            <h2>Rental Item Information</h2>\r\n                                            <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n                                                <tr style="font-size: medium">\r\n                                                    <th>Name</th>\r\n                                                    <th>Quantity</th>\r\n                                                    <th>Price Per Day</th>\r\n                                                    <th>Date Due</th>\r\n                                                    <th>Days Late</th>\r\n                                                    <th></th>\r\n                                                </tr>\r\n                                                <tr style="font-size: medium">\r\n                                                    <td> Pistol </td>\r\n                                                    <td> 1 </td>\r\n                                                    <td> $3.00 </td>\r\n                                                    <td> 2015-04-20 </td>\r\n                                                    <td> 3 </td>\r\n                                                </tr>\r\n                                            </table>\r\n                                            <br/>\r\n                                            <h4>Sub Total: $9.00</h4>\r\n                                            <br/><h4>Condition When Rented:\r\n                                                <span style="color: darkgreen; font-weight: bold">Good</span>\r\n                                            </h4>\r\n                                            <h4>Condition When Returned:\r\n                                                <select>\r\n                                                    <option style="color: darkgreen" value="Good">Good</option>\r\n                                                    <option style="color: darkgoldenrod" value="OK">OK</option>\r\n                                                    <option style="color:orange;" value="Poor">Poor</option>\r\n                                                    <option style="color: #A41425" value="usable">Broken</option>\r\n                                                </select>\r\n                                            </h4>\r\n                                            <br/>\r\n                                            <h4 style="color: #A41425">Damage Fee:\r\n                                                <input type="text"/>\r\n                                            </h4>\r\n                                            <h3>Total Amount Due: $14.00</h3>\r\n                                        </div>\r\n                                        <div class="modal-footer">\r\n                                            <button type="button" class="btn btn-warning">Return and Add to Transaction</button>\r\n                                            <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                                        </div>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                    </div>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('         </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/rental.manage.html", "uri": "rental.manage.html", "source_encoding": "ascii", "line_map": {"64": 29, "65": 31, "66": 90, "35": 1, "72": 66, "45": 3, "27": 0, "52": 3, "53": 23, "54": 24, "55": 25, "56": 25, "57": 26, "58": 26, "59": 27, "60": 27, "61": 28, "62": 28, "63": 29}}
__M_END_METADATA
"""
