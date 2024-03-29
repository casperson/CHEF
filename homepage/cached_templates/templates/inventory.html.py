# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428536033.509194
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/inventory.html'
_template_uri = 'inventory.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <h2 style="text-decoration: underline">Inventory</h2>\r\n        <ul class="nav nav-tabs" style="background-color: white">\r\n            <li role="menu"><a href="/homepage/item/">Item</a></li>\r\n            <li role="menu"><a href="/homepage/product/">Product</a></li>\r\n        </ul>\r\n\r\n        <button class="btn btn-success" href="#addItem" style="margin: 5px 0px 15px 0px;" type="button" data-toggle="modal" data-target="#form-modal" >Add item</button>\r\n        <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n            <thead>\r\n                <th>Name</th>\r\n                <th>Description</th>\r\n                <th>Value</th>\r\n                <th>Rental Price</th>\r\n                <th>Edit/Delete</th>\r\n            </thead>\r\n            <tbody>\r\n')
        for item in items:
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(str( item.name ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( item.description ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( item.value ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( item.standard_rental_price ))
            __M_writer('</td>\r\n                    <td>\r\n                        <div class="btn-group" role="group" aria-label="...">\r\n                            <button type="button" class="btn btn-default"><i class="fa fa-edit"></i></button>\r\n                            <button type="button" class="btn btn-danger"><i class="fa fa-trash"></i></button>\r\n                        </div>\r\n                    </td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n    </div>\r\n    <div class="modal fade" id="form-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n        <div class="modal-dialog">\r\n          <div class="modal-content">\r\n            <div class="modal-header">\r\n              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n              <h4 class="modal-title">Add Item</h4>\r\n            </div>\r\n            <div id="form-modal-body" class="modal-body">\r\n                <form>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputName">Name</label>\r\n                    <input type="name" class="form-control" id="exampleName" placeholder="Enter name">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Description</label>\r\n                    <input type="description" class="form-control" id="exampleInputDescription" placeholder="Description">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Value</label>\r\n                    <input type="value" class="form-control" id="exampleInputValue" placeholder="Value">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Rental Price</label>\r\n                    <input type="rentalprice" class="form-control" id="exampleInputrentalprice" placeholder="Rental Price">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Size</label>\r\n                    <input type="size" class="form-control" id="exampleInputSize" placeholder="Size">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Size Modifier</label>\r\n                    <input type="sizeModifier" class="form-control" id="exampleInputSizeModifier" placeholder="Size Modifier">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Gender</label>\r\n                    <input type="Gender" class="form-control" id="exampleInputGender" placeholder="Gender">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Color</label>\r\n                    <input type="color" class="form-control" id="exampleInputColor" placeholder="Color">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Pattern</label>\r\n                    <input type="pattern" class="form-control" id="exampleInputPattern" placeholder="Pattern">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Start Year</label>\r\n                    <input type="startYear" class="form-control" id="exampleInputStartYear" placeholder="Start Year">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">End Year</label>\r\n                    <input type="End Year" class="form-control" id="exampleInputEndYear" placeholder="End Year">\r\n                  </div>\r\n                  <div class="form-group">\r\n                    <label for="exampleInputDescription">Note</label>\r\n                    <input type="note" class="form-control" id="exampleInputNote" placeholder="Note">\r\n                  </div>\r\n\r\n                </form>\r\n           </div>\r\n           <div class="modal-footer">\r\n             <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n             <button type="submit" class="btn btn-default">Submit</button>\r\n           </div>\r\n         </div>\r\n       </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 22, "54": 23, "55": 24, "56": 24, "57": 25, "58": 25, "59": 26, "60": 26, "61": 27, "62": 27, "63": 36}, "uri": "inventory.html", "source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/inventory.html"}
__M_END_METADATA
"""
