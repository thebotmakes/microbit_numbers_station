## microbit_numbers_station
# Numbers station simulator using the BBC Microbit and MicroPython

Simple bit of code to convert your Microbit to a numbers station and live life like you're a cold war spy!  Just attach a speaker in the normal way and you're good to go!

The basic flow of this is:

  3 functions:
  * say_codes - this generates a random 5 number sequence, then says it twice (some of the numbers stations do this so the definitely not spies that are listening to the messages have two goes to get the code).  The last number is pitched slightly differently cause this was a feature of most of the stations.
  * say_group - this is a fixed code, so the definitely not spies know which one time pad to use to decode the message (13700 as in the LM13700 OTA chip)
  * play_music - because we're in MicroPython I used the Monty Python theme tune, but I might do something a bit more custom later on.  I quite liked this though cause it reminded me of the Lincolnshire Poacher, used on one of the most famous stations
  
Then there's a main loop, which just runs through the sequence:
  * play the theme (so the definitely not spies know they've tuned in correctly)
  * say the group twice (so the definitely not spies know the one time pad to use)
  * say the codes (five groups of five random numbers, each repeated twice)
