#include "pong.h"
#include "input.h"

namespace pong
{

  int pong_direccion = 1;

  const int botonArriba = 2;
  const int botonAbajo = 19;
  const int botonDerecha = 4;
  const int botonIzquierda = 16;
  const int botonSelect = 5;

  const int pong_len_block = 4;
  const int width = 12;
  const int limite_inferior = ALTO_PANTALLA - width;
  const int limite_inferior_ball = ALTO_PANTALLA - len_block;
  const int limite_superior = 0;
  const int ball_size = 4;

  int x_AI = ANCHO_PANTALLA - len_block;
  int x = 0;
  int y = 0;
  int ball_x = 0;
  int ball_y = 0;

  void pong_direcciones()
  {
    if (pong_direccion == 0)
      y -= len_block;
    if (pong_direccion == 1)
      y += len_block;
  }

  void pong_buttons_read()
  {
    int dir = input.realDirection();
    if (dir == 1)
    {
      pong_direccion = 0;
    }
    else if (dir == 2)
    {
      pong_direccion = 1;
    }
  }

  void screen_limits()
  {
    if (y <= limite_superior)
      y = limite_superior;
    else if (y > ALTO_PANTALLA - width)
      y = limite_inferior;
  }

  void print_player()
  {
    display.fillRect(x, y, len_block, width, SSD1306_WHITE);
  }

  void print_AI()
  {
    display.fillRect(x_AI, y, len_block, width, SSD1306_WHITE);
  }

  void ball_limits()
  {
    if (ball_y <= 0 || ball_y >= ALTO_PANTALLA - ball_size)
    {
      ball_y *= -1;
    }
  }

  void caida()
  {
    ball_y++;
  }

  void game_pong()
  {
    display.clearDisplay();
    pong_buttons_read();
    pong_direcciones();
    screen_limits();
    print_player();
    print_AI();
    display.display();

    delay(120);
  }
}