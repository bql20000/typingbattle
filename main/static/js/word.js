let collection = [];    // list of strings representing words
let words = [];         // list of span elements representing words
let cur = 0;            // index of current word

function rand(min, max) {
    // random int in [min:max] (both inclusive)
    return Math.floor(Math.random() * (max - min) ) + min;
}

function lastInLine(word) {
    // If the current word reaches the end of the container, clear current line
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
    // remove all span elements representing words
    let cur_words = Array.from(document.getElementsByClassName('word'));
    cur_words.forEach(element => {
        element.remove();
    });
    words = [];
    cur = 0;
}

async function getCollection(mode) {
    // get 300 shuffled words based on chosen game mode
    url = '/words?mode=' + `${mode}`;
    let response = await fetch(url);
    return response.json();
}

function generateWords() {
    // generate span elements from collection of words received from server
    let board = document.getElementById('word-board');
    for (let i = 0; i < collection.length; ++i) {
        let w = document.createElement('span');
        let content = document.createTextNode(collection[i]);
        w.appendChild(content);
        w.classList.add('word');
        board.appendChild(w);
    }
    words = document.getElementsByClassName('word');
    words[0].classList.add('active-word');
}

async function resetWords() {
    clearWords();
    collection = await getCollection(mode);
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




jQuery(document).ready(function($){
 
    // Define a blank array for the effect positions. This will be populated based on width of the title.
    var bArray = [];
    // Define a size array, this will be used to vary bubble sizes
    var sArray = [4,6,8,10];
 
    // Push the header width values to bArray
    for (var i = 0; i < $('.bubbles').width(); i++) {
        bArray.push(i);
    }
     
    // Function to select random array element
    // Used within the setInterval a few times
    function randomValue(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }
 
    // setInterval function used to create new bubble every 350 milliseconds
    setInterval(function(){
         
        // Get a random size, defined as variable so it can be used for both width and height
        var size = randomValue(sArray);
        // New bubble appeneded to div with it's size and left position being set inline
        // Left value is set through getting a random value from bArray
        $('.bubbles').append('<div class="individual-bubble" style="left: ' + randomValue(bArray) + 'px; width: ' + size + 'px; height:' + size + 'px;"></div>');
         
        // Animate each bubble to the top (bottom 100%) and reduce opacity as it moves
        // Callback function used to remove finsihed animations from the page
        $('.individual-bubble').animate({
            'bottom': '100%',
            'opacity' : '-=0.7'
        }, 3000, function(){
            $(this).remove()
        }
        );
 
 
    }, 350);
 
});