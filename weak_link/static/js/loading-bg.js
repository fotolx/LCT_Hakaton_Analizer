const forecastColumn = document.querySelectorAll('.forecast-column')
const numberProbability = document.querySelectorAll('.number-probability');
const load = document.querySelectorAll('.load__bg');

forecastColumn.forEach((el) => {
    const numberProbability = el.querySelectorAll('.number-probability');
    const load = el.querySelectorAll('.load__bg');

    numberProbability.forEach((item) => {
        const itemNumber = parseInt(item.textContent);

        if (itemNumber <= 50) {
            item.style.color = '#48BB78'

        } else if (itemNumber >= 50) {
            item.style.color = '#FF7455'
        }

        load.forEach((loadBg) => {
            const tdElement = loadBg.closest('.forecast-column');
       
            const probabilityElement = tdElement.querySelector('.number-probability');
       
            const probabilityValue = probabilityElement.innerText.replace('%', '');
       
            loadBg.style.width = `${probabilityValue}%`;

            if (itemNumber <= 50) {
                loadBg.style.background = '#48BB78';

            } else if (itemNumber >= 50) {
                loadBg.style.background = '#FF7455';
            }
        });

    });

});

