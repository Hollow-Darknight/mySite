$(document).ready(function(){
    $('.card').click(function(){
        window.location.replace($(this).data('url'));
    });
});