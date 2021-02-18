document.addEventListener('DOMContentLoaded', ()=>{
    axios.get(`/referencial/sala/get_salas`).then(
        ({data}) => {
            const tbody = document.getElementById('tb');
            let cadena = "";
            data.map(({id, description}) => {
                cadena += `<tr><td>${id}</td>
                <td>${description}</td></tr>`
            })
            tbody.innerHTML = `${cadena}`;
        }
    )
})