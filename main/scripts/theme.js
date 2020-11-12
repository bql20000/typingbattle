function setBackground(self) {
    let value = `url(../images/background/${self.innerHTML}.gif)`;
    console.log(value);
    $('body').css('background-image', value);
    self.parentNode.previousSibling.previousSibling.innerHTML = self.innerHTML;
}
