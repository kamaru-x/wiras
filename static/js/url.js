$(document).ready(function(){
    $('#title').on('keyup',function(){
        var value = $('#title').val();
        var final = value.replace(/ /g,"-");
        $('#seo_url').val(final);
    });
})