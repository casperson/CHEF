# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428646089.223776
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.edit.html'
_template_uri = 'product.edit.html'
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
    return runtime._inherit_from(context, '/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        product = context.get('product', UNDEFINED)
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
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <form class="form-horizontal" id="ProductEditForm" method="POST" action="/retail/product.edit/')
        __M_writer(str( product.id ))
        __M_writer('">\r\n        <table>\r\n')
        for field in form:
            __M_writer('                <div class="form-group">\r\n                    <label for="id_')
            __M_writer(str(field.name))
            __M_writer('" class="col-sm-3 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\r\n                    <div class="col-sm-9">\r\n                        ')
            __M_writer(str(field))
            __M_writer('\r\n                    </div>\r\n                </div>\r\n')
        __M_writer('            <div class="form-group">\r\n                <div class="col-sm-offset-3 col-sm-9">\r\n                    <button class="btn btn-success" type="submit">Save Product</button>\r\n                </div>\r\n            </div>\r\n        </table>\r\n\r\n    </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 11, "65": 15, "27": 0, "36": 1, "71": 65, "46": 3, "54": 3, "55": 5, "56": 5, "57": 7, "58": 8, "59": 9, "60": 9, "61": 9, "62": 9, "63": 11}, "uri": "product.edit.html", "source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/product.edit.html"}
__M_END_METADATA
"""
