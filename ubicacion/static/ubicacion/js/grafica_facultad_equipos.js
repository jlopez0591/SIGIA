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
    var etiquetas = []; // Etiquetas de la grafica.
    var datos = []; // Datos de la grafica
    var ctx = document.getElementById("recursosChart"); // Id de la grafica.
    var dataUrl = ctx.getAttribute("data-url"); // URL con datos en Json
    var datasets = [];
    var label = "Equipos por categoria";
    var chartData = {};

    // Adquirir los datos.
    $.ajax({
        url: dataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            etiquetas = Object.keys(info);
            datos = Object.values(info);
            // data_dict = {
            //     'computadora': 50,
            //     'laptop': 20
            // } // Esto es lo que viene del JSON.
            // etiquetas = ['computadora', 'laptop']
            // datos = [50, 20]

            // Asignar las etiquetas. Ej. ["Computadoras", "Laptops", "Teclados"]
            colores = randomRGB();
            chartData["labels"] = etiquetas;

            // chartData = {
            //     "labels": ["computadora", "laptop"]
            // }


            var dataset = {
                label: "Cantidad en Inventario",
                data: datos,
                backgroundColor: colores[0],
                borderColor: colores[1],
                borderWidth: 1
            };

            //chartDataSet.push(dataset);
            datasets.push(dataset);
            // datasets = [
            //     {
            //         "label": "Cantidad en Inventario",
            //         "data": [50, 20],
            //         "backgroundColor": "Red",
            //         "borderColor": "Red",
            //         "borderWidth": 1
            //     }
            // ]


            chartData["datasets"] = datasets;

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

            console.log(chartData);

            // Crear la grafica
            window.myBar = new Chart(ctx, {
                type: "bar",
                data: chartData,
                options: {
                    responsive: true,
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: false,
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

        }
    });

    /**
     * Generar grafica de aulas.
     */

    var aulaEtiquetas = [];
    var aulaDatos = [];
    var aulaCtx = document.getElementById("aulasChart");
    var aulaDataUrl = aulaCtx.getAttribute("data-url");
    var aulaDatasets = [];
    var aulaLabel = "Aulas por categoria";
    var aulaChartData = {};

    $.ajax({
        url: aulaDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            aulaEtiquetas = Object.keys(info);
            aulaDatos = Object.values(info);
            aulaColores = randomRGB();
            aulaChartData["labels"] = aulaEtiquetas;


            var aulaDataset = {
                label: "Aulas",
                data: aulaDatos,
                backgroundColor: aulaColores[0],
                borderColor: aulaColores[1],
                borderWidth: 1
            };

            aulaDatasets.push(aulaDataset);


            aulaChartData["datasets"] = aulaDatasets;

            console.log(aulaChartData);

            window.aulaMyBar = new Chart(aulaCtx, {
                type: "bar",
                data: aulaChartData,
                options: {
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: false,
                        text: "Aulas por Categoria"
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
        }
    });


};
