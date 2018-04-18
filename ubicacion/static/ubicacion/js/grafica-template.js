function randomRGB() {
    var colores = [];
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    colores.push('rgb(' + r + ',' + g + ',' + b + ')');  // Centro
    colores.push('rgba(' + r + ',' + g + ',' + b + ',' + 0.5 + ')'); // Borde
    return colores;
};

var chart_data = {};
var etiquetas = [];
var datos = [];
var chartData = {};
var chartDataSet = [];
var ctx = document.getElementById(""); // Id de la grafica.
var dataUrl = estudiantectx.getAttribute("data-url");


window.onload = function () {
    // Adquirir los datos.
    $.ajax({
        url: dataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            etiquetas = info["etiquetas"];
            datos = info["datos"];
        }
    });

    // Asignar las etiquetas. Ej. ["Computadoras", "Laptops", "Teclados"]
    chart_data["labels"] = etiquetas;
    colores = randomRGB();
    for (dato in datos) {
        dataset = {
            "label": "",
            "data": dato,
            backgroundColor: [colores[0]],
            borderColor: [colores[1]],
            borderWidth: 1
        };
        chartDataSet.push(dataset);
    }
    chart_data["datasets"] = chartDataSet;
    // Crear la grafica
    window.myBar = new Chart(ctx, {
        type: "bar",
        data: chartDataSet,
        options: {
            responsive: true,
            legend: {
                position: 'top'
            },
            title: {
                display: true,
                text: ""
            }
        }
    });
};