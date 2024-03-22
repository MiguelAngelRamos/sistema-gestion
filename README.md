Sistema de gestión para una tienda de videojuegos. 
# Ejercicio
Este sistema debe permitir registrar nuevas desarrolladoras de videojuegos, añadir videojuegos al catálogo de la tienda, gestionar empleados y clientes, y realizar operaciones de venta. Cada videojuego está asociado con una desarrolladora específica y puede tener varios géneros asignados. Los empleados pueden vender videojuegos a los clientes, acción que afecta el stock del producto y el saldo del cliente, además de generar una comisión para el empleado.

Para este propósito, necesitas diseñar un sistema orientado a objetos que incluya clases para las desarrolladoras de videojuegos, los videojuegos, los empleados y los clientes. Además, debes implementar un menú interactivo que permita al usuario realizar todas las operaciones necesarias, como registrar desarrolladoras y videojuegos, actualizar precios, realizar ventas, recargar saldo a los clientes, entre otros.

El sistema debe tener en cuenta lo siguiente:

- **Desarrolladora**: Cada desarrolladora debe tener un RUT, nombre, dirección, país y un indicador de si es una persona jurídica.
- **Videojuego**: Cada videojuego debe contener un código único, título, precio, stock disponible, la desarrolladora que lo provee y, opcionalmente, su género.
- **Empleado**: Cada empleado debe tener un ID, nombre y, opcionalmente, una comisión acumulada por ventas realizadas.
- **Cliente**: Cada cliente debe tener un ID, nombre, saldo disponible para compras y, opcionalmente, su género de videojuegos preferido.

Tu tarea es implementar este sistema en Python, asegurándote de que sea posible interactuar con él a través de un menú de consola. Este menú debe ofrecer opciones para registrar desarrolladoras, videojuegos, empleados y clientes, así como para actualizar el precio de los videojuegos, realizar ventas y recargar el saldo de los clientes. Debes proporcionar una solución que incluya tanto la definición de las clases necesarias como la implementación del menú interactivo.
