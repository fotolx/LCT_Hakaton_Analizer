document.getElementById('analizator-file').addEventListener('change', function () {
    const fileInput = this;
    const submitButton = document.querySelector('.btn');
    const formAlert = document.querySelector('.analizator-form__alert')

    if (fileInput.files.length > 0) {
        submitButton.removeAttribute('disabled');
        formAlert.innerHTML ='Файл загружен'
    } else {
        submitButton.setAttribute('disabled', true);
    }

});
