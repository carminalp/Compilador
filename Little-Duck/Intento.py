# Importar las funciones necesarias
from Compi.parser import compile_code
from VM.virtualMachine import execute_quadruples
from VM.Memory import Memory

# Definir el código fuente como un string
source_code = """
program test;

    var i, j, n, square, input : int;

    main {
        n = 10;
        print("Number of squares to calculate: ");
	    print(n);
        if (n < 0) {
            print("It's not a positive integer greater than zero.");
        } else {
            i = 0;
            do {
                if (i / 2 > 0) {
                    square = i * i;
                    print("Square of ", i, " is: ", square);
                } else {
                    print(i, " is odd, calculating squares for next ", n, " numbers.");
                    j = i;
                    do {
                        square = j * j;
                        if (square / 2 > 0) { 
                            print("Square of ", j, " is: ", square, " and it is even.");
                        } else {
                            print("Square of ", j, " is: ", square, " and it is odd.");
                        };
                        j = j + 1;
                    } while (j < i + n);
                };
                i = i + 1;
            } while (i < n);
        };
    }
end

"""

# Función para compilar y ejecutar el código fuente
def compile_and_run(source_code):
    try:
        # Enviar el código fuente a la función de compilación
        cte_directory, quadruples = compile_code(source_code)
            
        # Inicializar la memoria con el directorio de constantes
        memory = Memory()
        memory.initialize_constants(cte_directory)
        
        # Ejecutar los cuádruplos y obtener el array de salida
        output = execute_quadruples(quadruples, memory)
        
        # Imprimir la salida
        for line in output:
            print(line)
            
    except Exception as e:
        print(f"Error: {e}")

# Llamar a la función con el código fuente definido
compile_and_run(source_code)
