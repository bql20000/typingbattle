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
            mode = 'random'
            break;
    }
    reset();
}
