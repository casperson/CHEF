# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428205747.745039
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/checkout.payment.html'
_template_uri = 'checkout.payment.html'
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <p></p>\r\n    </div>\r\n\r\n    <div class="container">\r\n        <p id="love" class="list-group-item-heading">Checkout: easy as 1, 2, 3!</p>\r\n        <div class="row form-group">\r\n            <div class="col-xs-12">\r\n                <ul class="nav nav-pills nav-justified thumbnail setup-panel">\r\n                    <li class="disabled"><a href="checkout.review.html">\r\n                        <h4 class="list-group-item-heading">Step 1: Review</h4>\r\n                    </a></li>\r\n                    <li class="active"><a href="checkout.payment.html">\r\n                        <h4 class="list-group-item-heading">Step 2: Shipping and Payment</h4>\r\n                    </a></li>\r\n                    <li class="disabled"><a href="#step-3">\r\n                        <h4 class="list-group-item-heading">Step 3: Confirmation</h4>\r\n                    </a></li>\r\n                </ul>\r\n            </div>\r\n        </div>\r\n\r\n        <form id="PaymentForm" method="POST">\r\n            <table>\r\n                ')
        __M_writer(str( form ))
        __M_writer('\r\n            </table>\r\n            <br/>\r\n            <button class="btn btn-success" type="submit">Process Payment</button>\r\n        </form>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"56": 29, "35": 1, "54": 3, "55": 29, "40": 35, "41": 240, "27": 0, "62": 56, "47": 3}, "uri": "checkout.payment.html", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/checkout.payment.html"}
__M_END_METADATA
"""
