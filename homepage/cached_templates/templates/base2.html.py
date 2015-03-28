# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423359283.01382
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/base2.html'
_template_uri = 'base2.html'
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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n        <header>\r\n            <link rel="icon" type="image/x-icon" href="/static/homepage/media/colonial_flag.jpg" />\r\n            <div id="div-head"></div>\r\n            <div class="container-fluid">\r\n                <div class="col-xs-3" >\r\n                    <img src="/static/homepage/media/ch_logo.png" height="75">\r\n                </div>\r\n                <div class="col-xs-4"></div>\r\n                <div class="col-xs-5" style="text-align: right;margin-top: 20px">\r\n                    <ul class="nav nav-tabs">\r\n                        <li role="menu"><a href="/homepage/index/">Home</a></li>\r\n                        <li role="person"><a href="/homepage/person/">Contacts</a></li>\r\n                        <li role="phone"><a href="/homepage/phone/">Phone List</a></li>\r\n                        <li role="venue"><a href="/homepage/venue/">Venues</a></li>\r\n                        <li role="menu"><a href="/homepage/item/">Inventory</a></li>\r\n                        <li role="logout"><a class="btn btn-danger" href="/homepage/logout/">Log Out</a></li>\r\n                    </ul>\r\n                </div>\r\n            </div>\r\n            <div style="background-color: #A41425; height: 2px"></div>\r\n        </header>\r\n\r\n')
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
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"56": 50, "34": 1, "27": 0, "44": 24, "50": 24}, "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/base2.html", "source_encoding": "ascii", "uri": "base2.html"}
__M_END_METADATA
"""
