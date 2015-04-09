$(function(){

        $('.UserEdit').on('click', function() {

            var userid = $(this).attr('data-pid');
            $.loadmodal({
                url: '/account/user.edit/' + userid,
                title: 'Edit Account',
                width: '500px'
            });

        });

        $('.DeleteUser').on('click', function() {

            var r = confirm("Are you sure you want to delete this User?");
            if (r) {
                var pid = $(this).attr('data-pid');
                $.ajax({
                    url: '/account/user.delete/' + pid
                });
                window.location.reload()
            } else {
            }
        });

}); //end tag