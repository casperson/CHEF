# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422144332.44787
_enable_loop = True
_template_filename = 'C:\\Users\\Braden\\PycharmProjects\\CHEF\\homepage\\templates/inventory.html'
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
        __M_writer('\r\n    <div>\r\n        <table class="table table-striped">\r\n            <thead>\r\n                <th>Name</th>\r\n                <th>Description</th>\r\n                <th>Value</th>\r\n                <th>Standard Rental Price</th>\r\n                <th>Size</th>\r\n                <th>Size Modifier</th>\r\n                <th>Gender</th>\r\n                <th>Color</th>\r\n                <th>Pattern</th>\r\n                <th>Start Year</th>\r\n                <th>End Year</th>\r\n                <th>Note</th>\r\n            </thead>\r\n            <tbody>\r\n                <tr>\r\n                    <td>Blue Britches</td>\r\n                    <td>A pair of blue cotton britches</td>\r\n                    <td>$35.00</td>\r\n                    <td>$3.00</td>\r\n                    <td>M</td>\r\n                    <td>-</td>\r\n                    <td>Male</td>\r\n                    <td>Blue</td>\r\n                    <td>Striped</td>\r\n                    <td>1820</td>\r\n                    <td>1850</td>\r\n                </tr>\r\n            </tbody>\r\n        </table>\r\n        <div class="col-xs-8" style="margin-top: 10px"><img src="/static/homepage/media/colonial_flag.jpg" height="400"></div>\r\n        <div class="col-xs-2"></div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "inventory.html", "source_encoding": "ascii", "filename": "C:\\Users\\Braden\\PycharmProjects\\CHEF\\homepage\\templates/inventory.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
