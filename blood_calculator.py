print("Python thinks this is called {}".format(__name__))

def interface():
    print("My Program")
    print("Options:")
    print("1 - Analyse HDL")
    print("2 - Analyse LDL")
    print("3 - Analyse Total Cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == "1" :
            HDL_driver()
        elif choice == "2" :
            LDL_driver()
        elif choice == "3" :
            Cholesterol_driver()


def input_HDL():
    HDL_input = input("Enter the HDL value: ")
    return int(HDL_input)

def input_LDL():
    LDL_input = input("Enter the LDL value: ")
    return int(LDL_input)

def input_chol():
    chol_input = input("Enter the Cholesterol value: ")
    return int(chol_input)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def check_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 159:
        return "Borderline High"
    elif 160 <= LDL_value < 189:
        return "High"
    else:
        return "Very High"

def check_chol(chol_value):
    if chol_value < 200:
        return "Normal"
    elif 200 <= chol_value < 239:
        return "Borderline High"
    else:
        return "High"

def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)

def LDL_driver():
    ldl_value = input_LDL()
    answer2 = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer2)

def Cholesterol_driver():
    chol_value = input_chol()
    answer3 = check_chol(chol_value)
    output_chol_result(chol_value, answer3)

def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value of {} is {}".format(hdl_value, charac))

def output_LDL_result(ldl_value, charac2):
    print("The results for an LDL value of {} is {}".format(ldl_value, charac2))

def output_chol_result(chol_value, charac3):
    print("The results for an Cholesterol value of {} is {}".format(chol_value, charac3))

if __name__ == "__main__":
	interface()
