#include <iostream>
#include <stdlib.h>
using namespace std;

class Persona
{
private:
    int edad;
    string nombre;

public:
    Persona(int, string);
    void leer();
    void correr();
};

Persona::Persona(int _edad, string _nombre)
{
    edad = _edad;
    nombre = _nombre;
}

void Persona::leer()
{
    cout << "Soy " << nombre << " y estoy leyendo un libro" << endl;
}

void Persona::correr()
{
    cout << "Soy " << nombre << " y estoy corriendo una maraton" << endl;
}

int main()
{
    Persona p1 = Persona(20, "Ruben");
    p1.leer();
    system("pause");
    return 0;
}