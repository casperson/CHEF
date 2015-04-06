$(function(){

    $('#shopping_cart_dialog').on('click', function() {

        var pid = $(this).attr('data-pid');
        var qid = document.getElementById('qty-input').value;

        $.loadmodal({
            url: '/retail/product.create_line_item/' + pid + "/" + qid + "/product",
            title: 'Shopping Cart',
            width: '800px'
        });

    });
}); //end tag