 #include dictnote.py
from typing import List, Any

import dictnote
import csv

##############################
## WHAT IS THIS SCRIPT?  WHY DOES IT EXIST?
##
## THE audioDIWHY AD9833 library outputs a frequency based on
## a hex or numberic fequency value entered as a parameter
##
## We will put an ADC in front of AD9833 with outputs of 0-1024, 0-4096 etc.
##
## so, a lookup table of bits to frequency is needed,
##
## there are plenty of examples already for 7 bit (MIDI) to frequency
## like this one: https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
## but none I could find for higher resolution ADCs in this particular application.
##
## so I wrote this python script.
##
## enter then starting note, ending note, and how many cents should appear between entries
## out comes a python list and a file in CSV format.
###############################




if __name__ == '__main__':

     counter = 1
     end_this_loop = 0


     def get_cent(x):

        cents = 2 ** (x / 1200)
        return cents


     freqarray = []
     list_of_numbers = []

     ########## change these values##############################
     cents_between_entries = 3  #how many cents do you want between each entry?
     starting_value = 'C0'  #what semitone do you want to start at?
     stop_value = 'C10'      #what semitone do you want to stop at?
     output_filename = "list.csv"
     output_filename_reversed = "list.rev.csv"
     ############################################################


     cent_multiplier = get_cent(cents_between_entries)

     print("\nFrequency proportion between F2 and F1 is " + str(cent_multiplier))
     number_steps = int(100/cents_between_entries)
     print("number of values between each semitone is " + str(number_steps) + "\n")
     value = dictnote.init_freq[starting_value]
     endvalue = dictnote.init_freq[stop_value]

     print("starting freq is: "+ value + " or " + starting_value)  #value of starting semitone frequency
     print("stopping freq is: " + endvalue + " or " + stop_value + "\n")  # value of starting semitone frequency
     for x in dictnote.init_freq.values():
        if (float(x) >= float(value)):
            list_of_numbers.append(x)



     for qq in list_of_numbers:
         if (end_this_loop == 2):
             freqarray.pop()
             break
         freqarray.append(float(qq))
         ab = len(freqarray)
         counter = 0
         for i in range(ab,ab+number_steps):
             counter = counter + 1
             if counter == (number_steps + 1):
                 counter = 0
                 break
             else:

                freqarray.append(float(freqarray[i-1])*cent_multiplier)
                guess1 = freqarray[i-1]
                guess2 = float(endvalue)
                if (guess2 == guess1):
                     end_this_loop = 2
                     break
     print("here is your list: \n")


     print(str(freqarray) + "\n")

     lengg = str(len(freqarray))

     print("Your list has " + lengg + " entries\n \n")



     #write to file
     with open(output_filename, 'w') as f:

         # using csv.writer method from CSV package
         write = csv.writer(f)

         write.writerow(freqarray)
         print("Created CSV: " + output_filename + "\n")

     freqarray.reverse()
     print("here it is again, in reverse: \n")
     print(str(freqarray) + "\n")

with open(output_filename_reversed, 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(freqarray)
    print("Created CSV: " + output_filename_reversed + "\n")
