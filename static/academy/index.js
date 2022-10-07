csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

document.addEventListener('DOMContentLoaded', () => {
    if (window.matchMedia("(orientation: portrait)").matches) {
        document.body.innerHTML = "";
        const element = document.createElement('h1');
        element.innerHTML = " Please rotate your device and reload to load the page properly."
        document.body.style.textAlign = 'center';
        document.body.style.marginTop = '290px';
        document.body.append(element);
    }
});


function add(btn, coursename, place, taken) {
    if (document.querySelector(`#${place}`).innerHTML === '') {
        if (taken < 3) {


            fetch(`/schedule`, {
                method: 'post',
                body: JSON.stringify({

                    coursename: coursename

                }), headers: { "X-CSRFToken": csrftoken },
                credentials: 'same-origin'
            });
            document.querySelector(`#${place}`).innerHTML = coursename;
            btn.parentElement.remove();
        } else {
            alert("You can not take more than three courses at the same time.")
        }
    } else {
        alert("the time of this class interferes with your other class!");
        document.querySelector(`#${place}`).style.backgroundColor = 'red';
    }


}