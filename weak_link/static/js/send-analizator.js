document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('.save-form');
    
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        
        // Собираем данные из формы
        var director = form.querySelector('#save-form-director').value;
        var department = form.querySelector('#save-form__deportament').value;
        var message = form.querySelector('#save-form__massage').value;
        
        // Собираем данные из таблицы
        var tableRows = document.querySelectorAll('.table-tbody__item');
        var tableData = [];
        
        tableRows.forEach(function (row) {
            var rowData = {
                name: row.querySelector('.name-column__title').textContent,
                probability: row.querySelector('.number-probability').textContent,
                department: row.querySelector('.deportament-column__text').textContent,
                director: row.querySelector('.director-column__text').textContent,
                date: row.querySelector('.data-column__text').textContent
            };
            
            tableData.push(rowData);
        });
        
        // Отправляем данные на сервер
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'mail/mail.php', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        
        xhr.onload = function () {
            if (xhr.status === 200) {
                alert('Данные успешно отправлены!');
            } else {
                alert('Произошла ошибка при отправке данных.');
            }
        };
        
        xhr.send(JSON.stringify({
            director: director,
            department: department,
            message: message,
            tableData: tableData
        }));
    });
});