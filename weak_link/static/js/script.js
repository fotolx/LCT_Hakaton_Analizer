document.getElementById('authorizationForm').addEventListener('input', ()=> {
    const authorizationName = document.getElementById('authorization-name').value;
    const authorizationPassword = document.getElementById('authorization-password').value;
    const authorizationBtn = document.getElementById('authorizationBtn');

    if (authorizationName.trim() !== '' && authorizationPassword.trim() !== '') {
        authorizationBtn.removeAttribute('disabled');
    } else {
        authorizationBtn.setAttribute('disabled', true);
    }
});
