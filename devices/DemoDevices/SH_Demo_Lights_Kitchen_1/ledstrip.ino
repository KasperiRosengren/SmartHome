/*
 * Red      = (255, 0, 0)
 * Green    = (0, 255, 0)
 * Blue     = (0, 0, 255)
 * Yellow   = (255, 255, 0)
 * Cyan     = (0, 255, 255)
 * Magenta  = (255, 0, 255)
 * White    = (255, 255, 255)
 */

void ledstripmain()
{
  if(loopflag)
  {
    loopflag = false;

/*######Turn all leds to same color at the same time######*/   
    if(ledshow == "allsame"){
      for(int i=0; i<NUM_LEDS; i++){
        leds[i] = CRGB(color_0_r, color_0_g, color_0_b);      //RGB valus for leds
      }FastLED.show();}
    

/*######Turn off all leds at the same time######*/
    else if(ledshow == "allOff")
    {
      for(int i=0; i<NUM_LEDS; i++)
      {
        leds[i] = CRGB(0, 0, 0);    //Off
      }FastLED.show();
    }

/*######Back and forth with the same color######*/
    else if(ledshow == "backandforth"){
      while(ledshow == "backandforth"){
        for(int i=0; i<NUM_LEDS+2; i++){
          leds[i] = CRGB(color_0_r, color_0_g, color_0_b);      //Green
          leds[i+1] = CRGB(color_0_r, color_0_g, color_0_b);    //Green
          leds[i-1] = CRGB(0, 0, 0);      //Off
          leds[i-2] = CRGB(0, 0, 0);      //Off
          FastLED.show();
        }
        for(int i=NUM_LEDS-1; i>-2; i--){
          leds[i] = CRGB(color_0_r, color_0_g, color_0_b);      //Green
          leds[i-1] = CRGB(color_0_r, color_0_g, color_0_b);    //Green
          leds[i+1] = CRGB(0, 0, 0);      //Off
          leds[i+2] = CRGB(0, 0, 0);      //Off
          FastLED.show();}}}

/*######Second color chases First color######*/
    else if(ledshow == "chase"){ //
      while(ledshow == "chase"){
        for(int i=0; i<NUM_LEDS+4; i++){
          leds[i+3] = CRGB(color_0_r, color_0_g, color_0_b);
          leds[i+2] = CRGB(color_0_r, color_0_g, color_0_b);
          leds[i+1] = CRGB(0, 0, 0);      //Off
          leds[i] = CRGB(0, 0, 0);      //Off
          leds[i-1] = CRGB(color_1_r, color_1_g, color_1_b);
          leds[i-2] = CRGB(color_1_r, color_1_g, color_1_b);
          leds[i-3] = CRGB(0, 0, 0);      //Off
          leds[i-4] = CRGB(0, 0, 0);      //Off
          FastLED.show();}}}
  }
}
