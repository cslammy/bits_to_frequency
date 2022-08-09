# bits_to_frequency
Python script to create a lookup table for ADC bits to audio frequencies\

 
 
 THE audioDIWHY AD9833 library outputs a frequency based on
a hex or numberic fequency value entered as a parameter

We will put an ADC in front of AD9833, but the ADC has outputs of 0-1024 (10 bit ADC), 0-4096 (12 bit ADC) etc.

so, a lookup table of bits to frequency is needed, for at least this specific application, maybe others.

there are plenty of examples already for 7 bit (MIDI) in other words, 128 semitones to frequency tables
like this one: https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
but none I could find for higher resolution ADCs in this particular application.

Hence this python script.

enter then starting note, ending note, and how many cents should appear between entries
out comes a python list and a file in CSV format, both forward and reverse()'d.


###############################

