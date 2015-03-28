# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426738291.02593
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\account\\templates/account.html'
_template_uri = 'account.html'
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
    return runtime._inherit_from(context, 'homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        lineitems = context.get('lineitems', UNDEFINED)
        user = context.get('user', UNDEFINED)
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
        lineitems = context.get('lineitems', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <h2 style="text-decoration: underline">My Account</h2>\r\n    <p>Login Successful!</p>\r\n        <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <th>First Name</th>\r\n            <th>Last Name</th>\r\n            <th>Username</th>\r\n            <th>Email</th>\r\n')
        __M_writer('            <th>Phone Number</th>\r\n            <th>Security Question</th>\r\n            <th>Security Answer</th>\r\n            <th>Edit | Delete</th>\r\n        </tr>\r\n            <tr>\r\n                <td>')
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
        __M_writer('/" type="button" id="user_edit" data-pid="')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-default"><i class="fa fa-edit"></i></a>\r\n                        <button type="button" data-toggle="modal" data-target="#form-modal" class="btn btn-danger"><i class="fa fa-trash"></i></button>\r\n                        <div class="modal fade" id="form-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                            <div class="modal-dialog">\r\n                                <div class="modal-content">\r\n                                    <div class="modal-header">\r\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                                        <h4 class="modal-title">Delete Warning</h4>\r\n                                    </div>\r\n                                    <div id="form-modal-body" class="modal-body">\r\n                                        <p>Are you sure you want to delete ')
        __M_writer(str( user.first_name ))
        __M_writer('</p>\r\n                                    </div>\r\n                                    <div class="modal-footer">\r\n                                        <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                                        <a href="/account/user.delete/')
        __M_writer(str( user.id ))
        __M_writer('/" class="btn btn-danger">Delete</a>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </td>\r\n            </tr>\r\n    </table>\r\n    <button id="change_password_dialog" class="btn btn-warning">Change Password</button>\r\n    <br/><br/>\r\n    <h2>My Rentals</h2>\r\n    <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>Quantity</th>\r\n            <th>Rental Price</th>\r\n            <th>Price Per Day</th>\r\n            <th>Date Due</th>\r\n        </tr>\r\n')
        for lineitem in lineitems:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( lineitem.rental_line_item.rentable_item.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.quantity ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.rental_line_item.rentable_item.rental_price ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.rental_line_item.rentable_item.price_per_day ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( lineitem.rental_line_item.date_due ))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 30, "65": 30, "66": 30, "67": 31, "68": 31, "69": 32, "70": 32, "71": 35, "72": 35, "73": 35, "74": 35, "75": 45, "76": 45, "77": 49, "78": 49, "79": 69, "80": 70, "81": 71, "82": 71, "83": 72, "84": 72, "85": 73, "86": 73, "87": 74, "88": 74, "89": 75, "90": 75, "27": 0, "97": 91, "91": 78, "36": 1, "46": 2, "54": 2, "55": 16, "56": 22, "57": 22, "58": 23, "59": 23, "60": 24, "61": 24, "62": 25, "63": 25}, "source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\account\\templates/account.html", "uri": "account.html"}
__M_END_METADATA
"""
