int LED0 = 43;
int LED1 = 44;
int LED2 = 45;
int LED3 = 46;

int SW0 = 38;
int SW1 = 39;
int SW2 = 40;
int SW3 = 41;

bool ledState0 = false;
bool ledState1 = false;
bool ledState2 = false;
bool ledState3 = false;

void setup() {

  pinMode(LED0, OUTPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);

  pinMode(SW0, INPUT);
  pinMode(SW1, INPUT);
  pinMode(SW2, INPUT);
  pinMode(SW3, INPUT);

}

void loop() {

  // SW0
  if(digitalRead(SW0) == HIGH) {

    ledState0 = !ledState0;

    digitalWrite(LED0, ledState0);

    while(digitalRead(SW0) == HIGH);

    delay(100);
  }

  // SW1
  if(digitalRead(SW1) == HIGH) {

    ledState1 = !ledState1;

    digitalWrite(LED1, ledState1);

    while(digitalRead(SW1) == HIGH);

    delay(100);
  }

  // SW2
  if(digitalRead(SW2) == HIGH) {

    ledState2 = !ledState2;

    digitalWrite(LED2, ledState2);

    while(digitalRead(SW2) == HIGH);

    delay(100);
  }

  // SW3
  if(digitalRead(SW3) == HIGH) {

    ledState3 = !ledState3;

    digitalWrite(LED3, ledState3);

    while(digitalRead(SW3) == HIGH);

    delay(100);
  }

}
