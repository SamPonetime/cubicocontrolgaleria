const nombre = document.getElementById("name")
const correo = document.getElementById("email")
const telefono = document.getElementById("cellphone")
const mensaje = document.getElementById("message")
const formulario = document.getElementById("formulario")
const advertencias = document.getElementById("warnings")
  
const btn = document.getElementById('button');

formulario.addEventListener('submit', function(event) {
    event.preventDefault();
    
    let warnings = ""
    let entrar = false;
    let regexEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
    

    if(nombre.value.length <6){
        warnings += 'El nombre ingresado no es válido <br>'
        entrar = true
    }
    if(!regexEmail.test(email.value)){
        warnings += 'El email no es válido <br>'
        entrar = true
    }
    if(isNaN(telefono.value)||telefono.value.length <10){ /*Validación únicamente numeros y longitud minima*/
       warnings += 'El número ingresado no es válido <br>'
        entrar = true
   }
    if(mensaje.value==""){
        warnings += 'El campo "Mensaje" no puede estar vacío'
        entrar = true
   
    }
 
    if(!entrar){ 
        advertencias.innerHTML = "";
        btn.value = 'Enviando...';
        
        const serviceID = 'default_service';
        const templateID = 'template_518rd0q';
        
        emailjs.sendForm(serviceID, templateID, this)
            .then(() => {
            btn.value = 'Enviar';
            alert('¡Tu correo ha sido enviado!');
            }, (err) => {
            btn.value = 'Enviar';
            alert(JSON.stringify(err));
            });
    } 
    else {
        advertencias.innerHTML = warnings 
    }

   
    
 });  







 
 
 
            

             
            