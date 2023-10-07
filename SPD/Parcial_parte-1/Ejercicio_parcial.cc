// CÁTODO COMÚN
# define A 3
# define B 4
# define C A1
# define D A2
# define E A0
# define F 2
# define G 5
# define L_DISP A4 // display izquierdo
# define R_DISP A5 // display derecho
# define INC_BTN 10 // boton de incremento
# define DEC_BTN 9 // boton de decremento
# define RES_BTN 8 // boton de reinicio

int counter;
// arreglo con estados contra los cuales comparar
int btnLastStates[3] = {LOW, LOW, LOW};

void setup()
{
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(L_DISP, OUTPUT);
  pinMode(R_DISP, OUTPUT);
  pinMode(INC_BTN, INPUT_PULLUP);
  pinMode(DEC_BTN, INPUT_PULLUP);
  pinMode(RES_BTN, INPUT_PULLUP);
  counter = 0;
}

void loop()
{
  // leyendo constantemente el estado actual de los pulsadores 
  int incCurrentState = digitalRead(INC_BTN);
  int decCurrentState = digitalRead(DEC_BTN);
  int resCurrentState = digitalRead(RES_BTN);
  // arreglo con los estados actuales
  int btnStates[3] = {incCurrentState, decCurrentState, resCurrentState};
  // al haber 3 pulsadores, el for tiene 3 iteraciones
  for (int i = 0; i < 3; i++)
  {
    // se compara un cambio en el estado actual del pulsador
    if(btnStates[i] != btnLastStates[i])
    {
      if (btnStates[i] == LOW)
      {
        // solo se accede en caso de presionar el pulsador
        handleCounter(i);
      }
    }
  }
  // se actualiza el estado anterior con el actual (presionado o no)
  btnLastStates[0] = incCurrentState;
  btnLastStates[1] = decCurrentState;
  btnLastStates[2] = resCurrentState;
  
  handleDigits(counter);
}
// prendido y apagado de pines
void lightOn(int pin)
{
  digitalWrite(pin, HIGH);
}
void lightOff(int pin)
{
  digitalWrite(pin, LOW);
}
// con el proposito de no ser repetitivo, todos los números están hechos a partir del 0
void numberZeroOn()
{
  lightOn(A);
  lightOn(B);
  lightOn(C);
  lightOn(D);
  lightOn(E);
  lightOn(F);
  lightOff(G);
}
void numberOneOn()
{
  numberZeroOn();
  lightOff(A);
  lightOff(D);
  lightOff(E);
  lightOff(F);
}
void numberTwoOn()
{
  numberZeroOn();
  lightOff(C);
  lightOff(F);
  lightOn(G);
}
void numberThreeOn()
{
  numberZeroOn();
  lightOff(E);
  lightOff(F);
  lightOn(G);
}
void numberFourOn()
{
  numberOneOn();
  lightOn(F);
  lightOn(G);
}
void numberFiveOn()
{
  numberZeroOn();
  lightOff(B);
  lightOff(E);
  lightOn(G);
}
void numberSixOn()
{
  numberZeroOn();
  lightOff(B);
  lightOn(G);
}
void numberSevenOn()
{
  numberOneOn();
  lightOn(A);
}
void numberEightOn()
{
  numberZeroOn();
  lightOn(G);
}
void numberNineOn()
{
  numberFourOn();
  lightOn(A);
}
// muestra el numero del parametro en el display
void showNumber(int number)
{
  switch (number)
  {
    case 0:
    {
      numberZeroOn();
      break;
    }
    case 1:
    {
      numberOneOn();
      break;
    }
    case 2:
    {
      numberTwoOn();
      break;
    }
    case 3:
    {
      numberThreeOn();
      break;
    }
    case 4:
    {
      numberFourOn();
      break;
    }
    case 5:
    {
      numberFiveOn();
      break;
    }
    case 6:
    {
      numberSixOn();
      break;
    }
    case 7:
    {
      numberSevenOn();
      break;
    }
    case 8:
    {
      numberEightOn();
      break;
    }
    case 9:
    {
      numberNineOn();
      break;
    }
  }
}
// prendido y apagado constante de los displays (multiplexación)
void handleDigits(int number)
{
  int unit;
  // APAGO AMBOS (los dos en HIGH)
  lightOn(L_DISP);
  lightOn(R_DISP);
  // PRENDO LA DECENA (unidad en LOW, decena en HIGH)
  showNumber(number / 10); // enciendo el número
  lightOff(R_DISP); // unidad
  lightOn(L_DISP); // decena
  delay(10); // 10 ms para estabilidad visual
  // APAGO AMBOS (los dos en HIGH)
  lightOn(L_DISP);
  lightOn(R_DISP);
  // condiciono la unidad
  if (number >= 10 && number <= 99)
  {
    unit = number % 10;
  }
  else {
    unit = number;
  }
  // PRENDO LA UNIDAD (decena en LOW, unidad en HIGH)
  showNumber(unit);
  lightOff(L_DISP); // decena
  lightOn(R_DISP); // unidad
  delay(10); // 10 ms para estabilidad visual
}
// determina que hacer con el contador al detectar los cambios de estados de los pulsadores
void handleCounter(int btnIndex)
{
  switch (btnIndex)
  {
    case 0: // pulsador de incremento
      if (counter <= 99)
      {
        counter++;
      }
      break;
    case 1: // pulsador de decremento
      if (counter > 0)
      {
        counter--;
      }
      break;
    case 2: // pulsador de reseteo
      counter = 0;
      break;
  }
}