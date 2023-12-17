document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('analizator-Chart').getContext('2d');
    const selectData = document.getElementById('select-data');
    const sendMessageNumber = document.querySelector('.chart-header__group.send-message .chart-header__number').textContent;
    const receivedMessageNumber = document.querySelector('.chart-header__group.received-message .chart-header__number').textContent;

    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [], 
            datasets: [
                {
                    label: 'Отправленные сообщения',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: sendMessageNumber,
                },
                {
                    label: 'Полученные сообщения',
                    backgroundColor: 'rgba(255, 116, 85, 0.3)',
                    borderColor: 'rgba(255, 116, 85, 1)',
                    borderWidth: 1,
                    data: receivedMessageNumber,
                },
            ],
        },
        options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                display: true,
                position: 'top'
            }
        },
        layout: {
            padding: {
                left: 10,
                right: 10,
                top: 0,
                bottom: 0
            }
        },
        indexAxis: 'x',
        barPercentage: 1, 
        categoryPercentage: 1
      }
    });

  const selectedPeriod = selectData.value;

        fetch(window.location.href+'/chart/', {
            method: 'GET', 
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {

            chart.data.labels = data.periods; 
            chart.data.datasets[0].data = data.data; 
            chart.data.datasets[1].data = data.msgs_sent;

            chart.update();
        })
        .catch(error => console.error('Ошибка при получении данных с сервера', error));
})
