let btn = document.getElementById('search'),
    select = document.getElementById('select'),
    head = document.getElementById('head'),
    body = document.getElementById('body'),
    datein = document.getElementById('datein'),
    datefi = document.getElementById('datefi');


const renderGeneral = (element) => 
{
    return `
    <tr>
        <th scope="row">${element.Id}</th>
        <td>${element.NombreServicio}</td>
        <td>${element.cantidad}</td>
    </tr>
    `
}

const renderPersona = (element) => 
{
    return `
    <tr>
        <th scope="row">${element.Id}</th>
        <td>${element.Nombre}</td>
        <td>${element.TotalGastado}</td>
    </tr>
    `
}
const renderGenero = (element) => 
{
    return `
    <tr>
        <th scope="row">#</th>
        <td>${element.Genero}</td>
        <td>${element.Cantidad}</td>
    </tr>
    `
}
const renderVip = (element) => 
{
    return `
    <tr>
        <th scope="row">#</th>
        <td>${element.Direccion}</td>
        <td>${element.Nombre}</td>
        <td>${element.cantidad}</td>
    </tr>
    `
}
const renderSer = (element) => 
{
    return `
    <tr>
        <th scope="row">#</th>
        <td>${element.Direccion}</td>
        <td>${element.NombreServicio}</td>
        <td>${element.cantidad}</td>
    </tr>
    `
}
const renderGas = (element) => 
{
    return `
    <tr>
        <th scope="row">#</th>
        <td>${element.Direccion}</td>
        <td>${element.Nombre}</td>
        <td>${element.TotalGastado}</td>
        <td>${element.cantidad}</td>
    </tr>
    `
}
const renderGenSuc = (element) => 
{
    return `
    <tr>
        <th scope="row">#</th>
        <td>${element.Direccion}</td>
        <td>${element.Genero}</td>
        <td>${element.Cantidad}</td>
    </tr>
    `
}


btn.addEventListener('click', () => {
   if(datein.value == "" || datefi.value == "") alert("envie fechas para realizar el reporte")
    switch (select.value){
        case "1":
            head.innerHTML = null
            head.innerHTML = `<tr>
            <th scope="col">#</th>
            <th scope="col">Nombre Servicio</th>
            <th scope="col">cantidad</th>
          </tr>`
          const url = fetch(`http://localhost:3000/general`,{
            method: 'POST',
            body : JSON.stringify({FechaInicial: datein.value, FechaFinal : datefi.value}),
            headers : {'Content-Type': 'application/json'}
            })
            url.then(res => res.json())
                .then(data => {
                    body.innerHTML = null
                    data.forEach(element => {
                        body.innerHTML += renderGeneral(element)
                    });
                })
                .catch(error => console.log(error))
        
            break;
        case "2":
            head.innerHTML = null
            head.innerHTML = `<tr>
            <th scope="col">#</th>
            <th scope="col">Nombre Completo</th>
            <th scope="col">Total Gastado</th>
          </tr>`
            const url2 = fetch(`http://localhost:3000/persona`,{
                method: 'POST',
                body : JSON.stringify({FechaInicial: datein.value, FechaFinal : datefi.value}),
                headers : {'Content-Type': 'application/json'}
                })
                url2.then(res => res.json())
                    .then(data => {
                        body.innerHTML = null
                        data.forEach(element => {
                            body.innerHTML += renderPersona(element)
                        });
                    })
                    .catch(error => console.log(error))
            break;
        case "3":
            head.innerHTML = null
            head.innerHTML = `<tr>
            <th scope="col">#</th>
            <th scope="col">Genero</th>
            <th scope="col">Cantidad</th>
          </tr>`
            const url3 = fetch(`http://localhost:3000/genero`,{
                method: 'POST',
                body : JSON.stringify({FechaInicial: datein.value, FechaFinal : datefi.value}),
                headers : {'Content-Type': 'application/json'}
                })
                url3.then(res => res.json())
                    .then(data => {
                        body.innerHTML = null
                        data.forEach(element => {
                            body.innerHTML += renderGenero(element)
                        });
                    })
                    .catch(error => console.log(error))
            break;
        case "4":
            head.innerHTML = null
            head.innerHTML = `<tr>
            <th scope="col">#</th>
            <th scope="col">Direccion</th>
            <th scope="col">Nombre</th>
            <th scope="col">Cantidad</th>
          </tr>`
            const url4 = fetch(`http://localhost:3000/vipSucursal`,{
                method: 'POST',
                body : JSON.stringify({FechaInicial: datein.value, FechaFinal : datefi.value}),
                headers : {'Content-Type': 'application/json'}
                })
                url4.then(res => res.json())
                    .then(data => {
                        body.innerHTML = null
                        data.forEach(element => {
                            body.innerHTML += renderVip(element)
                        });
                    })
                    .catch(error => console.log(error))
            break;
        case "5":
            head.innerHTML = null
            head.innerHTML = `<tr>
            <th scope="col">#</th>
            <th scope="col">Direccion</th>
            <th scope="col">Nombre</th>
            <th scope="col">Cantidad</th>
          </tr>`
            const url5 = fetch(`http://localhost:3000/servicioSucursal`,{
                method: 'POST',
                body : JSON.stringify({FechaInicial: datein.value, FechaFinal : datefi.value}),
                headers : {'Content-Type': 'application/json'}
                })
                url5.then(res => res.json())
                    .then(data => {
                        body.innerHTML = null
                        data.forEach(element => {
                            body.innerHTML += renderSer(element)
                        });
                    })
                    .catch(error => console.log(error))
            break;
        case "6":
            head.innerHTML = null
            head.innerHTML = `<tr>
            <th scope="col">#</th>
            <th scope="col">Direccion</th>
            <th scope="col">Nombre</th>
            <th scope="col">Total Gastado</th>
            <th scope="col">Cantidad</th>
          </tr>`
            const url6 = fetch(`http://localhost:3000/gastoSucursal`,{
                method: 'POST',
                body : JSON.stringify({FechaInicial: datein.value, FechaFinal : datefi.value}),
                headers : {'Content-Type': 'application/json'}
                })
                url6.then(res => res.json())
                    .then(data => {
                        body.innerHTML = null
                        data.forEach(element => {
                            body.innerHTML += renderGas(element)
                        });
                    })
                    .catch(error => console.log(error))
            break;
        case "7":
            head.innerHTML = null
            head.innerHTML = `<tr>
            <th scope="col">#</th>
            <th scope="col">Direccion</th>
            <th scope="col">Genero</th>
            <th scope="col">Cantidad</th>
          </tr>`
            const url7 = fetch(`http://localhost:3000/generoSucursal`,{
                method: 'POST',
                body : JSON.stringify({FechaInicial: datein.value, FechaFinal : datefi.value}),
                headers : {'Content-Type': 'application/json'}
                })
                url7.then(res => res.json())
                    .then(data => {
                        body.innerHTML = null
                        data.forEach(element => {
                            body.innerHTML += renderGenSuc(element)
                        });
                    })
                    .catch(error => console.log(error))
            break;
        default:
            alert("seleccione un opcion")
    }
    

})