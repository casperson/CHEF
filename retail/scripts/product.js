$(function() {

    $('#search').keyup(function(){
        var valThis = $(this).val().toLowerCase();
        console.log(valThis);
        $('#product_list>li').each(function(){
            var text = $(this).find("a").text().toLowerCase();
            console.log(valThis);
            (text.indexOf(valThis) == 0) ? $(this).show() : $(this).hide();
       });
    });
});