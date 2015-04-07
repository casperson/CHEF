# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428374959.812222
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/overdue_report.html'
_template_uri = 'overdue_report.html'
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
        sixty = context.get('sixty', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
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
        sixty = context.get('sixty', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n\r\n        <h3>Items Over 30 Days</h3>\r\n        <table class="table table-striped table-condensed receipt-table">\r\n        <thead>\r\n            <tr>\r\n                <th>ID</th>\r\n                <th>Item Name</th>\r\n                <th>Date Due</th>\r\n                <th>Days Late</th>\r\n                <th>Current Fee Owed</th>\r\n                <th>Renter</th>\r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        for rentalitem in thirty:
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(str( rentalitem['id'] ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( rentalitem['name'] ))
            __M_writer(' </td>\r\n                    <td>')
            __M_writer(str( rentalitem['datedue'] ))
            __M_writer(' </td>\r\n                    <td>')
            __M_writer(str( rentalitem['dayslate'] ))
            __M_writer(' (x $')
            __M_writer(str( rentalitem['price'] ))
            __M_writer('/day)</td>\r\n                    <td>$')
            __M_writer(str( rentalitem['latefee'] ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( rentalitem['renter'] ))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('        </tbody>\r\n        </table>\r\n        <h3>Items Over 60 Days</h3>\r\n        <table class="table table-condensed receipt-table">\r\n        <thead>\r\n            <tr>\r\n                <th>ID</th>\r\n                <th>Item Name</th>\r\n                <th>Date Due</th>\r\n                <th>Days Late</th>\r\n                <th>Current Fee Owed</th>\r\n                <th>Renter</th>\r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        for rentalitem in sixty:
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(str( rentalitem['id'] ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( rentalitem['name'] ))
            __M_writer(' </td>\r\n                    <td>')
            __M_writer(str( rentalitem['datedue'] ))
            __M_writer(' </td>\r\n                    <td>')
            __M_writer(str( rentalitem['dayslate'] ))
            __M_writer(' (x $')
            __M_writer(str( rentalitem['price'] ))
            __M_writer('/day)</td>\r\n                    <td>$')
            __M_writer(str( rentalitem['latefee'] ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( rentalitem['renter'] ))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('        </tbody>\r\n        </table>\r\n        <h3>Items Over 90 Days</h3>\r\n        <table class="table table-condensed receipt-table">\r\n        <thead>\r\n            <tr>\r\n                <th>ID</th>\r\n                <th>Item Name</th>\r\n                <th>Date Due</th>\r\n                <th>Days Late</th>\r\n                <th>Current Fee Owed</th>\r\n                <th>Renter</th>\r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        for rentalitem in ninety:
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(str( rentalitem['id'] ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( rentalitem['name'] ))
            __M_writer(' </td>\r\n                    <td>')
            __M_writer(str( rentalitem['datedue'] ))
            __M_writer(' </td>\r\n                    <td>')
            __M_writer(str( rentalitem['dayslate'] ))
            __M_writer(' (x $')
            __M_writer(str( rentalitem['price'] ))
            __M_writer('/day)</td>\r\n                    <td>$')
            __M_writer(str( rentalitem['latefee'] ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(str( rentalitem['renter'] ))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('        </tbody>\r\n        </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "37": 1, "47": 3, "56": 3, "57": 19, "58": 20, "59": 21, "60": 21, "61": 22, "62": 22, "63": 23, "64": 23, "65": 24, "66": 24, "67": 24, "68": 24, "69": 25, "70": 25, "71": 26, "72": 26, "73": 29, "74": 44, "75": 45, "76": 46, "77": 46, "78": 47, "79": 47, "80": 48, "81": 48, "82": 49, "83": 49, "84": 49, "85": 49, "86": 50, "87": 50, "88": 51, "89": 51, "90": 54, "91": 69, "92": 70, "93": 71, "94": 71, "95": 72, "96": 72, "97": 73, "98": 73, "99": 74, "100": 74, "101": 74, "102": 74, "103": 75, "104": 75, "105": 76, "106": 76, "107": 79, "113": 107}, "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/overdue_report.html", "uri": "overdue_report.html"}
__M_END_METADATA
"""
