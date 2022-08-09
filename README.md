# bits_to_frequency
Python script to create a lookup table for ADC bits to audio frequencies\

 
 
 THE audioDIWHY AD9833 library outputs a frequency based on
a hex or numberic fequency value entered as a parameter

We will put an ADC in front of AD9833 with outputs of 0-1024, 0-4096 etc.

so, a lookup table of bits to frequency is needed,

there are plenty of examples already for 128 bit (MIDI) bit to frequency
like this one: https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
but none I could find for higher resolution ADCs in this particular application.

Hence this python script.

enter then starting note, ending note, and how many cents should appear between entries
out comes a python list and a file in CSV format, both forward and reverse()'d.


###############################

