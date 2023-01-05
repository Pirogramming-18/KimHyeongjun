

let stTime = 0;
let endTime = 0;
let timerStart;
 
let sec;
let milisec;
 
const stopwatch = document.getElementById('stopwatch_time');
const startBtn = document.querySelector('.start_button');
const stopBtn = document.querySelector('.stop_button');
const r_button = document.querySelector('.reset_button');
const container = document.querySelector('.container');
const recordList = document.querySelector('.recordList');

startBtn.addEventListener('click', function() {
	// RECORD
    // if(this.innerText == 'RECORD' && milisec) {
    //     console.log(min, sec, milisec);
    //     let li = document.createElement('li');
    //     li.style.color = "#fff";
    //     li.innerText = min + ' : ' + sec + ' : ' + milisec;
    //     if(! recordList.firstChild) {
    //         recordList.append(li);
    //     } else {
    //         recordList.insertBefore(li, recordList.firstChild);
    //     }
    //     return false;
    // }
	
    if(!stTime) {
        stTime = Date.now();	// 최초 START
    } else {
        stTime += (Date.now() - endTime);	// RESTART
    }
 
    timerStart = setInterval(function() {
        let nowTime = new Date(Date.now() - stTime);
 
        sec = addZero(nowTime.getSeconds());
        milisec = addZero(Math.floor(nowTime.getMilliseconds() / 10));
 
        document.getElementById('postTestSec').innerText = sec;
        document.getElementById('postTestMilisec').innerText = milisec;
    }, 1);
})
 
stopBtn.addEventListener('click', function() {
    if(timerStart) {
        clearInterval(timerStart);	// STOP
        endTime = Date.now();
        console.log(min, sec, milisec);
        let li = document.createElement('div');
        // li.style.color = "#fff";
        li.innerText = sec + ' : ' + milisec;
        if(! recordList.firstChild) {
            recordList.append(li);
        } else {
            recordList.insertBefore(li, recordList.firstChild);
        }
    }
})

r_button.addEventListener('click', function() {
    if(timerStart) {
        clearInterval(timerStart);	// STOP
 
        stTime = 0;
        sec = 0;
        milisec = 0;
        document.getElementById('postTestSec').innerText = '00';
        document.getElementById('postTestMilisec').innerText = '00';
        timerStart = null;
        recordList.innerHTML = '';
    }
})
 
function addZero(num) {
    return (num < 10 ? '0'+num : ''+num);
}