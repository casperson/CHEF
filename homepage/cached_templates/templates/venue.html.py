# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423376150.67836
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/venue.html'
_template_uri = 'venue.html'
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
        venues = context.get('venues', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        venues = context.get('venues', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <h2 style="text-decoration: underline">Venues</h2>\r\n    <div class="clearfix"></div>\r\n    <div class="text-right">\r\n        <a href="/homepage/venue.create/" class="btn btn-success">Add New Venue</a>\r\n    </div>\r\n\r\n    <table class="table table-stripped table-bordered">\r\n        <tr>\r\n            <th>ID</th>\r\n            <th>Name</th>\r\n            <th>Address</th>\r\n            <th>City</th>\r\n            <th>State</th>\r\n            <th>ZIP</th>\r\n            <th>Edit/Delete</th>\r\n        </tr>\r\n')
        for venue in venues:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( venue.id ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( venue.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( venue.address ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( venue.city ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( venue.state ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( venue.zip ))
            __M_writer('</td>\r\n                <td>\r\n                    <div class="btn-group" role="group" aria-label="...">\r\n                        <a type="button" class="btn btn-default" href="/homepage/venue.edit/')
            __M_writer(str( venue.id ))
            __M_writer('/"><i class="fa fa-edit"></i></a>\r\n                        <button type="button" data-toggle="modal" data-target="#form-modal" class="btn btn-danger"><i class="fa fa-trash"></i></button>\r\n                        <div class="modal fade" id="form-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                            <div class="modal-dialog">\r\n                                <div class="modal-content">\r\n                                    <div class="modal-header">\r\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                                        <h4 class="modal-title">Delete Warning</h4>\r\n                                    </div>\r\n                                    <div id="form-modal-body" class="modal-body">\r\n                                        <p>Are you sure you want to delete ')
            __M_writer(str( venue.name ))
            __M_writer('</p>\r\n                                    </div>\r\n                                    <div class="modal-footer">\r\n                                        <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                                        <a href="/homepage/venue.delete/')
            __M_writer(str( venue.id ))
            __M_writer('/" class="btn btn-danger">Delete</a>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "venue.html", "line_map": {"64": 26, "65": 27, "66": 27, "67": 30, "68": 30, "69": 40, "70": 40, "71": 44, "72": 44, "73": 53, "79": 73, "27": 0, "35": 1, "45": 2, "52": 2, "53": 20, "54": 21, "55": 22, "56": 22, "57": 23, "58": 23, "59": 24, "60": 24, "61": 25, "62": 25, "63": 26}, "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/venue.html"}
__M_END_METADATA
"""
