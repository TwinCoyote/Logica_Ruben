#include <iostream> // La librería para entrada/salida de datos
#include <string>

string "Hola";



void display_counter() {
    // El equivalente a Serial.println es std::cout
    std::cout << "-----------------------" << std::endl;
    std::cout << "       SNAKE           " << std::endl;
    std::cout << "-----------------------" << std::endl;
    std::cout << "Dibujando el fondo..." << std::endl;
    
    // En consola no podemos dibujar bitmaps, así que usamos texto
    std::cout << "Estado: Juego iniciado" << std::endl;
}

int main() {
    // Llamamos a la función
    display_counter();
    
    return 0;
}