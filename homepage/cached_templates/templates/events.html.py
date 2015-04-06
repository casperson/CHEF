# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428209475.682333
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div>\r\n        <h2 style="text-decoration: underline">Festivals</h2>\r\n\r\n    <div style="margin-top: 10px" class="container-fluid">\r\n\r\n        <div style="margin-top: 10px">\r\n            <p>\r\n                <a href="/homepage/events.create/" class="btn btn-success">Add New Festival</a>\r\n            </p>\r\n\r\n           <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n                <tr>\r\n                    <th>Event Name</th>\r\n                    <th>Description</th>\r\n                    <th>Start Date</th>\r\n                    <th>End Date</th>\r\n                    <th>Edit | Delete</th>\r\n                </tr>\r\n\r\n')
        for event in events:
            __M_writer('                        <tr>\r\n\r\n                            <td><a href="/homepage/events.details/')
            __M_writer(str( event.id ))
            __M_writer('"> ')
            __M_writer(str( event.name ))
            __M_writer('<a/> </td>\r\n                            <td>')
            __M_writer(str( event.description ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( event.start_date ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( event.end_date ))
            __M_writer('</td>\r\n                            <td>\r\n                                <div class="btn-group" role="group" aria-label="...">\r\n                                    <a href="/homepage/events.edit/')
            __M_writer(str( event.id ))
            __M_writer('" type="button" class="btn btn-default"><i class="fa fa-edit"></i></a>\r\n                                    <button type="button" data-toggle="modal" data-target="#form-modal" class="btn btn-danger"><i class="fa fa-trash"></i></button>\r\n                                    <div class="modal fade" id="form-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                                        <div class="modal-dialog">\r\n                                          <div class="modal-content">\r\n                                            <div class="modal-header">\r\n                                              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                                              <h4 class="modal-title">Delete Warning</h4>\r\n                                            </div>\r\n                                            <div id="form-modal-body" class="modal-body">\r\n                                                <p> Are you sure you want to DELETE "')
            __M_writer(str( event.name ))
            __M_writer('"</p>\r\n                                           </div>\r\n                                           <div class="modal-footer">\r\n                                             <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                                             <a href="/homepage/events.delete/')
            __M_writer(str( event.id ))
            __M_writer('" class="btn btn-danger">Delete</a>\r\n                                           </div>\r\n                                         </div>\r\n                                       </div>\r\n                                    </div>\r\n                                </div>\r\n                            </td>\r\n                        </tr>\r\n')
        __M_writer('\r\n\r\n           </table>\r\n\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.html", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/events.html", "line_map": {"64": 29, "65": 32, "66": 32, "67": 42, "68": 42, "69": 46, "70": 46, "71": 55, "77": 71, "27": 0, "35": 1, "45": 3, "52": 3, "53": 23, "54": 24, "55": 26, "56": 26, "57": 26, "58": 26, "59": 27, "60": 27, "61": 28, "62": 28, "63": 29}, "source_encoding": "ascii"}
__M_END_METADATA
"""
