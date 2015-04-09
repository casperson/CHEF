$(function(){

        //$('#ShoppingCart').ajaxForm(function(data){
        //
        //    $('#jquery-loadmodal-js-body').html(data);
        //
        //});


        $('.delete_line_item').on('click', function() {

            var pid =  $(this).attr('data-pid');
            $.ajax({
                url: '/retail/product.delete_line_item/' + pid
            });

        });

        $('.delete_rental_item').on('click', function() {

             var rid =  $(this).attr('data-rid');
            $.ajax({
                url: '/retail/rental.delete_rental_item/' + rid
                //success: function(data) {
                //}
            });
            //$('#jquery-loadmodal-js-body').reload()

        });

}); //end tag