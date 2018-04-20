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

    var pieColors = [];

    for (dato in keyDatos) {
        pieColors.push(randomRGB()[0]);
    }


    var config = {
        type: 'pie',
        data: {
            datasets: [{
                data: keyDatos,
                backgroundColor: pieColors,
                label: 'Trabajos de Graduacion'
            }],
            labels: keyEtiquetas
        },
        options: {
            responsive: true
        }
    };

    console.log(config);

    window.myBar = new Chart(keyCtx, config);
};
