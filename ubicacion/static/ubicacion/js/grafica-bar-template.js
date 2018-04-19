window.onload = function () {

    function randomRGB() {
        var colores = [];
        var r = Math.floor(Math.random() * 256);
        var g = Math.floor(Math.random() * 256);
        var b = Math.floor(Math.random() * 256);
        colores.push('rgb(' + r + ',' + g + ',' + b + ')');  // Centro
        colores.push('rgba(' + r + ',' + g + ',' + b + ',' + 0.5 + ')'); // Borde
        return colores;
    };
    
    // En Uso
    var keyEtiquetas = []; // Etiquetas de la grafica.
    var keyDatos = []; // Datos de la grafica
    var keyCtx = document.getElementById("keyChart"); // Id de la grafica.
    var keyDataUrl = ctx.getAttribute("data-url"); // URL con datos en Json
    var keyDatasets = [];
    var keyLabel = "Equipos por categoria";
    var keyChartData = {};
    
    // Adquirir los datos.
    $.ajax({
        url: keyDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            for (var dato in info) {
                keyData_dict = info;
                keyEtiquetas.push(dato);
                keyDatos.push(info[dato]);
            }
        }
    });
    // data_dict = {
    //     'computadora': 50,
    //     'laptop': 20
    // } // Esto es lo que viene del JSON.
    // etiquetas = ['computadora', 'laptop']
    // datos = [50, 20]

    // Asignar las etiquetas. Ej. ["Computadoras", "Laptops", "Teclados"]
    keyColores = randomRGB();
    keyChartData["labels"] = keyEtiquetas;

    // chartData = {
    //     "labels": ["computadora", "laptop"]
    // }

    
    var keyDataset = {
        label: "Cantidad en Inventario",
        data: keyDatos,
        backgroundColor: keyColores[0],
        borderColor: keyColores[1],
        borderWidth: 1
    };

    //chartDataSet.push(dataset);
    keyDatasets.push(keyDataset);
    // datasets = [
    //     {
    //         "label": "Cantidad en Inventario",
    //         "data": [50, 20],
    //         "backgroundColor": "Red",
    //         "borderColor": "Red",
    //         "borderWidth": 1
    //     }
    // ]


    keyChartData["datasets"] = keyDatasets;

    // chartData = {
    //     "labels": ["computadora", "laptop"],
    //     "datasets": [{
    //         "label": "Cantidad en Inventario",
    //         "data": [
    //             50,
    //             20
    //         ],
    //         backgroundColor: "Red",
    //         borderColor: "Red",
    //         borderWidth: 1
    //     }]
    // }

    console.log(keyChartData);

    // Crear la grafica
    window.myBar = new Chart(keyCtx, {
        type: "bar",
        data: keyChartData,
        options: {
            responsive: true,
            legend: {
                position: 'top'
            },
            title: {
                display: true,
                text: "Cantidad de recursos por categoria."
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
};
