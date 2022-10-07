function time() {
    seconds--;
    if (seconds === -1) {
        minutes--;
        seconds = 59;
    }
    if (seconds === 0 && minutes === 0) {
        alert('Your time finished and the answers has been submited.')
        submitanswers(0);
    }
    if (seconds < 10) {
        document.querySelector('#time').innerHTML = `0${minutes} : 0${seconds}`;
    } else {
        document.querySelector('#time').innerHTML = `0${minutes} : ${seconds}`;
    }
}

function changepage(direction, len) {
    if (direction === 'next') {
        document.querySelector('#btnbox').style.marginLeft = '770px';
        if (i === len - 2) {
            document.querySelector('#btnbox').style.marginLeft = '748px';
            document.querySelector('#next').innerHTML = 'End test';
        }
        document.querySelector('#previous').style.display = 'inline-block';
        i++;
    }

    else if (direction === 'previous') {
        if (i === 1) {
            document.querySelector('#btnbox').style.marginLeft = '870px';
            document.querySelector('#previous').style.display = 'none';
        }
        if (i === len - 1) {
            document.querySelector('#next').innerHTML = 'Next';
            document.querySelector('#btnbox').style.marginLeft = '770px';

        }
        i--;
    }

    else {
        document.querySelector('#btnbox').style.marginLeft = '870px';
        document.querySelector('#next').style.display = 'inline-block';
        intervalID = setInterval(time, 1000);
    }
}


function showquest(quest) {
    document.querySelector('#questnow').innerHTML = `Question ${i + 1}/${quest.length}`;
    document.querySelector('#question').innerHTML = quest[i];
    if (quest[i].includes("?")) {
        const text = document.createElement('textarea');
        text.placeholder = 'Answer here';
        const submitbtn = document.createElement('button');
        submitbtn.innerHTML = 'submit';
        submitbtn.className = 'btn btn-primary'
        submitbtn.addEventListener('click', () => {
            answer[i] = text.value;
            if (i === quest.length - 1) {
                alert('if you finished answering, press "end test" to submit your answers.')
            } else {
                changepage('next', quest.length);
                showquest(quest);
            }
        });

        document.querySelector('#answerbox').innerHTML = "";
        document.querySelector('#answerbox').append(text);
        document.querySelector('#answerbox').append(submitbtn);

    } else if (quest[i].includes(".")) {
        truebtn = document.createElement('button');
        truebtn.innerHTML = 'True';
        truebtn.className = 'btn btn-primary';
        truebtn.addEventListener('click', () => {
            answer[i] = 'True';

            if (i === quest.length - 1) {
                alert('if you finished answering, press "end test" to submit your answers.')
            } else {
                changepage('next', quest.length);
                showquest(quest);
            }

        });
        falsebtn = document.createElement('button');
        falsebtn.innerHTML = 'False';
        falsebtn.className = 'btn btn-primary';
        falsebtn.addEventListener('click', () => {
            answer[i] = 'False';
            if (i === quest.length - 1) {
                alert('if you finished answering, press "end test" to submit your answers.')
            } else {

                changepage('next', quest.length);
                showquest(quest);
            }
        });
        document.querySelector('#answerbox').innerHTML = "";
        document.querySelector('#answerbox').append(truebtn);
        document.querySelector('#answerbox').append(falsebtn);

    }
}


function submitanswers(len) {
    empty = []
    if (len != 0) {
        for (let j = 0; j < len; j++) {
            if (!answer[j]) {
                empty.push(j + 1)
            }
        }
    }

    if (empty.length > 0) {
        alert(`You did not answer questions ${empty}`);
    }
    else {
        fetch(`/exam/${title}`, {
            method: 'post',
            body: JSON.stringify({

                answers: answer

            }), headers: { "X-CSRFToken": csrftoken },
            credentials: 'same-origin'
        })
        clearInterval(intervalID);
        document.querySelector('#answerbox').innerHTML = "";
        document.querySelector('#btnbox').innerHTML = "";
        document.querySelector('#time').innerHTML = "";
        document.querySelector('#questnow').innerHTML ="";
        document.querySelector('#questionbox').style.textAlign = 'center';
        document.querySelector('#question').innerHTML = 'Your answers have submited and you can see your score in the score page.';
        
        window.setTimeout(() => { window.location.href = indexurl }, 5000);


    }


}