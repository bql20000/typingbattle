const localhost = 'http:/127.0.0.1:5000'

let collection_size = 200;
let collection = [];
let num_words = 300;
let words = [];
let cur = 0;

function rand(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

function clear_input_field() {
    document.getElementById('input').value = '';
}

function last_in_line(word) {
    let cur_right = word.getBoundingClientRect().right;
    let next_right = word.nextSibling.getBoundingClientRect().right;
    return cur_right > next_right;
}

function pressKey(event) {
    let new_char_ascii_value = event.which || event.keyCode;
    if (new_char_ascii_value == 32) {   // press ' '
        let cur_input = document.getElementById('input').value;
        event.preventDefault();
        clear_input_field();

        // change color of words
        words[cur].classList.remove('active');
        if (cur_input == words[cur].innerHTML) {
            words[cur].classList.add('corrected');
        }
        else {
            words[cur].classList.add('typo');
        }

        // clear a line if reach its end
        if (last_in_line(words[cur])) {
            for (let i = cur; i >= 0; --i) {
                words[i].hidden = true;
            }
        }
        words[++cur].classList.add('active');
    }
}

function clear_words() {
    let cur_words = Array.from(document.getElementsByClassName('word'));
    cur_words.forEach(element => {
        element.remove();
    });
    words = [];
    cur = 0;
}

async function get_collection(num) {
    url = localhost + '/words?size=' + `${num}`;
    let response = await fetch(url);
    return response.json();
}

function generate_words() {
    let board = document.getElementById('word-board');
    for (let i = 0; i < num_words; ++i) {
        let w = document.createElement('span');
        let content = document.createTextNode(collection[rand(0, collection_size-1)]);
        w.appendChild(content);
        w.classList.add('word');
        board.appendChild(w);
    }
    board.firstChild.classList.add('active');
    words = document.getElementsByClassName('word');
}

async function reset_words() {
    clear_words();
    collection = await get_collection(collection_size);
    generate_words();
    clear_input_field();
}