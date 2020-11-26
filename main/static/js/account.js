let inMemoryToken;
let tokenType;

$(document).ready(function () {
    $('#username, #password').keypress(function(event) {
        if (event.keyCode === 13) {
            login();
        }
    });
});

function getUserData() {
    return {
        "username": document.getElementById("username").value,
        "password": document.getElementById("password").value
    }
}

async function displayAccount() {
    await getUserStatistic();
    $('.sec').hide();
    $('#sec-account').show();
}

$('#nav-account').click(function () {
    if (!inMemoryToken) {
        $('#enrollModal').modal('show');
        //displayAccount();
    }
    else {
        displayAccount();
    }
});

function processResponse(jsonResponse, status) {
    document.getElementById('error-message').innerHTML = jsonResponse.message;
    document.getElementById('error-message').classList.remove('d-none');
    document.getElementById('error-message').style.color = ((status == 201) ? 'green' : 'red');
    if ('error_info' in jsonResponse) {
        let errors = ['username', 'password'];
        for (err of errors) {
            if (err in jsonResponse.error_info) {
                console.log(document.getElementById(err));
                document.getElementById(`${err}-error-message`).innerHTML = jsonResponse.error_info[err][0]; 
                document.getElementById(`${err}-error-message`).classList.remove('d-none');
                document.getElementById(`${err}`).parentElement.classList.add('form-group-customized');
            }
            else {
                document.getElementById(`${err}-error-message`).classList.add('d-none');
                document.getElementById(`${err}`).parentElement.classList.remove('form-group-customized');
            }
        }
    }
}

async function login() {
    let response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify(getUserData())
    });
    let jsonResponse = await response.json();
    processResponse(jsonResponse, response.status);
    if (response.status == 200) {
        inMemoryToken = jsonResponse.access_token;
        tokenType = jsonResponse.token_type;

        $('#enrollModal').modal('hide');
        displayAccount();
    } else 
    if (response.status == 500) {
        console.log(response.message);
    }
}

async function register() {
    let response = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify(getUserData())
    });
    let jsonResponse = await response.json();
    processResponse(jsonResponse, response.status)
    if (response.status == 500) {
        console.log(response.message);
    }
}

async function saveResultsToDB() {
    // if not logged in
    if (!inMemoryToken) {
        return;
    }

    // logged in
    let response = await fetch('/results', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'Authorization': `${tokenType} ${inMemoryToken}`
        },
        body: JSON.stringify(composeResult())
    });
    let jsonResponse = await response.json();
    if (response.status == 201) {
        console.log("Saving result successfully.");
    }
    else {
        console.log(jsonResponse.message);
    }
}

async function getUserStatistic() {
    let response = await fetch('/results', {
        method: 'GET',
        headers: {
            'Content-type': 'application/json',
            'Authorization': `${tokenType} ${inMemoryToken}`
        }
    });
    let jsonResponse = await response.json();
    if (response.status == 200) {
        document.getElementById('username-in-card').innerHTML = jsonResponse.username;
        mins_practiced = parseInt(jsonResponse.time_practiced) / 60;
        document.getElementById('time-practiced').innerHTML = String(mins_practiced + ' mins');
        document.getElementById('overall-wpm').innerHTML = jsonResponse.overall_wpm.toFixed(2);
        document.getElementById('overall-acc').innerHTML = jsonResponse.overall_acc.toFixed(2);
        document.getElementById('overall-acc-bar').style.width = String(jsonResponse.overall_acc.toFixed(2) + '%')
        document.getElementById('recent-wpm').innerHTML = jsonResponse.recent_wpm.toFixed(2);
        document.getElementById('recent-acc').innerHTML = jsonResponse.recent_acc.toFixed(2);
        document.getElementById('recent-acc-bar').style.width = String(jsonResponse.recent_acc.toFixed(2) + '%')
    }
    else {
        console.log(jsonResponse.message);
    }
}