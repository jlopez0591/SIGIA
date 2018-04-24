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

    var estudiantesCtx = document.getElementById("estudiantesChart"); // Id de la grafica.
    var estudiantesDataUrl = estudiantesCtx.getAttribute("data-url"); // URL con datos en Json
    var estudiantesEtiquetas = []; // Etiquetas de la grafica.
    var estudiantesDatos = []; // Datos de la grafica
    var estudiantesData_dict = {};
    
    
    $.ajax({
        url: estudiantesDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            estudiantesEtiquetas = Object.keys(info);
            estudiantesDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: estudiantesDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos Sustentados'
                    }],
                    labels: estudiantesEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(estudiantesCtx, config);
        }
    });


    var estadosCtx = document.getElementById("estadosChart"); // Id de la grafica.
    var estadosDataUrl = estadosCtx.getAttribute("data-url"); // URL con datos en Json
    var estadosEtiquetas = []; // Etiquetas de la grafica.
    var estadosDatos = []; // Datos de la grafica
    var estadosData_dict = {};
    
    
    $.ajax({
        url: estadosDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            estadosEtiquetas = Object.keys(info);
            estadosDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: estadosDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos Sustentados'
                    }],
                    labels: estadosEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(estadosCtx, config);
        }
    });

    var categoriasCtx = document.getElementById("categoriasChart"); // Id de la grafica.
    var categoriasDataUrl = categoriasCtx.getAttribute("data-url"); // URL con datos en Json
    var categoriasEtiquetas = []; // Etiquetas de la grafica.
    var categoriasDatos = []; // Datos de la grafica
    var categoriasData_dict = {};
    
    
    $.ajax({
        url: categoriasDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            categoriasEtiquetas = Object.keys(info);
            categoriasDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: categoriasDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos Sustentados'
                    }],
                    labels: categoriasEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(categoriasCtx, config);
        }
    });
};
