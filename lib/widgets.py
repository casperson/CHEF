import django.forms

class DateDropdown(django.forms.DateInput):

    class Media:
        js = (
            'datetimepicker-master/jquery.datetimepicker.js',
            'datetimepicker-master/jquery.js'
        )
        css = {
            'all': (
                'datetimepicker-master/jquery.datetimepicker.css'
            )
        }

    def render(self, name, value, attrs=None):
        return super().render(name, value, attrs) + ('''
        <input id='datetimepicker' type='text'/>
        ''') + ('''
        <script>
            jQuery('#datetimepicker').datetimepicker({
            timepicker:false,
        });
        </script>
        ''')