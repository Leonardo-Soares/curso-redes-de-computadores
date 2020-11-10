function validarUsuario() {
  var usuario = document.getElementById('usuario').value;

  if (usuario != '') {
    alert('Usuário prenchido');
  } else {
    alert('Usuário invalido');
  }
}

function usarInnerHTML() {
  document.getElementById('idade').innerHTML = 'Teste iade';
}

var a = 10;

// a = 'Dez';

// a = 10.0;

// a = true;

// document.write(a);
