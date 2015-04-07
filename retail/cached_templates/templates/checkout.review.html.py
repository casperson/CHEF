# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428426289.636323
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/checkout.review.html'
_template_uri = 'checkout.review.html'
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
        subtotal = context.get('subtotal', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        returnitems = context.get('returnitems', UNDEFINED)
        total = context.get('total', UNDEFINED)
        rentalitems = context.get('rentalitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        subtotal = context.get('subtotal', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        def content_center():
            return render_content_center(context)
        len = context.get('len', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        returnitems = context.get('returnitems', UNDEFINED)
        total = context.get('total', UNDEFINED)
        rentalitems = context.get('rentalitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <p></p>\r\n    </div>\r\n\r\n    <div class="container">\r\n        <p id="love" class="list-group-item-heading">Checkout: easy as 1, 2, 3!</p>\r\n        <div class="row form-group">\r\n            <div class="col-xs-12">\r\n                <ul class="nav nav-pills nav-justified thumbnail setup-panel">\r\n                    <li class="active"><a href="#step-1">\r\n                        <h4 class="list-group-item-heading">Step 1: Review</h4>\r\n                    </a></li>\r\n                    <li class="disabled"><a href="#step-2">\r\n                        <h4 class="list-group-item-heading">Step 2: Shipping and Payment</h4>\r\n                    </a></li>\r\n                    <li class="disabled"><a href="#step-3">\r\n                        <h4 class="list-group-item-heading">Step 3: Confirmation</h4>\r\n                    </a></li>\r\n                </ul>\r\n            </div>\r\n        </div>\r\n        <div class="row setup-content" id="step-1">\r\n            <div class="col-xs-12">\r\n                <div class="col-md-12 well text-center">\r\n')
        __M_writer('                    <div class="container">\r\n                        <div class="row">\r\n                            <div class="col-xs-8">\r\n                                <div class="panel panel-info">\r\n                                    <div class="panel-heading">\r\n                                        <div class="panel-title">\r\n                                            <div class="row">\r\n                                                <div class="col-xs-6">\r\n                                                    <h5><span class="glyphicon glyphicon-shopping-cart"></span> Shopping Cart Review</h5>\r\n                                                </div>\r\n                                                <div class="col-xs-6">\r\n                                                    <button type="button" class="btn btn-primary btn-sm btn-block">\r\n                                                        <span class="glyphicon glyphicon-share-alt"></span> Continue shopping\r\n                                                    </button>\r\n                                                </div>\r\n                                            </div>\r\n                                        </div>\r\n                                    </div>\r\n                                    <div class="panel-body">\r\n')
        if len(lineitems):
            __M_writer('                                            <h3>Sale Items</h3>\r\n')
        for lineitem in lineitems:
            __M_writer('                                        <div class="row">\r\n                                            <div class="col-xs-2"><img class="img-responsive" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('retail/media/')
            __M_writer(str( lineitem.product_name() ))
            __M_writer('.jpg/">\r\n                                            </div>\r\n                                            <div class="col-xs-4">\r\n                                                <h4 class="product-name"><strong>')
            __M_writer(str( lineitem.product_name() ))
            __M_writer('</strong></h4><h4><small>Product description</small></h4>\r\n                                            </div>\r\n                                            <div class="col-xs-6">\r\n                                                <div class="col-xs-6 text-right">\r\n                                                    <h6><strong>')
            __M_writer(str( lineitem.product_price() ))
            __M_writer('<span class="text-muted">x</span></strong></h6>\r\n                                                </div>\r\n                                                <div class="col-xs-4">\r\n                                                    <input type="text" class="form-control input-sm" value=')
            __M_writer(str( lineitem.quantity ))
            __M_writer('>\r\n                                                </div>\r\n                                                <div class="col-xs-2">\r\n                                                    <button type="button" class="btn btn-link btn-xs">\r\n                                                        <span class="glyphicon glyphicon-trash"> </span>\r\n                                                    </button>\r\n                                                </div>\r\n                                            </div>\r\n                                        </div>\r\n                                        <hr>\r\n')
        if len(rentalitems) > 0:
            __M_writer('                                            <h3>Rental Items</h3>\r\n')
        for rentalitem in rentalitems:
            __M_writer('                                        <div class="row">\r\n                                            <div class="col-xs-2"><img class="img-responsive" src="http://placehold.it/100x70">\r\n                                            </div>\r\n                                            <div class="col-xs-4">\r\n                                                <h4 class="product-name"><strong>')
            __M_writer(str( rentalitem.rental_item_name() ))
            __M_writer('</strong></h4><h4><small>Rental description</small></h4>\r\n                                            </div>\r\n                                            <div class="col-xs-6">\r\n                                                <div class="col-xs-6 text-right">\r\n                                                    <h6><strong>')
            __M_writer(str( rentalitem.rental_item_price() ))
            __M_writer(' <span class="text-muted">x</span></strong></h6>\r\n                                                </div>\r\n                                                <div class="col-xs-4">\r\n                                                    <input type="text" class="form-control input-sm" value="1">\r\n                                                </div>\r\n                                                <div class="col-xs-2">\r\n                                                    <button type="button" class="btn btn-link btn-xs">\r\n                                                        <span class="glyphicon glyphicon-trash"> </span>\r\n                                                    </button>\r\n                                                </div>\r\n                                            </div>\r\n                                        </div>\r\n                                        <hr>\r\n')
        if len(returnitems) > 0:
            __M_writer('                                            <h3>Return Items</h3>\r\n')
        for returnitem in returnitems:
            __M_writer('                                        <div class="row">\r\n                                            <div class="col-xs-2"><img class="img-responsive" src="http://placehold.it/100x70">\r\n                                            </div>\r\n                                            <div class="col-xs-4">\r\n                                                <h4 class="product-name"><strong>')
            __M_writer(str( returnitem.return_item_name() ))
            __M_writer('</strong></h4><h4><small>Rental description</small></h4>\r\n                                            </div>\r\n                                            <div class="col-xs-6">\r\n                                                <div class="col-xs-6 text-right">\r\n                                                    <h6><strong>')
            __M_writer(str( returnitem.return_line_item.rental_line_item.calc_returntotal() ))
            __M_writer(' <span class="text-muted">x</span></strong></h6>\r\n                                                </div>\r\n                                                <div class="col-xs-4">\r\n                                                    <input type="text" class="form-control input-sm" value="1">\r\n                                                </div>\r\n                                                <div class="col-xs-2">\r\n                                                    <button type="button" class="btn btn-link btn-xs">\r\n                                                        <span class="glyphicon glyphicon-trash"> </span>\r\n                                                    </button>\r\n                                                </div>\r\n                                            </div>\r\n                                        </div>\r\n                                        <hr>\r\n')
        __M_writer('                                        <div class="row">\r\n                                            <div class="text-center">\r\n                                                <div class="col-xs-9">\r\n                                                    <h6 class="text-right">Added items?</h6>\r\n                                                </div>\r\n                                                <div class="col-xs-3">\r\n                                                    <button type="button" class="btn btn-default btn-sm btn-block">\r\n                                                        Update cart\r\n                                                    </button>\r\n                                                </div>\r\n                                            </div>\r\n                                        </div>\r\n                                    </div>\r\n                                    <div class="panel-footer">\r\n                                        <div class="row text-center">\r\n                                            <div class="col-xs-9">\r\n                                                <h5 class="text-right">Sub Total <strong>$ ')
        __M_writer(str( subtotal ))
        __M_writer('</strong></h5>\r\n                                                <h5 class="text-right">Tax <strong>$ ')
        __M_writer(str( tax ))
        __M_writer('</strong></h5>\r\n                                                <h4 class="text-right">Total <strong>$ ')
        __M_writer(str( total ))
        __M_writer('</strong></h4>\r\n                                            </div>\r\n                                            <div class="col-xs-3">\r\n                                                <a href="/retail/checkout.payment/" type="button" class="btn btn-success btn-block">\r\n                                                    Next Step\r\n                                                </a>\r\n                                            </div>\r\n                                        </div>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "checkout.review.html", "source_encoding": "ascii", "line_map": {"27": 0, "42": 1, "47": 162, "53": 3, "67": 3, "68": 30, "69": 49, "70": 50, "71": 52, "72": 53, "73": 54, "74": 54, "75": 54, "76": 54, "77": 57, "78": 57, "79": 61, "80": 61, "81": 64, "82": 64, "83": 75, "84": 76, "85": 78, "86": 79, "87": 83, "88": 83, "89": 87, "90": 87, "91": 101, "92": 102, "93": 104, "94": 105, "95": 109, "96": 109, "97": 113, "98": 113, "99": 127, "100": 143, "101": 143, "102": 144, "103": 144, "104": 145, "105": 145, "111": 105}, "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/checkout.review.html"}
__M_END_METADATA
"""
