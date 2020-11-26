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
    statisticizer = setInterval(calculateStep, 1000*(prev_time_limit/10));
}

function counting() {
    document.getElementById("time-button").innerHTML = --time_limit;
    if (time_limit == 0) {
        clearIntervals();
        showResults();
        saveResultsToDB();
    }
}

function calculateStep() {
    let result = composeResult();
    wpmData.push({x: prev_time_limit - time_limit, y: result.wpm});
    accData.push({x: prev_time_limit - time_limit, y: result.accuracy});
}