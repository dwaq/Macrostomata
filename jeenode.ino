/// @dir test2
/// Very simple demo sketch to transmit LDR light readings once a second
// 2013-02-16 <jc@wippler.nl> http://opensource.org/licenses/mit-license.php

#include <JeeLib.h>

#define button1 4
#define button2 5
#define button3 6

int button1Read, button2Read, button3Read;
byte buttonsState = 0;

void setup () {
  // this is node 1 in net group 100 on the 868 MHz band
  rf12_initialize(1, RF12_915MHZ, 100);

    pinMode(button1, INPUT);
    pinMode(button2, INPUT);
    pinMode(button3, INPUT);
}
  
void loop () {
  // measure analog value and convert the 0..1023 result to 255..0
  button1Read = digitalRead(button1);
  button2Read = digitalRead(button2);
  button3Read = digitalRead(button3);

  // These if statements set the bit of buttonsState to the cooresponding
  // state of the button.
  // bit 1 = button1State, bit2 = button2State, bit3= button3State
  if (button1Read == 1){
    buttonsState &= ~(1 << 0);
  }else{
    buttonsState |= (1 << 0); 
  }
  
  if (button2Read == 1){
    buttonsState &= ~(1 << 1);
  }else{
    buttonsState |= (1 << 1); 
  }
  
  if (button3Read == 1){
     buttonsState &= ~(1 << 2);
  }else{
    buttonsState |= (1 << 2); 
  }

  // actual packet send: broadcast to all, current counter, 1 byte long
  rf12_sendNow(0, &buttonsState, 1);

  // let one second pass before sending out another packet
  delay(1000);
}
