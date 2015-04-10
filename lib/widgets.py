import django.forms


class DateDropdown(django.forms.DateInput):

    # class Media:
    #     js = (
    #         'datetimepicker-master/jquery.datetimepicker.js',
    #         'datetimepicker-master/jquery.js'
    #     )
    #     css = {
    #         'all': (
    #             'datetimepicker-master/jquery.datetimepicker.css'
    #         )
    #     }

    def render(self, name, value, attrs=None):
        return super().render(name, value, attrs) + ('''
        <span class='datetimepicker' ></span>
        ''') + ('''
        <script type='text/javascript'>
        $(function(){
            var input = $('.datetimepicker').siblings('input[name="%s"]');
            input.datetimepicker({
                timepicker: false,
                format: 'Y-m-d',
                allowblank: true
            });
        });
        </script>
        ''' % name)

    # def render(self, name, value, attrs=None):
    #     return super().render(name, value, attrs) + ('''
    #     <input id='datetimepicker' type='text'/>
    #     ''') + ('''
    #     <script type='text/javascript'>
    #     $(document).ready(function(){
    #         $('#datetimepicker').datetimepicker({
    #             timepicker:false,
    #             format: 'Y-m-d'
    #         });
    #     });
    #     </script>
    #     ''')