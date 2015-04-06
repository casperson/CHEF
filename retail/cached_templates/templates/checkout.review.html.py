# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428182784.006129
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
        total = context.get('total', UNDEFINED)
        rentalitems = context.get('rentalitems', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        subtotal = context.get('subtotal', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
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
        total = context.get('total', UNDEFINED)
        rentalitems = context.get('rentalitems', UNDEFINED)
        lineitems = context.get('lineitems', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        subtotal = context.get('subtotal', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div>\r\n        <p></p>\r\n    </div>\r\n\r\n    <div class="container">\r\n        <p id="love" class="list-group-item-heading">Checkout: easy as 1, 2, 3!</p>\r\n        <div class="row form-group">\r\n            <div class="col-xs-12">\r\n                <ul class="nav nav-pills nav-justified thumbnail setup-panel">\r\n                    <li class="active"><a href="#step-1">\r\n                        <h4 class="list-group-item-heading">Step 1: Review</h4>\r\n                    </a></li>\r\n                    <li class="disabled"><a href="#step-2">\r\n                        <h4 class="list-group-item-heading">Step 2: Shipping and Payment</h4>\r\n                    </a></li>\r\n                    <li class="disabled"><a href="#step-3">\r\n                        <h4 class="list-group-item-heading">Step 3: Confirmation</h4>\r\n                    </a></li>\r\n                </ul>\r\n            </div>\r\n        </div>\r\n        <div class="row setup-content" id="step-1">\r\n            <div class="col-xs-12">\r\n                <div class="col-md-12 well text-center">\r\n')
        __M_writer('                    <div class="container">\r\n                        <div class="row">\r\n                            <div class="col-xs-8">\r\n                                <div class="panel panel-info">\r\n                                    <div class="panel-heading">\r\n                                        <div class="panel-title">\r\n                                            <div class="row">\r\n                                                <div class="col-xs-6">\r\n                                                    <h5><span class="glyphicon glyphicon-shopping-cart"></span> Shopping Cart Review</h5>\r\n                                                </div>\r\n                                                <div class="col-xs-6">\r\n                                                    <button type="button" class="btn btn-primary btn-sm btn-block">\r\n                                                        <span class="glyphicon glyphicon-share-alt"></span> Continue shopping\r\n                                                    </button>\r\n                                                </div>\r\n                                            </div>\r\n                                        </div>\r\n                                    </div>\r\n                                    <div class="panel-body">\r\n')
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
        for rentalitem in rentalitems:
            __M_writer('                                        <div class="row">\r\n                                            <div class="col-xs-2"><img class="img-responsive" src="http://placehold.it/100x70">\r\n                                            </div>\r\n                                            <div class="col-xs-4">\r\n                                                <h4 class="product-name"><strong>')
            __M_writer(str( rentalitem.rental_item_name() ))
            __M_writer('</strong></h4><h4><small>Rental description</small></h4>\r\n                                            </div>\r\n                                            <div class="col-xs-6">\r\n                                                <div class="col-xs-6 text-right">\r\n                                                    <h6><strong>')
            __M_writer(str( rentalitem.rental_item_price() ))
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
{"uri": "checkout.review.html", "source_encoding": "ascii", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\retail\\templates/checkout.review.html", "line_map": {"64": 30, "65": 49, "66": 50, "67": 51, "68": 51, "69": 51, "70": 51, "71": 54, "72": 54, "73": 58, "74": 58, "75": 61, "76": 61, "77": 72, "78": 73, "79": 77, "80": 77, "81": 81, "82": 81, "83": 95, "84": 111, "85": 111, "86": 112, "87": 112, "88": 113, "89": 113, "27": 0, "95": 89, "40": 1, "45": 130, "51": 3, "63": 3}}
__M_END_METADATA
"""
