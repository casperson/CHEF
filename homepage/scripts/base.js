$(function(){

        $('#show_login_dialog').on('click', function() {

            $.loadmodal({
                url: '/base.loginform/',
                title: 'Login Here',
                width: '500px'
            });

        });

        $('#create_account_btn').on('click', function() {
                $.loadmodal({
                    url: '/account/user.create/',
                    title: 'Create Account',
                    width: '500px'
                });

            });


        $('#shopping_cart_dialog2').on('click', function() {

            $.loadmodal({
                url: '/retail/product.shopping_cart/',
                title: 'Shopping Cart',
                width: '800px'
                 });
        });

}); //end tag