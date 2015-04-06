# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428209478.594867
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/events.detail.html'
_template_uri = 'events.detail.html'
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
        event = context.get('event', UNDEFINED)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
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
        event = context.get('event', UNDEFINED)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n    <div>\r\n        <p> <h2>')
        __M_writer(str( event.name ))
        __M_writer(' </h2></p>\r\n        <p> Dates: ')
        __M_writer(str( event.start_date))
        __M_writer(' - ')
        __M_writer(str( event.end_date))
        __M_writer('  </p>\r\n        <p> Description: ')
        __M_writer(str( event.description))
        __M_writer(' </p>\r\n    </div>\r\n\r\n        <p><h4>Events</h4></p>\r\n            <div>\r\n                <table class="table table-bordered">\r\n                    <thead>\r\n                        <th>Name</th>\r\n                        <th>Description</th>\r\n                        <th>Location</th>\r\n                        <th>Supervisor</th>\r\n                    </thead>\r\n\r\n')
        for area in areas:
            __M_writer('                        <tr>\r\n                            <td>')
            __M_writer(str( area.name))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( area.description ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( area.place_number ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( area.supervisor ))
            __M_writer('</td>\r\n                        </tr>\r\n')
        __M_writer('                </table>\r\n            </div>\r\n    <p><h4>Products Available</h4></p>\r\n           <div>\r\n                <table class="table table-striped" style="background-color: white; border: .5px solid #DDDDDD">\r\n                    <thead>\r\n                        <th>Picture</th>\r\n                        <th>Name</th>\r\n                        <th>Description</th>\r\n                        <th>Price</th>\r\n                    </thead>\r\n                    <tbody>\r\n')
        for product in products:
            __M_writer('                        <tr>\r\n                            <div>\r\n                                <td> <img class="description" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('retail/media/')
            __M_writer(str( product.name ))
            __M_writer('.jpg/"></td>\r\n                            </div>\r\n                            <td>')
            __M_writer(str( product.name))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( product.description ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(str( product.price ))
            __M_writer('</td>\r\n                         </tr>\r\n')
        __M_writer('                </table>\r\n            </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.detail.html", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/events.detail.html", "line_map": {"64": 8, "65": 9, "66": 9, "67": 22, "68": 23, "69": 24, "70": 24, "71": 25, "72": 25, "73": 26, "74": 26, "75": 27, "76": 27, "77": 30, "78": 42, "79": 43, "80": 45, "81": 45, "82": 45, "83": 45, "84": 47, "85": 47, "86": 48, "87": 48, "88": 49, "89": 49, "90": 52, "27": 0, "96": 90, "38": 1, "48": 3, "58": 3, "59": 7, "60": 7, "61": 8, "62": 8, "63": 8}, "source_encoding": "ascii"}
__M_END_METADATA
"""
