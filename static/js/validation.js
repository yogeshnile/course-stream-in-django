const button = document.querySelector('#registersubmit');

// Password SHOW and HIDE coding.
const showpassword = document.querySelector('.showpassword');
const password = document.querySelector('.passwordshow');
const handelToggleinput = (e) => {
    if (showpassword.textContent === 'SHOW') {
        showpassword.textContent = 'HIDE';
        password.setAttribute("type", "text");
    } else {
        showpassword.textContent = 'SHOW';
        password.setAttribute("type", "password");
    }
};
showpassword.addEventListener('click', handelToggleinput);

// Password SHOW and HIDE coding for singUp.
const showpasswordSignup = document.querySelector('.showpasswordsingup');
const passwordSingup = document.querySelector('.passwordshowsingup');
const handelToggleinputSingup = (e) => {
    if (showpasswordSignup.textContent === 'SHOW') {
        showpasswordSignup.textContent = 'HIDE';
        passwordSingup.setAttribute("type", "text");
    } else {
        showpasswordSignup.textContent = 'SHOW';
        passwordSingup.setAttribute("type", "password");
    }
};
showpasswordSignup.addEventListener('click', handelToggleinputSingup);

// Ragister email validation coding. 
const email = document.querySelector('#emailid');
const feedbackemail = document.querySelector('.key-error-email');
email.addEventListener('keyup', (e) => {
    const emailval = e.target.value;
    //console.log('usernameval', usernameval);

    email.classList.remove("is-invalid");
    feedbackemail.style.display = "none";
    button.disabled = false;

    if (emailval.length > 0) {
        fetch('/validate/email', {
            body: JSON.stringify({ emailid: emailval }), method: "POST",
        }).then(res => res.json()).then(data => {
            //console.log('data', data);
            if (data.email_error) {
                email.classList.add("is-invalid");
                feedbackemail.style.display = "block";
                feedbackemail.innerHTML = `<small>${data.email_error}</small>`;
                button.disabled = true;
            }
        });
    }
});

// ragister username validation coding. 
const usernameField = document.querySelector('#username');
const feedbackusername = document.querySelector('.key-error-username');
usernameField.addEventListener("keyup", (e) => {
    const usernameval = e.target.value;
    //console.log('usernameval', usernameval);

    usernameField.classList.remove("is-invalid");
    feedbackusername.style.display = "none";
    button.disabled = false;

    if (usernameval.length > 0) {
        fetch('/validate/username', {
            body: JSON.stringify({ username: usernameval }), method: "POST",
        }).then(res => res.json()).then(data => {
            //console.log('data', data);
            if (data.username_error) {
                usernameField.classList.add("is-invalid");
                feedbackusername.style.display = "block";
                feedbackusername.innerHTML = `<small>${data.username_error}</small>`;
                button.disabled = true;
            }
        });
    }
});

const loginbutton = document.querySelector('#loginsubmit');

// Login Username validation coding.
const loginusernameField = document.querySelector('#login_username');
const loginfeedbackusername = document.querySelector('.login-key-error-username');
loginusernameField.addEventListener("keyup", (e) => {
    const usernameval = e.target.value;
    //console.log('usernameval', usernameval);

    loginusernameField.classList.remove("is-invalid");
    loginusernameField.classList.remove("is-valid");
    loginfeedbackusername.style.display = "none";
    loginbutton.disabled = false;

    if (usernameval.length > 0) {
        fetch('/validate/login-username', {
            body: JSON.stringify({ login_username: usernameval }), method: "POST",
        }).then(res => res.json()).then(data => {
            //console.log('data', data);
            if (data.login_username_error) {
                loginusernameField.classList.add("is-invalid");
                loginfeedbackusername.style.display = "block";
                loginfeedbackusername.innerHTML = `<small>${data.login_username_error}</small>`;
                loginbutton.disabled = true;
            } else if (data.login_username_valid) {
                loginusernameField.classList.add("is-valid");
            }
        });
    }
});