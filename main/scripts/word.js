const localhost = 'http:/127.0.0.1:5000'

let collection_size = 200;
let collection = [];
let num_words = 300;
let words = [];
let cur = 0;

function rand(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

function lastInLine(word) {
    let cur_right = word.getBoundingClientRect().right;
    let next_right = word.nextSibling.getBoundingClientRect().right;
    return cur_right > next_right;
}

function pressKey(event, self) {
    if (!self.classList.contains('started')) {
        // these scope only executes once when typing the first letter
        startTiming();
        self.classList.add('started');
    }
    let new_char_ascii_value = event.which || event.keyCode;
    if (new_char_ascii_value == 32) {   // press ' '
        let cur_input = self.value;
        event.preventDefault();
        self.value = '';

        // change color of words
        words[cur].classList.remove('active-word');
        if (cur_input == words[cur].innerHTML) {
            words[cur].classList.add('corrected');
        }
        else {
            words[cur].classList.add('incorrected');
        }

        // clear a line if reach its end
        if (lastInLine(words[cur])) {
            for (let i = cur; i >= 0; --i) {
                words[i].hidden = true;
            }
        }
        words[++cur].classList.add('active-word');
    }
}

function clearWords() {
    let cur_words = Array.from(document.getElementsByClassName('word'));
    cur_words.forEach(element => {
        element.remove();
    });
    words = [];
    cur = 0;
}

async function getCollection(num) {
    url = localhost + '/words?size=' + `${num}`;
    let response = await fetch(url);
    return response.json();
}

function generateWords() {
    let board = document.getElementById('word-board');
    for (let i = 0; i < num_words; ++i) {
        let w = document.createElement('span');
        let content = document.createTextNode(collection[rand(0, collection_size-1)]);
        w.appendChild(content);
        w.classList.add('word');
        board.appendChild(w);
    }
    board.firstChild.classList.add('active-word');
    words = document.getElementsByClassName('word');
}

async function resetWords() {
    clearWords();
    collection = await getCollection(collection_size);
    generateWords();
}

function resetInputField() {
    inputField = document.getElementById('input');
    inputField.value = '';
    if (inputField.classList.contains('started')) {
        inputField.classList.remove('started');
    }
}

function reset() {
    resetWords();
    resetInputField();
    resetTimeLimit();
    $('#summary').hide();
}

document.addEventListener('DOMContentLoaded', function(event) {
    resetWords();
    $('#summary').hide();
})

$("#input").focusout(function(){
    $(this).attr("placeholder", "Countdown starts when you begin to type!");
});

$("#input").focus(function(){
    $(this).attr("placeholder", "");
});

