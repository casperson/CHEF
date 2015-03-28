# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423365680.511335
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/item.html'
_template_uri = 'item.html'
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
    return runtime._inherit_from(context, 'base2.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <h2 style="text-decoration: underline">Inventory</h2>\r\n        <ul class="nav nav-tabs" style="background-color: white">\r\n            <li role="menu"><a href="/homepage/item/" style="font-size: medium">View Items</a></li>\r\n            <li role="menu"><a href="/homepage/retail/" style="font-size: medium">View Products</a></li>\r\n        </ul>\r\n\r\n        <a href="/homepage/item.create/" class="btn btn-success">Add New Item</a>\r\n\r\n        <h3 style="text-decoration: underline">Item List</h3>\r\n\r\n        <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n            <thead>\r\n                <th>Item ID</th>\r\n                <th>Name</th>\r\n                <th>Description</th>\r\n                <th>Value</th>\r\n                <th>Rental Price</th>\r\n                <th>Edit/Delete</th>\r\n            </thead>\r\n            <tbody>\r\n')
        for item in items:
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(str( item.id))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( item.name ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( item.description ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( item.value ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( item.standard_rental_price ))
            __M_writer('</td>\r\n                    <td>\r\n                        <div class="btn-group" role="group" aria-label="...">\r\n                        <a type="button" class="btn btn-default" href="/homepage/item.edit/')
            __M_writer(str( item.id ))
            __M_writer('/"><i class="fa fa-edit"></i></a>\r\n                        <button type="button" data-toggle="modal" data-target="#form-modal" class="btn btn-danger"><i class="fa fa-trash"></i></button>\r\n                        <div class="modal fade" id="form-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                            <div class="modal-dialog">\r\n                                <div class="modal-content">\r\n                                    <div class="modal-header">\r\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                                        <h4 class="modal-title">Delete Warning</h4>\r\n                                    </div>\r\n                                    <div id="form-modal-body" class="modal-body">\r\n                                        <p>Are you sure you want to delete ')
            __M_writer(str( item.name ))
            __M_writer('</p>\r\n                                    </div>\r\n                                    <div class="modal-footer">\r\n                                        <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                                        <a href="/homepage/item.delete/')
            __M_writer(str( item.id ))
            __M_writer('/" class="btn btn-danger">Delete</a>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                    </td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "item.html", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/item.html", "line_map": {"64": 32, "65": 35, "66": 35, "67": 45, "68": 45, "69": 49, "70": 49, "71": 58, "77": 71, "27": 0, "35": 1, "45": 3, "52": 3, "53": 26, "54": 27, "55": 28, "56": 28, "57": 29, "58": 29, "59": 30, "60": 30, "61": 31, "62": 31, "63": 32}}
__M_END_METADATA
"""
