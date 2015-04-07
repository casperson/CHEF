$(function(){

        $('.return_lineitem').on('click', function() {

            var rid =  $(this).attr('data-rid');

            $.loadmodal({
                url: '/retail/rental.return_lineitem/' + rid,
                title: '',
                width: '700px'
            });

        });

}); //end tag