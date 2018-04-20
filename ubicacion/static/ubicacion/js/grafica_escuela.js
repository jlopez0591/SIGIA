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
    // Adquirir los datos.
    $.ajax({
        url: trabajosDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            trabajosData_dict = info;
            trabajosEtiquetas= Object.keys(info);
            trabajosDatos = Object.values(info);
        }
    });

    var pieColors = [];

    for (var dato in trabajosDatos) {
        color = randomRGB()[0];
        console.log(color);
        pieColors.push(randomRGB()[0]);
    }

    console.log("Antes del config");
    console.log(trabajosDatos);
    for (var test; test <= trabajosDatos.length; test++) {
        console.log("Hola");
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

    console.log(config);

    window.myBar = new Chart(trabajosCtx, config);
    window.myBar.update()
};
