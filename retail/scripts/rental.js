$(function(){

    $('.shopping_cart_dialog3').on('click', function() {

        var rid = $(this).attr('data-pid');

        $.loadmodal({
            url: '/retail/rental.create_rentalline_item/' + rid,
            title: 'Shopping Cart',
            width: '800px'
        });
    });

}); //end tag