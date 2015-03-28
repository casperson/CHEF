# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425790736.309317
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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
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
        def content_center():
            return render_content_center(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div class="clearfix"></div>\r\n    <div class="text-right">\r\n        <button id="create_account_btn" class="btn btn-warning">Add User</button>\r\n    </div>\r\n\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <th>First Name</th>\r\n            <th>Last Name</th>\r\n            <th>Username</th>\r\n            <th>Email</th>\r\n')
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
            __M_writer('</td>\r\n                <td>\r\n                    <div class="btn-group"  role="group" aria-label="...">\r\n                        <a href="/account/user.edit/')
            __M_writer(str( user.id ))
            __M_writer('/" type="button"  class="btn btn-default"><i class="fa fa-edit"></i></a>\r\n                        <button type="button" data-toggle="modal" data-target="#form-modal" class="btn btn-danger"><i class="fa fa-trash"></i></button>\r\n                        <div class="modal fade" id="form-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                            <div class="modal-dialog">\r\n                                <div class="modal-content">\r\n                                    <div class="modal-header">\r\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                                        <h4 class="modal-title">Delete Warning</h4>\r\n                                    </div>\r\n                                    <div id="form-modal-body" class="modal-body">\r\n                                        <p>Are you sure you want to delete ')
            __M_writer(str( user.first_name ))
            __M_writer('</p>\r\n                                    </div>\r\n                                    <div class="modal-footer">\r\n                                        <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                                        <a href="/account/user.delete/')
            __M_writer(str( user.id ))
            __M_writer('/" class="btn btn-danger">Delete</a>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\account\\templates/user.html", "source_encoding": "ascii", "uri": "user.html", "line_map": {"64": 34, "65": 34, "66": 34, "67": 35, "68": 35, "69": 36, "70": 36, "71": 39, "72": 39, "73": 49, "74": 49, "75": 53, "76": 53, "77": 62, "83": 77, "27": 0, "35": 1, "45": 2, "52": 2, "53": 19, "54": 24, "55": 25, "56": 26, "57": 26, "58": 27, "59": 27, "60": 28, "61": 28, "62": 29, "63": 29}}
__M_END_METADATA
"""
