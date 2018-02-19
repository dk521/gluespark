var barChartData = {
    labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"],
    datasets: [{
        fillColor: 'tomato',
    strokeColor: "black",
    data: [10, 20, 30, 40, 50]
}]
}

var ctx = document.getElementById("canvas").getContext("2d");
var barChartDemo = new Chart(ctx).Bar(barChartData, {
responsive: true,
barValueSpacing: 2
});

