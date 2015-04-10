# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428641235.288654
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\account\\templates/user.html'
_template_uri = 'user.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="clearfix"></div>\r\n    <br/>\r\n    <h2 style="text-decoration: underline">Users</h2>\r\n    <div class="text-right">\r\n        <button id="create_account_btn" class="btn btn-warning UserCreate">Add User</button>\r\n    </div>\r\n    <br/>\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <th>First Name</th>\r\n            <th>Last Name</th>\r\n            <th>Username</th>\r\n            <th>Email</th>\r\n')
        __M_writer('            <th>Phone Number</th>\r\n            <th>Security Question</th>\r\n            <th>Security Answer</th>\r\n            <th>Edit | Delete</th>\r\n        </tr>\r\n')
        for user in users:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.username))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\r\n')
            __M_writer('                <td>')
            __M_writer(str( user.phone ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.security_question ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( user.security_answer ))
            __M_writer('</td>\r\n                <td>\r\n                    <div class="btn-group"  role="group" aria-label="...">\r\n                        <button data-pid="')
            __M_writer(str( user.id ))
            __M_writer('" type="button"  class="btn btn-default UserEdit"><i class="fa fa-edit"></i></button>\r\n                        <button data-pid="')
            __M_writer(str( user.id ))
            __M_writer('" type="button" class="btn btn-danger DeleteUser"><i class="fa fa-trash "></i></button>\r\n\r\n')
            __M_writer('\r\n                    </div>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "user.html", "line_map": {"64": 35, "65": 35, "66": 35, "67": 36, "68": 36, "69": 37, "70": 37, "71": 40, "72": 40, "73": 41, "74": 41, "75": 61, "76": 66, "82": 76, "27": 0, "35": 1, "45": 2, "52": 2, "53": 20, "54": 25, "55": 26, "56": 27, "57": 27, "58": 28, "59": 28, "60": 29, "61": 29, "62": 30, "63": 30}, "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\account\\templates/user.html"}
__M_END_METADATA
"""
