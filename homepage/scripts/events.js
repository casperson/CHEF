$(function(){

        $('#create-event').on('click', function() {

            $.loadmodal({
                url: '/homepage/events.create/',
                title: 'Create Event',
                width: '500px'
            });

        });

        $('.EventEditForm').on('click', function() {

            var pid = $(this).attr('data-pid');
            $.loadmodal({
                url: '/homepage/events.edit/' + pid,
                title: 'Edit Event',
                width: '500px'
            });

        });

        $('.delete-event').on('click', function() {

            var r = confirm("Are you sure you want to delete this Festival Event?");
            if (r) {
                var eid = $(this).attr('data-eid');
                $.ajax({
                    url: '/homepage/events.delete/' + eid
                });
                window.location.reload()
            } else {
            }
        });

}); //end tag