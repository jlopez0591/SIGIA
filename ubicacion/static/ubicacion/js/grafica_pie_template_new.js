    var keyCtx = document.getElementById("keyChart"); // Id de la grafica.
    var keyDataUrl = keyCtx.getAttribute("data-url"); // URL con datos en Json
    var keyEtiquetas = []; // Etiquetas de la grafica.
    var keyDatos = []; // Datos de la grafica
    var keyData_dict = {};
    
    
    $.ajax({
        url: keyDataUrl,
        type: "GET",
        dataType: 'json',
        success: function (info) {
            keyEtiquetas = Object.keys(info);
            keyDatos = Object.values(info);
            var pieColors = [];
            for (var dato in info) {
                color = randomRGB()[0];
                pieColors.push(randomRGB()[0]);
            }
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: keyDatos,
                        backgroundColor: pieColors,
                        label: 'Trabajos Sustentados'
                    }],
                    labels: keyEtiquetas
                },
                options: {
                    responsive: true
                }
            };
            window.myBar = new Chart(keyCtx, config);
        }
    });
