$(function(){

        $('#create-rental').on('click', function() {

            $.loadmodal({
                url: '/retail/rental.create/normal/',
                title: 'Create Rental Item',
                width: '500px'
            });

        });


        $('#create-wardrobe').on('click', function() {

            $.loadmodal({
                url: '/retail/rental.create/wardrobe/',
                title: 'Create Wardrobe Item',
                width: '500px'
            });

        });


        $('.WardrobeEditForm').on('click', function() {

            var wardrobeid = $(this).attr('data-pid');
            $.loadmodal({
                url: '/retail/rental.editwardrobeitem/' + wardrobeid,
                title: 'Edit Wardrobe Item',
                width: '500px'
            });

        });

        $('.RentalEditForm').on('click', function() {

            var rentalid = $(this).attr('data-pid');
            $.loadmodal({
                url: '/retail/rental.edit/' + rentalid,
                title: 'Edit Rental Item',
                width: '500px'
            });

        });

        $('.DeleteRentalItem').on('click', function() {

            var r = confirm("Are you sure you want to delete this Rentable Item?");
            if (r) {
                var rid = $(this).attr('data-rid');
                $.ajax({
                    url: '/retail/rental.delete/' + rid
                });
                window.location.reload()
            } else {

            }
        });

        $('.DeleteWardrobeItem').on('click', function() {

            var r = confirm("Are you sure you want to delete this Wardrobe Item?");
            if (r) {
                var wid = $(this).attr('data-wid');
                $.ajax({
                    url: '/retail/rental.deletewardrobeitem/' + wid
                });
                window.location.reload()
            } else {
            }
        });

}); //end tag