//manipulamos el dom 
const contenidoSend = document.getElementById("contenido")
//para el boton que vamos enviar el contenido
const createBtn = document.getElementById("createPost")

createBtn.addEventListener("click",createPublish)



function createPublish() {
    const contenido = contenidoSend.value;
    if (contenido.trim().length < 0) {
        alert("Escribe algun contenido");
        return;
    }

    // Obtener el token CSRF de la cookie
    const csrfToken = getCookie("csrf_access_token");

    const postData = {
        contenido: contenido
    };

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Agregar el token CSRF al encabezado de la solicitud
            'X-CSRF-TOKEN': csrfToken,
            // Agregar ambas cookies al encabezado de la solicitud
            'Cookie': `access_token_cookie=${getCookie("access_token_cookie")}; csrf_access_token=${csrfToken}`
        },
        body: JSON.stringify(postData)
    };

    // Realizar la solicitud fetch
    fetch("/publish/", options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud');
            }
            alert("publicacion creado correctamente");
            console.log(response);
            return response.json();
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Función para obtener el valor de una cookie por nombre
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
