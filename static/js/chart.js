const ctx = document.getElementById('myChart');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Four days ago', 'Three days ago', 'Two days ago', 'Yesterday', 'Today'],
        datasets: [{
            label: 'Net Value Bar',
            data: historyData,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,
            order: 0
        }, {
            data: historyData,
            tension: 0,
            backgroundColor:'rgba(200, 14, 133, 0)',
            borderColor: 'rgba(255, 99, 132, 1)',
            type: 'line',
            order: 1,
        }]
    },
    options: {
        responsive: true,
        layout: {
            padding: {
                left: 450,
                right: 450,
            }
        },
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Weekly Portfolio Value'
            }
        }
    }
});