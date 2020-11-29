/* Navigation bar setup */
$('#navbarResponsive .nav-item').click(function () {
    let cur = $('.active-nav');
    if (cur) {
        cur.removeClass('active-nav');
    }
    $(this).addClass('active-nav');
    $('.sec').hide();

    let sec_name = '#sec-' + $(this).attr("name");
    if ($(this).attr("name") != 'account') $(sec_name).show();
});

/* Home page setup */
$(document).ready(function () {
    $('.sec').hide();
    $('#sec-home').show();
});


/* Theme setup */
var theme = 'Ocean';
function setBackground(self) {
    let value = `url(static/img/backgrounds/${self.innerHTML}.gif)`;
    $('body').css('background-image', value);
    document.getElementById("theme-button").innerHTML = self.innerHTML;
}

/* Mode setup */
var mode = 'basic';
function setMode(self) {
    document.getElementById('mode-button').innerHTML = self.innerHTML;
    switch (self.innerHTML) {
        case 'White Collar':
            mode = 'basic';
            break;
        case 'Scientist':
            mode = 'numerical';
            break;
        case 'Psychologist':
            mode = 'random';
            break;
    }
    reset();
}