# database.py

print("This is the database.py module")
print("Python thinks this is called {}".format(__name__))

# import runs the file, so it basically runs the blood_calculator.py
import blood_calculator.py
# or
# from blood_calculator import check_HDL
# or
# import blood_calculator as bc
# answer = bc.check_HDL(55)
# or
# from blood_calculator import *  (* means import ALL) (although bad practice)

answer = blood_calculator.HDL_check(55)
print("The HDL of 55 is {}",format(answer))



