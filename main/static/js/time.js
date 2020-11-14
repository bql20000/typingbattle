let prev_time_limit = 15;
let time_limit = 15;

function setTime(self) {
    time_limit = parseInt(self.innerHTML);
    self.parentNode.previousSibling.previousSibling.innerHTML = time_limit;
    prev_time_limit = time_limit;
    reset();
}   

function clearIntervals() {
    clearInterval(timer);
    clearInterval(statisticizer);
}

function resetTimeLimit() {
    clearIntervals();
    time_limit = prev_time_limit;
    document.getElementById("time-button").innerHTML = time_limit;
}

let timer;
let statisticizer;
let wpmData = [];
let accData = [];

function startTiming() {
    timer = setInterval(counting, 1000);
    wpmData = [];
    accData = [];
    statisticizer = setInterval(calculate, 1000*(prev_time_limit/10));
}

function counting() {
    document.getElementById("time-button").innerHTML = --time_limit;
    if (time_limit == 0) {
        clearIntervals();
        showResults();
    }
}

function calculate() {
    let corrected = document.getElementsByClassName('corrected').length;
    let incorrected = document.getElementsByClassName('incorrected').length;

    let words_per_min = (corrected + incorrected) * 60 / (prev_time_limit - time_limit);
    let accuracy = (corrected + incorrected > 0) ? (corrected / (corrected + incorrected) * 100) : 100;

    wpmData.push({x: prev_time_limit - time_limit, y: words_per_min});
    accData.push({x: prev_time_limit - time_limit, y: accuracy});
}