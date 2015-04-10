# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428644212.687992
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
        __M_writer('\r\n<div>\r\n        <h2 style="text-decoration: underline">Festivals</h2>\r\n\r\n    <div style="margin-top: 10px" class="container-fluid">\r\n\r\n    <button id="create-event" class="btn btn-success">Add New Festival</button>\r\n        <br/>\r\n        <div style="margin-top: 10px">\r\n\r\n           <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n                <tr>\r\n                    <th>Event Name</th>\r\n                    <th>Description</th>\r\n                    <th>Start Date</th>\r\n                    <th>End Date</th>\r\n                    <th>Edit | Delete</th>\r\n                </tr>\r\n\r\n')
        for event in events:
            __M_writer('                        <tr>\r\n\r\n                            <td><a href="/homepage/events.details/')
            __M_writer(str( event.id ))
            __M_writer('"> ')
            __M_writer(str( event.name ))
            __M_writer('</a> </td>\r\n                            <td>')
            __M_writer(str( event.description ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( event.start_date ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( event.end_date ))
            __M_writer('</td>\r\n                            <td>\r\n                                <div class="btn-group" role="group" aria-label="...">\r\n                                    <button data-pid=')
            __M_writer(str( event.id ))
            __M_writer(' type="button" class="btn btn-default EventEditForm"><i class="fa fa-edit"></i></button>\r\n                                    <button data-eid=')
            __M_writer(str( event.id ))
            __M_writer(' type="button" class="btn btn-danger delete-event"><i class="fa fa-trash"></i></button>\r\n\r\n')
            __M_writer('\r\n                                </div>\r\n                            </td>\r\n                        </tr>\r\n')
        __M_writer('\r\n\r\n           </table>\r\n\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/events.html", "line_map": {"64": 28, "65": 31, "66": 31, "67": 32, "68": 32, "69": 52, "70": 57, "76": 70, "27": 0, "35": 1, "45": 3, "52": 3, "53": 22, "54": 23, "55": 25, "56": 25, "57": 25, "58": 25, "59": 26, "60": 26, "61": 27, "62": 27, "63": 28}, "uri": "events.html"}
__M_END_METADATA
"""
