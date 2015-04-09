$(function(){

        $('.ProductEditForm').on('click', function() {

            var productid = $(this).attr('data-pid');
            $.loadmodal({
                url: '/retail/product.edit/' + productid,
                title: 'Edit Product Item',
                width: '500px'
            });

        });

        $('.DeleteProduct').on('click', function() {

            var r = confirm("Are you sure you want to delete this product?");
            if (r) {
                var did = $(this).attr('data-did');
                $.ajax({
                    url: '/retail/product.delete/' + did
                });
                window.location.reload()
            } else {
            }
        });

}); //end tag