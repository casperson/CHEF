$(function(){

    var userid = $(this).attr('data-pid');

    $('#change_password_dialog').on('click', function() {

        $.loadmodal({
            url: '/account/account.changepassword/',
            title: 'Change Password',
            width: '500px'
        });

    });

    $('#user_edit').on('click', function() {

            $.loadmodal({
                url: '/account/user.edit/' + userid + '/',
                title: 'Edit Account',
                width: '500px'
            });

        });
}); //end tag