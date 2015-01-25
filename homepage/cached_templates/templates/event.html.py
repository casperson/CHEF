# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422149577.481725
_enable_loop = True
_template_filename = 'C:\\Users\\Garrett\\PycharmProjects\\CHEF\\homepage\\templates/event.html'
_template_uri = 'event.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n<h2 style="text-decoration: underline">Events</h2>\r\n    <div style="margin-top: 10px" class="container-fluid">\r\n\r\n        <div style="margin-top: 10px">\r\n\r\n           <button style="margin-bottom: 15px" type="submit" class="btn btn-success">Add Event</button>\r\n           <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n                <tr>\r\n                    <th>Event Name</th>\r\n                    <th>Location</th>\r\n                    <th>Event Area</th>\r\n                    <th>Description</th>\r\n                    <th>Start Date</th>\r\n                    <th>End Date</th>\r\n                    <th>Edit/Delete</th>\r\n                </tr>\r\n                <tr>\r\n                    <td>Colonial Festival</td>\r\n                    <td>Orem, UT</td>\r\n                    <td>Area 3</td>\r\n                    <td>The Foundation sponsors the Colonial Heritage Festival, the largest colonial living and reenactment event west of the Mississippi River.</td>\r\n                    <td>July 4th</td>\r\n                    <td>July 5th</td>\r\n                    <td>\r\n                        <div class="btn-group" role="group" aria-label="...">\r\n                            <button type="button" class="btn btn-default"><i class="fa fa-edit"></i></button>\r\n                            <button type="button" class="btn btn-danger"><i class="fa fa-trash"></i></button>\r\n                        </div>\r\n                    </td>\r\n                </tr>\r\n           </table>\r\n\r\n        </div>\r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Garrett\\PycharmProjects\\CHEF\\homepage\\templates/event.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "source_encoding": "ascii", "uri": "event.html"}
__M_END_METADATA
"""
