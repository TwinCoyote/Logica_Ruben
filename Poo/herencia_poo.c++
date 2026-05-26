#include <iostream>
#include <stdlib.h>

using namespace std;

///       Clases       ///
class Persona
{
private: // Atributos
    string nombre;
    int edad;

public:                   // Metodos
    Persona(string, int); // Constructor
    void mostrarPersona();
};

class Alumno : public Persona
{
private:
    string codigoAlumno;
    float notaFinal;

public:
    Alumno(string, int, string, float);
    void mostrarAlumno();
};

///       Constructores       ///
Persona::Persona(string _nombre, int _edad)
{
    nombre = _nombre;
    edad = _edad;
}

Alumno::Alumno(string _nombre, int _edad, string _codigoAlumno, float _notaFinal) : Persona(_nombre, _edad)
{

    codigoAlumno = _codigoAlumno;
    notaFinal = _notaFinal;
}




///        Funciones         ///
void Persona::mostrarPersona()
{
    cout << "Nombre: " << nombre << endl;
    cout << "Edad: " << edad << endl;
}

void Alumno::mostrarAlumno()
{
    mostrarPersona();
    cout << "Codigo Alumno: " << codigoAlumno << endl;
    cout << "Nota Final: " << notaFinal << endl;
}

int main()
{
    Alumno alumno1("Ruben R.", 20, "21050565", 87.3);

    alumno1.mostrarAlumno();

    system("pause");
    return 0;
}