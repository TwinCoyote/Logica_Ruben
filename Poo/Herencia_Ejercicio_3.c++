#include <iostream>
#include <stdlib.h>

using namespace std;

/// ** Clases  ///

class Persona
{
private:
    string nombre;
    int edad;

public:
    Persona(string, int);
    void leer();
    void correr();
    void mostrarPersona();
};

class Estudiante : public Persona
{
private:
    string codigoAlumno;
    float notaFinal;

public:
    Estudiante(string, int, string, float);
    void mostrarAlumno();
};

class Universitario : public Estudiante
{
private:
    string carrera;
    int anios;

public:
    Universitario(string, int, string, float, string, int);
    void mostrarResumen();
};

class Empleado : public Persona
{
private:
    string rol;
    int salario;

public:
    Empleado(string, int, string, int);
    void doxear();
};
/// ** Constructores ///

Persona ::Persona(string _nombre, int _edad)
{
    nombre = _nombre;
    edad = _edad;
}

Estudiante::Estudiante(string _nombre, int _edad, string _codigoAlumno, float _notaFinal) : Persona(_nombre, _edad)
{
    codigoAlumno = _codigoAlumno;
    notaFinal = _notaFinal;
}

Universitario::Universitario(string _nombre, int _edad, string _codigoAlumno, float _notaFinal, string _carrera, int _anios) : Estudiante(_nombre, _edad, _codigoAlumno, _notaFinal)
{
    carrera = _carrera;
    anios = _anios;
}

Empleado::Empleado(string _nombre, int _edad, string _rol, int _salario) : Persona(_nombre, _edad)
{
    rol = _rol;
    salario = _salario;
}

/// ** Funciones  ///

void Persona::mostrarPersona()
{
    cout << "Nombre: " << nombre << endl;
    cout << "Edad: " << edad << endl;
}

void Persona::leer()
{
    cout << "Soy " << nombre << "y estoy leyendo un libro" << endl;
}

void Persona::correr()
{
    cout << "Soy " << nombre << "y estoy Corriendo" << endl;
}

void Estudiante::mostrarAlumno()
{
    mostrarPersona();
    cout << "Codigo de Alumno: " << codigoAlumno << endl;
    cout << "Calificacion: " << notaFinal << endl;
}

void Universitario::mostrarResumen()
{
    mostrarAlumno();
    cout << "Carrera del alumno: " << carrera << endl;
    cout << "LLeva " << anios << " Años en la carrera" << endl;
}

void Empleado::doxear()
{
    mostrarPersona();
    cout << "Tiene este Rol: " << rol << endl;
    cout << "Con un salario de: " << salario << endl;
}

///** Main *///

int main()
{
    Universitario rub("Ruben r.", 24, "21050565", 97, "Electronica", 4);

    rub.mostrarResumen();

    /// todo declarar al empleado

    Empleado no("Lino Ruben R.", 25, "Gerente", 55000);
    no.doxear();

    system("pause");
    return 0;
}