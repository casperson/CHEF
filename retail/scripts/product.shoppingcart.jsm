$(function(){

        //$('#ShoppingCart').ajaxForm(function(data){
        //
        //    $('#jquery-loadmodal-js-body').html(data);
        //
        //});

        var lid =  $(this).attr('data-pid');

        $('.delete_line_item').on('click', function() {

            $.ajax({
                url: '/retail/rental.delete_line_item/' + lid
            });

        });

        var rid =  $(this).attr('data-rid');

        $('.delete_rental_item').on('click', function() {

            $.ajax({
                url: '/retail/rental.delete_line_item/' + rid
            });

        });

}); //end tag