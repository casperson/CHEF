# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427506248.64365
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\scripts/product.shoppingcart.jsm'
_template_uri = 'product.shoppingcart.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer("$(function(){\r\n\r\n        //$('#ShoppingCart').ajaxForm(function(data){\r\n        //\r\n        //    $('#jquery-loadmodal-js-body').html(data);\r\n        //\r\n        //});\r\n\r\n        var lid =  $(this).attr('data-pid');\r\n\r\n        $('.delete_line_item').on('click', function() {\r\n\r\n            $.ajax({\r\n                url: '/retail/rental.delete_line_item/' + lid\r\n            });\r\n\r\n        });\r\n\r\n        var rid =  $(this).attr('data-rid');\r\n\r\n        $('.delete_rental_item').on('click', function() {\r\n\r\n            $.ajax({\r\n                url: '/retail/rental.delete_line_item/' + rid\r\n            });\r\n\r\n        });\r\n\r\n}); //end tag")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "product.shoppingcart.jsm", "line_map": {"16": 0, "27": 21, "21": 1}, "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\scripts/product.shoppingcart.jsm"}
__M_END_METADATA
"""
