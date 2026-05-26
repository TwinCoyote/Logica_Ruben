#include <Arduino.h>
#include "input.h"
#include "states_displays.h"
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define ANCHO_PANTALLA 128
#define ALTO_PANTALLA 64
#define DIRECCION_OLED 0x3C

int menu_count = 0;
unsigned int len_state = 0;

Adafruit_SSD1306 display(ANCHO_PANTALLA, ALTO_PANTALLA, &Wire, -1);
int direccion = 0;
using namespace std;

unsigned long interval = 200;

enum state
{
    INIT,
    MAIN_MENU,
    SETTINGS_MENU,
    GAME_PONG,
    GAME_SNAKE,
    LAST_STATE // Este estado es solo para calcular el len
};

state current_state = INIT;
Input input(2, 19, 4, 16);

bool canMove(unsigned long interval)
{
    static unsigned long previousTime = 0;

    unsigned long currentTime = millis();

    if (currentTime - previousTime >= interval)
    {
        previousTime = currentTime;
        return true;
    }

    return false;
}

void setup()
{
    if (!display.begin(SSD1306_SWITCHCAPVCC, DIRECCION_OLED))
    {
        Serial.println(F("Error en la asignación de SSD1306"));
        for (;;)
            ;
    }
    Serial.begin(115200);
    input.begin();
    display.clearDisplay();
    display.display();
}

void loop()
{

    // // if(menu_count >= 5) menu_count = (int)MAIN_MENU;
    // if(menu_count <= 1 ) menu_count =(int)LAST_STATE -1;
    // if(menu_count >= 5) menu_count =1;
    // menu_count = (menu_count - 1 + (LAST_STATE - 1)) % (LAST_STATE - 1) + 1;

    int dir = input.realDirection();
    if (dir == 4)
    {
        menu_count--;
        canMove(200);
    }
    if (dir == 3)
    {
        menu_count++;
        canMove(200);
    }
    if (menu_count > LAST_STATE - 1)
    {
        menu_count = 1;
    }

    if (menu_count < 1)
    {
        menu_count = LAST_STATE - 1;
    }

    Serial.println(menu_count);
    current_state = (state)menu_count;
    switch (current_state)
    {
    case INIT:
        display.clearDisplay();
        init_screen(display);

        display.display();
        canMove(600);
        if (end_init_screen())
        {

            current_state = MAIN_MENU;
        }
        break;

    case MAIN_MENU:
        display.clearDisplay();
        main_menu_display(display);
        display.display();
        break;

    case SETTINGS_MENU:
        display.clearDisplay();
        settings_display(display);
        display.display();
        break;

    case GAME_PONG:
        display.clearDisplay();
        pong_display(display);
        display.display();
        break;

    case GAME_SNAKE:
        display.clearDisplay();
        snake_display(display);
        display.display();
        break;
    }

    // if(current_state >= LAST_STATE){
    //   current_state = MAIN_MENU;
    // }
    // if(current_state <= MAIN_MENU){
    //   current_state = LAST_STATE;
    // }
    // if (menu_count >= LAST_STATE) {
    //   menu_count = 1;
    // }
    // if (menu_count <= 0) {
    //   menu_count = LAST_STATE - 1;
    // }
}