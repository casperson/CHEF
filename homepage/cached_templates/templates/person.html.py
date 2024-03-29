# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423365769.887886
_enable_loop = True
_template_filename = 'C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/person.html'
_template_uri = 'person.html'
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
    return runtime._inherit_from(context, 'base2.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        persons = context.get('persons', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
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
        persons = context.get('persons', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <h2 style="text-decoration: underline">Contact List</h2>\r\n    <div class="clearfix"></div>\r\n    <div class="text-right">\r\n        <a href="/homepage/person.create/" class="btn btn-success">Add New Person</a>\r\n    </div>\r\n\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <th>ID</th>\r\n            <th>First Name</th>\r\n            <th>Last Name</th>\r\n            <th>Email</th>\r\n            <th>Edit | Delete</th>\r\n        </tr>\r\n')
        for person in persons:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(str( person.id ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( person.given_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( person.family_name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str( person.email ))
            __M_writer('</td>\r\n                <td>\r\n                    <div class="btn-group" role="group" aria-label="...">\r\n                        <a type="button" class="btn btn-default" href="/homepage/person.edit/')
            __M_writer(str( person.id ))
            __M_writer('/"><i class="fa fa-edit"></i></a>\r\n                        <button type="button" data-toggle="modal" data-target="#form-modal" class="btn btn-danger"><i class="fa fa-trash"></i></button>\r\n                        <div class="modal fade" id="form-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                            <div class="modal-dialog">\r\n                                <div class="modal-content">\r\n                                    <div class="modal-header">\r\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                                        <h4 class="modal-title">Delete Warning</h4>\r\n                                    </div>\r\n                                    <div id="form-modal-body" class="modal-body">\r\n                                        <p>Are you sure you want to delete ')
            __M_writer(str( person.given_name ))
            __M_writer('</p>\r\n                                    </div>\r\n                                    <div class="modal-footer">\r\n                                        <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                                        <a href="/homepage/person.delete/')
            __M_writer(str( person.id ))
            __M_writer('/" class="btn btn-danger">Delete</a>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "person.html", "filename": "C:\\Users\\Sterling\\Documents\\GitHub\\CHEF\\homepage\\templates/person.html", "line_map": {"64": 26, "65": 36, "66": 36, "67": 40, "68": 40, "69": 49, "75": 69, "27": 0, "35": 1, "45": 2, "52": 2, "53": 18, "54": 19, "55": 20, "56": 20, "57": 21, "58": 21, "59": 22, "60": 22, "61": 23, "62": 23, "63": 26}}
__M_END_METADATA
"""
