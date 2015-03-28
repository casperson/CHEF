# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427242382.237698
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/check_rentals.html'
_template_uri = 'check_rentals.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <div class="email-header">\r\n            <img class="col-md-3" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/ch_logo.png" alt="Colonial Heritage Foundation"/>\r\n            <p class="col-md-3"></p>\r\n            <h2 class="col-md-6  right-align"><span style="color: red; font-weight: bold;">2</span> Overdue Items as of 3/20/2015</h2>\r\n        </div>\r\n        <div class="email-body">\r\n            <h3>Hello Sterling,</h3>\r\n            <p>The following items are still rented out under your account and are now considered overdue. The items and their\r\n            corresponding fees are listed below.</p>\r\n            <p>Payment is due immediately.</p>\r\n            <h3>Overdue Items</h3>\r\n        </div>\r\n        <table class="table table-striped table-condensed receipt-table">\r\n            <thead>\r\n                <tr>\r\n                    <th>ID</th>\r\n                    <th>Item Name</th>\r\n                    <th>Date Due</th>\r\n                    <th>Days Late</th>\r\n                    <th>Current Fee Owed</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                <tr>\r\n                    <td>1</td>\r\n                    <td>Pistol</td>\r\n                    <td>3/19/2015</td>\r\n                    <td>1 (x $1.50/day)</td>\r\n                    <td>$1.50</td>\r\n                </tr>\r\n                <tr>\r\n                    <td>2</td>\r\n                    <td>Boots</td>\r\n                    <td>3/15/2015</td>\r\n                    <td>5  (x $1.05/day)</td>\r\n                    <td>$5.25</td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n        <div>\r\n            <p>The following items are currently checked out, but are not yet due. Failure to return by due date will\r\n            result in a late fee.</p>\r\n            <h3>Rented Items</h3>\r\n        </div>\r\n        <table class="table table-striped table-condensed">\r\n            <thead>\r\n                <tr>\r\n                    <th>ID</th>\r\n                    <th>Item Name</th>\r\n                    <th>Date Due</th>\r\n                    <th>Remaining Days Until Late</th>\r\n')
        __M_writer('                    <th>Date Payment Received</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n                <tr>\r\n                    <td>3</td>\r\n                    <td>Cravat</td>\r\n                    <td>3/25/2015</td>\r\n                    <td>5</td>\r\n')
        __M_writer('                    <td>Not Paid </td>\r\n                </tr>\r\n')
        __M_writer('            </tbody>\r\n        </table>\r\n        <br/><br/><br/>\r\n        <h3>As always, thank you for choosing the Colonial Heritage Foundation and we look forward to seeing you in the future.</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 58, "35": 1, "52": 3, "53": 6, "54": 6, "55": 48, "56": 63, "57": 73, "58": 81, "27": 0, "45": 3}, "source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/check_rentals.html", "uri": "check_rentals.html"}
__M_END_METADATA
"""
