# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428647228.755933
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/base.loginform.html'
_template_uri = 'base.loginform.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <form class="form-horizontal" id="loginform" method="POST" action="/base.loginform/">\r\n        <table>\r\n')
        for field in form:
            __M_writer('                <div class="form-group">\r\n                    <label for="id_')
            __M_writer(str(field.name))
            __M_writer('" class="col-sm-3 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\r\n                    <div class="col-sm-9">\r\n                        ')
            __M_writer(str(field))
            __M_writer('\r\n                    </div>\r\n                </div>\r\n')
        __M_writer('            <div class="form-group">\r\n                <div class="col-sm-offset-7 col-sm-5">\r\n                    <a href="/password_reset/">Forgot Password?</a>\r\n                </div>\r\n            </div>\r\n            <div class="form-group">\r\n                <div class="col-sm-12">\r\n                    <button class="btn btn-success btn-block" type="submit">Login</button>\r\n                </div>\r\n            </div>\r\n        </table>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/base.loginform.html", "line_map": {"35": 1, "45": 3, "27": 0, "67": 61, "52": 3, "53": 7, "54": 8, "55": 9, "56": 9, "57": 9, "58": 9, "59": 11, "60": 11, "61": 15}, "source_encoding": "ascii", "uri": "base.loginform.html"}
__M_END_METADATA
"""
