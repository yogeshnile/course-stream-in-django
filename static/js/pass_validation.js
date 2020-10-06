// current password validation coding. 
const currentPasswordField = document.querySelector('#currentPassword');
const feedbackpassword = document.querySelector('.password-key-error');
const button = document.querySelector('#chapass');
currentPasswordField.addEventListener("keyup", (e) => {
    const usernameval = e.target.value;

    currentPasswordField.classList.remove("is-invalid");
    currentPasswordField.classList.remove("is-valid");
    feedbackpassword.style.display = "none";
    button.disabled = false;

    if (usernameval.length > 0) {
        fetch('/validate/password', {
            body: JSON.stringify({ password: usernameval }), method: "POST",
        }).then(res => res.json()).then(data => {
            if (data.password_error) {
                currentPasswordField.classList.add("is-invalid");
                feedbackpassword.style.display = "block";
                feedbackpassword.innerHTML = `<small>${data.password_error}</small>`;
                button.disabled = true;
            } else if (data.password_valid) {
                currentPasswordField.classList.add("is-valid");
            }
        });
    }
});

// Password SHOW and HIDE current pass.
const showpassword = document.querySelector('.currentpassword');
const password = document.querySelector('.currentpass');
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

// New password show and hide 
const newshowpassword = document.querySelector('.newpass');
const newpassword = document.querySelector('.newpassword');
const handelToggleinputnew = (e) => {
    if (newshowpassword.textContent === 'SHOW') {
        newshowpassword.textContent = 'HIDE';
        newpassword.setAttribute("type", "text");
    } else {
        newshowpassword.textContent = 'SHOW';
        newpassword.setAttribute("type", "password");
    }
};
newshowpassword.addEventListener('click', handelToggleinputnew);