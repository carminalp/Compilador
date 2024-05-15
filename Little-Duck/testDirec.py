from FuncDirectory import FuncDirectory

def run_tests():
    try:
        # Crear una instancia del directorio de funciones
        dir_func = FuncDirectory()

        # Añadir función global
        print("Añadiendo función 'global'")
        dir_func.add_function('global')
        dir_func.set_current_global('global')
        dir_func.create_variable_table()

        # Añadir variables globales
        print("Añadiendo variable 'a' al ámbito global")
        dir_func.add_variable_to_current_func('a', 'int')
        print("Añadiendo variable 'b' al ámbito global")
        dir_func.add_variable_to_current_func('b', 'float')

        # Añadir nueva función 'func1'
        print("Añadiendo función 'func1'")
        dir_func.add_function('func1')
        dir_func.create_variable_table()

        # Añadir variables a 'func1'
        try:
            print("Añadiendo variable 'a' a 'func1' (debería fallar)")
            dir_func.add_variable_to_current_func('a', 'int')
        except ValueError as e:
            print(e)  # Debería mostrar un error diciendo que 'a' ya está definida en el ámbito global

        print("Añadiendo variable 'c' a 'func1'")
        dir_func.add_variable_to_current_func('c', 'bool')

        # Verificar variables en 'func1'
        print("Variables en 'func1':", dir_func.get_current_function_vars())

        # Añadir nueva función 'func2'
        print("Añadiendo función 'func2'")
        dir_func.add_function('func2')
        dir_func.create_variable_table()

        # Añadir variables a 'func2'
        print("Añadiendo variable 'd' a 'func2'")
        dir_func.add_variable_to_current_func('d', 'int')

        # Verificar variables en 'func2'
        print("Variables en 'func2':", dir_func.get_current_function_vars())

    except ValueError as e:
        print("Error:", e)

# Ejecutar las pruebas
run_tests()
