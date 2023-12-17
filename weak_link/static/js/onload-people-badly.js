document.getElementById('download-btn').addEventListener('click', function () {
    // Создаем новую книгу Excel
    const wb = XLSX.utils.book_new();

    // Создаем новый лист
    const ws = XLSX.utils.aoa_to_sheet([[]]); // Пустой лист

    // Получаем строки таблицы и проверяем условие
    const tbodyRows = document.querySelectorAll('#table-people tbody tr');
    tbodyRows.forEach(function (row, rowIndex) {
        const numberProbability = parseFloat(row.querySelector('.number-probability').textContent);
        if (numberProbability < 50) {
            const rowData = [];
            const columns = row.querySelectorAll('td');
            columns.forEach(function (column, colIndex) {
                // Добавляем в лист только первые 5 колонок
                if (colIndex < 5) {
                    rowData.push(column.textContent.trim());
                }
            });
            XLSX.utils.sheet_add_aoa(ws, [rowData], { origin: rowIndex });
        }
    });

    // Установка ширины колонок (пример)
    ws['!cols'] = [
        { wch: 25 }, // Ширина первой колонки
        { wch: 20 }, // Ширина второй колонки
        { wch: 25 }, // Ширина третьей колонки
        { wch: 15 }, // Ширина четвертой колонки
        { wch: 20 }, // Ширина пятой колонки
    ];

    // Добавляем лист книги
    XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');

    // Сохраняем книгу в файл
    XLSX.writeFile(wb, 'output.xlsx');
});
