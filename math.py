import math
import time
import pyttsx3


def voice_command_findingFactors():
    converter1 = pyttsx3.init()
    converter1.setProperty("rate", 150)
    converter1.setProperty("volume", 0.7)
    converter1.say("Enter the number you want to find the factor of")
    converter1.runAndWait()


def voice_command_quadraticFormula():
    converter2 = pyttsx3.init()
    converter2.setProperty("rate", 150)
    converter2.setProperty("volume", 0.7)
    converter2.say("Quadratic formula")
    converter2.runAndWait()


def voice_command_infodesk():
    converter3 = pyttsx3.init()
    converter3.setProperty("rate", 150)
    converter3.setProperty("volume", 0.7)
    converter3.say(
        "Which of our products would you like to use: [1.finding factors 2. solving quadratic equations](enter 1 or 2)")
    converter3.runAndWait()


def finding_factors():
    voice_command_findingFactors()
    # finding factors
    nff = int(input("Enter the number you want to find factor off:"))

    count = 1
    while count <= nff/2:
        print(count)
        print(nff/count)
        count = count + 1


def quadratic_formula():
    voice_command_quadraticFormula()
    a = int(input("Input a:"))
    b = int(input("Input b:"))
    c = int(input("Input c"))

    x1 = (-b + math.sqrt(b**2 - 4*a*c)/2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)/2*a)

    print("X1 is " + x1)
    print("X2 is " + x2)

    # infodesk
    voice_command_infodesk()


def shvp_for_two():
    num1 = int(input("Enter the first number to use in SH.V.P equation"))
    num2 = int(input("Enter the second number to use in SH.V.P equation"))

    # find which number is bigger
    if num1 > num2:
        count = 0
        while count <= num1:
            print(count/num1)
            count = count+1
    else:
        count1 = 0
        while count1 <= num2:
            print(count1/num2)
            count1 = count1 + 1


infodesk = input(
    "Which of our products would you like to use: [1.finding factors 2. solving quadratic equations. 3. SH.V.P for two numbers only](enter 1,2 or 3)")
if infodesk == "1":
    print("Wait please ...")
    time.sleep(2)
    finding_factors()

if infodesk == "2":
    print("Wait please ....")
    time.sleep(2)
    quadratic_formula()

if infodesk == "3":
    print("Wait please")
    time.sleep(2)
    shvp_for_two()
