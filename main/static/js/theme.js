var theme = 'No theme';
function setBackground(self) {
    let value = (self.innerHTML == 'No theme') ? 'None' : `url(static/img/${self.innerHTML}.gif)`;
    $('body').css('background-image', value);
    document.getElementById("theme-button").innerHTML = self.innerHTML;
}
