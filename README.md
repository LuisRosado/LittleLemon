# API Endpoints - Little Lemon Restaurant

## Endpoints Públicos
1. Página Principal
   Ruta: /
   Método: GET

2. Panel de Administración
   Ruta: /admin/
   Método: GET

## Endpoints de Menú
1. Lista de Elementos del Menú
   Ruta: /restaurant/menu-items/
   Método: GET
   Auth: Token requerido

2. Detalle de Elemento del Menú
   Ruta: /restaurant/menu-items/<id>/
   Método: GET, PUT, PATCH, DELETE
   Auth: Token requerido
   Ejemplo: /restaurant/menu-items/1/

## Endpoints de Reservas
1. Gestión de Mesas
   Ruta: /restaurant/booking/tables/
   Método: GET, POST, PUT, DELETE
   Auth: Token requerido

## Autenticación
1. Obtener Token
   Ruta: /restaurant/api-token-auth/
   Método: POST
   Datos requeridos:
   {
       "username": "tu_usuario",
       "password": "tu_contraseña"
   }

2. Gestión de Usuarios (Djoser)
   Ruta: /auth/users/
   Método: POST (crear usuario)
   
3. Login/Logout (Djoser)
   Ruta: /auth/token/login/
   Ruta: /auth/token/logout/
   Método: POST

Notas:
- Para endpoints protegidos, incluir el token en el header:
  Authorization: Token <your_token>
- Todos los endpoints que requieren autenticación deben incluir este header# LittleLemon