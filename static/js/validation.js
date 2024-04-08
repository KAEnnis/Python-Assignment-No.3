document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const email = document.getElementById('email').value;
        const usernameError = document.getElementById('username-error');
        const passwordError = document.getElementById('password-error');
        const emailError = document.getElementById('email-error');
        let isValid = true;

        if (!/^[a-zA-Z0-9]{6,}$/.test(username)) {
            usernameError.textContent = 'Username must be alphanumeric and at least 6 characters long.';
            isValid = false;
        } else {
            usernameError.textContent = '';
        }

        if (password.length < 8) {
            passwordError.textContent = 'Password must be at least 8 characters long.';
            isValid = false;
        } else {
            passwordError.textContent = '';
        }

        if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
            emailError.textContent = 'Invalid email address.';
            isValid = false;
        } else {
            emailError.textContent = '';
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});