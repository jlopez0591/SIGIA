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

    var profesoresCtx = document.getElementById("profesoresChart"); // Id de la grafica.
    var profesoresDataUrl = profesoresCtx.getAttribute("data-url"); // URL con datos en Json
    var profesoresEtiquetas = []; // Etiquetas de la grafica.
    var profesoresDatos = []; // Datos de la grafica
    var profesoresData_dict = {};
    var tipoCtx = document.getElementById("tipoChart");
    var tipoDataUrl = tipoCtx.getAttribute("data-url");
    var tipoEtiquetas = [];
    var tipoDatos = [];
    var tipoData_dict = {};
    
    
    
    
    $.ajax({
        url: profesoresDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            profesoresEtiquetas = Object.keys(info);
            profesoresDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: profesoresDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos Sustentados'
                    }],
                    labels: profesoresEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(profesoresCtx, config);
        }
    });

  
    $.ajax({
        url: tipoDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            tipoEtiquetas = Object.keys(info);
            tipoDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: tipoDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos Sustentados'
                    }],
                    labels: tipoEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(tipoCtx, config);
        }
    });

    var estadoCtx = document.getElementById("estadoChart"); // Id de la grafica.
    var estadoDataUrl = estadoCtx.getAttribute("data-url"); // URL con datos en Json
    var estadoEtiquetas = []; // Etiquetas de la grafica.
    var estadoDatos = []; // Datos de la grafica
    var estadoData_dict = {};
    
    
    $.ajax({
        url: estadoDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            estadoEtiquetas = Object.keys(info);
            estadoDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: estadoDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos Sustentados'
                    }],
                    labels: estadoEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(estadoCtx, config);
        }
    });



};
