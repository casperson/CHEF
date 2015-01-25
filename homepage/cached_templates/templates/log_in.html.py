# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422139657.64808
_enable_loop = True
_template_filename = 'C:\\Users\\Garrett\\PycharmProjects\\CHEF\\homepage\\templates/log_in.html'
_template_uri = 'log_in.html'
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
        __M_writer('\r\n    <div class="container-fluid">\r\n\r\n        <form class="form-horizontal">\r\n         <div style="margin-top: 20px" class="form-group">\r\n            <label for="inputUserName3" class="col-sm-2 control-label">User Name</label>\r\n            <div class="col-sm-5">\r\n              <input type="userName" class="form-control" id="inputUserName3" placeholder="UserName">\r\n            </div>\r\n         </div>\r\n          <div class="form-group">\r\n            <label for="inputPassword3" class="col-sm-2 control-label">Password</label>\r\n            <div class="col-sm-5">\r\n              <input type="password" class="form-control" id="inputPassword3" placeholder="Password">\r\n            </div>\r\n          </div>\r\n          <div class="form-group">\r\n            <div class="col-sm-offset-2 col-sm-10">\r\n              <div class="checkbox">\r\n                <label>\r\n                  <input type="checkbox"> Remember me\r\n                </label>\r\n              </div>\r\n            </div>\r\n          </div>\r\n          <div class="form-group">\r\n            <div class="col-sm-offset-2 col-sm-10">\r\n              <button type="submit" class="btn btn-default">Sign in</button>\r\n            </div>\r\n          </div>\r\n        </form>\r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Garrett\\PycharmProjects\\CHEF\\homepage\\templates/log_in.html", "source_encoding": "ascii", "uri": "log_in.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
