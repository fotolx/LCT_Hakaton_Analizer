document.addEventListener('DOMContentLoaded', function () {
    const table = document.getElementById('table-people');
    const tbody = table.querySelector('.table-tbody');
    const rows = Array.from(tbody.querySelectorAll('.table-tbody__item'));

    const sortData = {
        'name-sort': { index: 0, type: 'string' },
        'forecast-sort': { index: 1, type: 'number' },
        'deportament-sort': { index: 2, type: 'string' },
        'director-sort': { index: 3, type: 'string' }
    };

    const sortTable = (columnId) => {
        const { index, type } = sortData[columnId];
        const order = table.classList.contains('asc') ? 1 : -1;

        rows.sort((a, b) => {
            const aValue = a.children[index].textContent.trim();
            const bValue = b.children[index].textContent.trim();

            if (type === 'string') {
                return order * aValue.localeCompare(bValue);
            } else if (type === 'number') {
                return order * (parseFloat(aValue) - parseFloat(bValue));
            }
        });

        while (tbody.firstChild) {
            tbody.removeChild(tbody.firstChild);
        }

        rows.forEach((row) => tbody.appendChild(row));

        table.classList.toggle('asc');
    };

    const headerIcons = table.querySelectorAll('.table-header__icon');
    headerIcons.forEach((icon) => {
        icon.addEventListener('click', (event) => {
            const columnId = event.target.id;
            sortTable(columnId);
        });
    });
});