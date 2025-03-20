from conexion import get_connection

def crear_tablas():
    """Crea las tablas en la base de datos 'tienda_online' si no existe."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("USE tienda_online")  # Selecciona la base de datos

            # Verificar si las tablas ya existen
            cursor.execute("SHOW TABLES LIKE 'proveedores'")
            tabla_existe = cursor.fetchone()
            

            if not tabla_existe:
                # Sentencia SQL para crear la tabla
                crear_tabla_sql = """
                    CREATE TABLE proveedores (
                        id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        contacto VARCHAR(100),
                        telefono VARCHAR(15),
                        direccion TEXT,
                        activo TINYINT(1) NOT NULL DEFAULT 1 -- Eliminación lógica
                    );

                    CREATE TABLE productos (
                        id_producto INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        descripcion TEXT,
                        precio DECIMAL(10,2) NOT NULL,
                        stock INT NOT NULL,
                        stock_minimo INT NOT NULL DEFAULT 5, -- Stock mínimo
                        disponible TINYINT(1) NOT NULL DEFAULT 1, -- 1 = Disponible, 0 = Agotado
                        id_proveedor INT NOT NULL, -- Relación con proveedor
                        activo TINYINT(1) NOT NULL DEFAULT 1, -- Eliminación lógica
                        FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor) ON DELETE RESTRICT
                    );

                    CREATE TABLE clientes (
                        id_cliente INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        correo VARCHAR(100) UNIQUE NOT NULL,
                        telefono VARCHAR(15),
                        direccion TEXT,
                        activo TINYINT(1) NOT NULL DEFAULT 1 -- Eliminación lógica
                    );


                    CREATE TABLE pedidos (
                        id_pedido INT AUTO_INCREMENT PRIMARY KEY,
                        id_cliente INT NOT NULL,
                        fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        total DECIMAL(10,2) NOT NULL,
                        estado ENUM('pendiente', 'enviado', 'entregado', 'cancelado') DEFAULT 'pendiente',
                        activo TINYINT(1) NOT NULL DEFAULT 1, -- Eliminación lógica
                        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
                    );

                    CREATE TABLE pagos (
                        id_pago INT AUTO_INCREMENT PRIMARY KEY,
                        id_pedido INT NOT NULL,
                        metodo_pago ENUM('tarjeta', 'transferencia', 'efectivo') NOT NULL,
                        monto DECIMAL(10,2) NOT NULL,
                        fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        activo TINYINT(1) NOT NULL DEFAULT 1, -- Eliminación lógica
                        FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido) ON DELETE CASCADE
                    );

                    CREATE TABLE detalle_pedido (
                        id_detalle INT AUTO_INCREMENT PRIMARY KEY,
                        id_pedido INT NOT NULL,
                        id_producto INT NOT NULL,
                        cantidad INT NOT NULL,
                        precio_unitario DECIMAL(10,2) NOT NULL,
                        subtotal DECIMAL(10,2) NOT NULL,
                        activo TINYINT(1) NOT NULL DEFAULT 1, -- Eliminación lógica
                        FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
                        FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
                    );
                """
                cursor.execute(crear_tabla_sql)
                print("✅ Tablas creadas exitosamente.")
            else:
                print("⚠️ Las tablas ya existe.")

        except Exception as e:
            print(f"❌ Error al crear la tabla: {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    crear_tablas()
