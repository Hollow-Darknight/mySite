$(document).ready(function () {
    let color = $('.characters').mouseenter(showName);
    $('.characters').mouseleave(hideName);
    $('#' + color).click(goToPage(color));
});

function showName(e) {
    e.preventDefault();
    let characterName = "";
    let color = $(this).attr('id');
    switch (color) {
        case 'red':
            characterName = "Hollow Darknight";
            break;

        case 'purple':
            characterName = "Abysse Everlasting";
            break;

        case 'blue':
            characterName = "Saphire Darkshift";
            break;

        case 'violet':
            characterName = "Violette Darknight";
            break;

        case 'black':
            characterName = "Starlight Arachnie";
            break;

        case 'green':
            characterName = "Sylith";
            break;

        default:
            break;
    }
    $('#selectedCharacterName').html(characterName);
    
    return color
}

function hideName(e){
    e.preventDefault();
    $('#selectedCharacterName').empty();
}

function goToPage(color, e){
    e.preventDefault();
    let redirect = $(this).data('url');
    alert("Clic sur " + $(this).data('url'));
    window.location.href = redirect;
}
