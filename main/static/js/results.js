function composeResult() {
    let corrected = document.getElementsByClassName('corrected').length;
    let incorrected = document.getElementsByClassName('incorrected').length;

    let wpm = (corrected + incorrected) * 60 / (prev_time_limit - time_limit);
    let accuracy = (corrected + incorrected > 0) ? (corrected / (corrected + incorrected) * 100) : 100;

    return {mode, "time": prev_time_limit, wpm, accuracy};
}

function statisticize() {
    let result = composeResult();
    document.getElementById('wpm').innerHTML = `${result.wpm.toFixed(0)}`;
    document.getElementById('accuracy').innerHTML = `${result.accuracy.toFixed(1)}%`;

    let panel2 = document.getElementById('panel2');
    let typos = Array.from(document.getElementsByClassName('incorrected'));
    while (panel2.firstChild) panel2.firstChild.remove();

    for (let i = 0; i < typos.length; ++i) {
        let p = document.createElement('p');
        let content = document.createTextNode(typos[i].innerHTML);
        p.appendChild(content);
        p.classList.add('text-danger', 'text-center');
        if (i & 1) {p.classList.add('bg-light', 'mb-0')} else {p.classList.add('bg-white', 'mb-0')};
        panel2.appendChild(p);
    };

    if (!typos.length) {
        let p = document.createElement('p');
        let content = document.createTextNode('All corrected, good job!');
        p.appendChild(content);
        p.classList.add('text-success', 'text-center', 'bg-white');
        panel2.appendChild(p);
    }

    panel2.firstChild.classList.add('mt-1');
    panel2.lastChild.classList.add('border-bottom', 'border-success');
}

function drawChart() {
    var chart = new CanvasJS.Chart("lineChart", {
        animationEnabled: true,
        theme: "light2",
        title: {text: "Process"},
        axisX:{
            title: "Time", 
            crosshair: {
                enabled: true,
                snapToDataPoint: true
            }
        },
        axisY: {
            includeZero: true,
            crosshair: {
                enabled: true
            }
        },
        toolTip:{
            shared:true
        },  
        legend:{
            cursor:"pointer",
            verticalAlign: "bottom",
            horizontalAlign: "left",
            dockInsidePlotArea: true,
            itemclick: toogleDataSeries
        },
        data: [{
            type: "line",
            showInLegend: true,
            name: "Words per minute",
            markerType: "square",
            color: "#F08080",
            dataPoints: wpmData
        },
        {
            type: "line",
            showInLegend: true,
            name: "Accuracy",
            lineDashType: "dash",
            dataPoints: accData
        }]
    });

    function toogleDataSeries(e){
        if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
            e.dataSeries.visible = false;
        } else{
            e.dataSeries.visible = true;
        }
        chart.render();
    }

    chart.render();
    $('.canvasjs-chart-canvas').addClass('border border-top-0 border-success');
    $('.canvasjs-chart-credit').hide();
}

function showResults() {
    statisticize();
    drawChart();
    $('#summary').show();
}
