# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428446705.031858
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/check_rentals.html'
_template_uri = 'check_rentals.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        today = context.get('today', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        overdueItem = context.get('overdueItem', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        today = context.get('today', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        overdueItem = context.get('overdueItem', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <div class="email-header">\r\n            <img class="col-md-3" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/ch_logo.png" alt="Colonial Heritage Foundation"/>\r\n            <p class="col-md-3"></p>\r\n            <h2 class="col-md-6  right-align"><span style="color: red; font-weight: bold;">2</span> Overdue Items as of ')
        __M_writer(str( today ))
        __M_writer('</h2>\r\n        </div>\r\n        <div class="email-body">\r\n            <h3>Hello ')
        __M_writer(str( user.first_name ))
        __M_writer(',</h3>\r\n            <p>The following items are still rented out under your account and are now considered overdue. The items and their\r\n            corresponding fees are listed below.</p>\r\n            <p>Payment is due immediately.</p>\r\n            <h3>Overdue Items</h3>\r\n        </div>\r\n        <table class="table table-striped table-condensed receipt-table">\r\n            <thead>\r\n                <tr>\r\n                    <th>ID</th>\r\n                    <th>Item Name</th>\r\n                    <th>Date Due</th>\r\n                    <th>Days Late</th>\r\n                    <th>Current Fee Owed</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                <tr>\r\n                    <td>')
        __M_writer(str( overdueItem['id'] ))
        __M_writer('</td>\r\n                    <td>')
        __M_writer(str( overdueItem['name'] ))
        __M_writer('</td>\r\n                    <td>')
        __M_writer(str( overdueItem['dateDue'] ))
        __M_writer('</td>\r\n                    <td>')
        __M_writer(str( overdueItem['daysLate'] ))
        __M_writer(' (x $')
        __M_writer(str( overdueItem['fee'] ))
        __M_writer('/day)</td>\r\n                    <td>')
        __M_writer(str( overdueItem['latefee'] ))
        __M_writer('</td>\r\n                </tr>\r\n            </tbody>\r\n        </table>\r\n        <div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "check_rentals.html", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/check_rentals.html", "line_map": {"64": 31, "65": 32, "66": 32, "72": 66, "16": 0, "27": 1, "32": 39, "38": 2, "48": 2, "49": 5, "50": 5, "51": 7, "52": 7, "53": 10, "54": 10, "55": 28, "56": 28, "57": 29, "58": 29, "59": 30, "60": 30, "61": 31, "62": 31, "63": 31}}
__M_END_METADATA
"""
