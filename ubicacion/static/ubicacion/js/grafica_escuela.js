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
    var trabajosCtx = document.getElementById("trabajosChart"); // Id de la grafica.
    var trabajosDataUrl = trabajosCtx.getAttribute("data-url"); // URL con datos en Json
    var trabajosEtiquetas = []; // Etiquetas de la grafica.
    var trabajosDatos = []; // Datos de la grafica
    var trabajosData_dict = {};

    var proyectosCtx = document.getElementById("proyectosChart"); // Id de la grafica.
    var proyectosDataUrl = proyectosCtx.getAttribute("data-url"); // URL con datos en Json
    var proyectosEtiquetas = []; // Etiquetas de la grafica.
    var proyectosDatos = []; // Datos de la grafica
    var proyectosData_dict = {};


    $.ajax({
        url: trabajosDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            trabajosEtiquetas = Object.keys(info);
            trabajosDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: trabajosDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos de Graduacion'
                    }],
                    labels: trabajosEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(trabajosCtx, config);
        }
    });

    $.ajax({
        url: proyectosDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            proyectosEtiquetas = Object.keys(info);
            proyectosDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: proyectosDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos Sustentados'
                    }],
                    labels: proyectosEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(proyectosCtx, config);
        }
    });
};
