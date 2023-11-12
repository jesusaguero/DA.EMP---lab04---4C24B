<?php
$apellido = $_POST['apellido'];
$contrasena = $_POST['contrasena'];

if ($apellido === "aguero" && $contrasena === "123") {
    header("Location: calculo.html");
    exit();
} else {
    // Credenciales incorrectas, redirige al usuario de vuelta al formulario de inicio de sesión
    header("Location: login.html");
    exit();
}
?>
