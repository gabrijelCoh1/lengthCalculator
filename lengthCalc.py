from tkinter import *

def convert():
    global eq
    global unit1
    global unit2

    try:

        n = float(entry.get())
        unit1, unit2 = clicked1.get(), clicked2.get()
        eq = 0

        if unit1 == unit2:
            eq = n
        #Kilometer##################
        elif unit1 == "Kilometer" and unit2 == "Meter":
            eq = n * 1000
        elif unit1 == "Kilometer" and unit2 == "Decimeter":
            eq = n * 10000
        elif unit1 == "Kilometer" and unit2 == "Centimeter":
            eq = n * 100000
        elif unit1 == "Kilometer" and unit2 == "Millimeter":
            eq = n * 1000000
        elif unit1 == "Kilometer" and unit2 == "Micrometer":
            eq = n * 1000000000
        elif unit1 == "Kilometer" and unit2 == "Nanometer":
            eq = n * 1000000000000
        elif unit1 == "Kilometer" and unit2 == "Mile":
            eq = n / 1.609
        elif unit1 == "Kilometer" and unit2 == "Yard":
            eq = n * 1094
        elif unit1 == "Kilometer" and unit2 == "Foot":
            eq = n * 3281
        elif unit1 == "Kilometer" and unit2 == "Inch":
            eq = n * 39370
        #Meter######################
        elif unit1 == "Meter" and unit2 == "Kilometer":
            eq = n / 1000
        elif unit1 == "Meter" and unit2 == "Decimeter":
            eq = n * 10
        elif unit1 == "Meter" and unit2 == "Centimeter":
            eq = n * 100
        elif unit1 == "Meter" and unit2 == "Millimeter":
            eq = n * 1000
        elif unit1 == "Meter" and unit2 == "Micrometer":
            eq = n * 1000000
        elif unit1 == "Meter" and unit2 == "Nanometer":
            eq = n * 1000000000
        elif unit1 == "Meter" and unit2 == "Mile":
            eq = n / 1609
        elif unit1 == "Meter" and unit2 == "Yard":
            eq = n * 1.094
        elif unit1 == "Meter" and unit2 == "Foot":
            eq = n * 3.281
        elif unit1 == "Meter" and unit2 == "Inch":
            eq = n * 39.37
        #Decimeter######################
        elif unit1 == "Decimeter" and unit2 == "Kilometer":
            eq = n / 10000
        elif unit1 == "Decimeter" and unit2 == "Meter":
            eq = n / 10
        elif unit1 == "Decimeter" and unit2 == "Centimeter":
            eq = n * 10
        elif unit1 == "Decimeter" and unit2 == "Millimeter":
            eq = n * 100
        elif unit1 == "Decimeter" and unit2 == "Micrometer":
            eq = n * 100000
        elif unit1 == "Decimeter" and unit2 == "Nanometer":
            eq = n * 100000000
        elif unit1 == "Decimeter" and unit2 == "Mile":
            eq = n / 16090
        elif unit1 == "Decimeter" and unit2 == "Yard":
            eq = n/ 9.144
        elif unit1 == "Decimeter" and unit2 == "Foot":
            eq = n / 3.048
        elif unit1 == "Decimeter" and unit2 == "Inch":
            eq = n * 3.937
        #Centimeter#####################################3
        elif unit1 == "Centimeter" and unit2 == "Kilometer":
            eq = n / 100000
        elif unit1 == "Centimeter" and unit2 == "Meter":
            eq = n / 100
        elif unit1 == "Centimeter" and unit2 == "Decimeter":
            eq = n / 10
        elif unit1 == "Centimeter" and unit2 == "Millimeter":
            eq = n * 10
        elif unit1 == "Centimeter" and unit2 == "Micrometer":
            eq = n * 10000
        elif unit1 == "Centimeter" and unit2 == "Nanometer":
            eq = n * 10000000
        elif unit1 == "Centimeter" and unit2 == "Mile":
            eq = n / 160900
        elif unit1 == "Centimeter" and unit2 == "Yard":
            eq = n / 91.44
        elif unit1 == "Centimeter" and unit2 == "Foot":
            eq = n / 30.48
        elif unit1 == "Centimeter" and unit2 == "Inch":
            eq = n / 2.54
        #Millimeter###############################
        elif unit1 == "Millimeter" and unit2 == "Kilometer":
            eq = n / 1000000
        elif unit1 == "Millimeter" and unit2 == "Meter":
            eq = n / 1000
        elif unit1 == "Millimeter" and unit2 == "Decimeter":
            eq = n / 100
        elif unit1 == "Millimeter" and unit2 == "Centimeter":
            eq = n / 10
        elif unit1 == "Millimeter" and unit2 == "Micrometer":
            eq = n * 1000
        elif unit1 == "Millimeter" and unit2 == "Nanometer":
            eq = n * 1000000
        elif unit1 == "Millimeter" and unit2 == "Mile":
            eq = n / 609000
        elif unit1 == "Millimeter" and unit2 == "Yard":
            eq = n / 914.4
        elif unit1 == "Millimeter" and unit2 == "Foot":
            eq = n / 304.8
        elif unit1 == "Millimeter" and unit2 == "Inch":
            eq = n / 25.4
        #Micrometer###############################33
        elif unit1 == "Micrometer" and unit2 == "Kilometer":
            eq = n / 1000000000
        elif unit1 == "Micrometer" and unit2 == "Meter":
            eq = n / 1000000
        elif unit1 == "Micrometer" and unit2 == "Decimeter":
            eq = n / 100000
        elif unit1 == "Micrometer" and unit2 == "Centimeter":
            eq = n / 10000
        elif unit1 == "Micrometer" and unit2 == "Millimeter":
            eq = n / 1000
        elif unit1 == "Micrometer" and unit2 == "Nanometer":
            eq = n * 1000
        elif unit1 == "Micrometer" and unit2 == "Mile":
            eq = n / 1609000000
        elif unit1 == "Micrometer" and unit2 == "Yard":
            eq = n / 914400
        elif unit1 == "Micrometer" and unit2 == "Foot":
            eq = n / 304800
        elif unit1 == "Micrometer" and unit2 == "Inch":
            eq = n  / 25400
        #Nanometer###############################
        elif unit1 == "Nanometer" and unit2 == "Kilometer":
            eq = n / 1000000000000
        elif unit1 == "Nanometer" and unit2 == "Meter":
            eq = n / 1000000000
        elif unit1 == "Nanometer" and unit2 == "Decimeter":
            eq = n / 100000000
        elif unit1 == "Nanometer" and unit2 == "Centimeter":
            eq = n / 10000000
        elif unit1 == "Nanometer" and unit2 == "Millimeter":
            eq = n / 1000000
        elif unit1 == "Nanometer" and unit2 == "Mile":
            eq = n * 1609000000000
        elif unit1 == "Nanometer" and unit2 == "Yard":
            eq = n / 914400000
        elif unit1 == "Nanometer" and unit2 == "Foot":
            eq = n / 304800000
        elif unit1 == "Nanometer" and unit2 == "Inch":
            eq = n / 25400000
        #Mile##############################
        elif unit1 == "Mile" and unit2 == "Kilometer":
            eq = n * 1.609
        elif unit1 == "Mile" and unit2 == "Meter":
            eq = n * 1609
        elif unit1 == "Mile" and unit2 == "Decimeter":
            eq = n * 16090
        elif unit1 == "Mile" and unit2 == "Centimeter":
            eq = n * 160900
        elif unit1 == "Mile" and unit2 == "Millimeter":
            eq = n * 1609000
        elif unit1 == "Mile" and unit2 == "Micrometer":
            eq = n * 1609000000
        elif unit1 == "Mile" and unit2 == "Nanometer":
            eq = n / 1609000000000
        elif unit1 == "Mile" and unit2 == "Yard":
            eq = n * 1760
        elif unit1 == "Mile" and unit2 == "Foot":
            eq = n * 5280
        elif unit1 == "Mile" and unit2 == "Inch":
            eq = 63360
        #Yard#######################################
        elif unit1 == "Yard" and unit2 == "Kilometer":
            eq = n / 1094
        elif unit1 == "Yard" and unit2 == "Meter":
            eq = n / 1.094
        elif unit1 == "Yard" and unit2 == "Decimeter":
            eq = n * 9.144
        elif unit1 == "Yard" and unit2 == "Centimeter":
            eq = n * 91.44
        elif unit1 == "Yard" and unit2 == "Millimeter":
            eq = n * 914.4
        elif unit1 == "Yard" and unit2 == "Micrometer":
            eq = n * 914400
        elif unit1 == "Yard" and unit2 == "Nanometer":
            eq = n * 91440000
        elif unit1 == "Yard" and unit2 == "Mile":
            eq = n / 1760
        elif unit1 == "Yard" and unit2 == "Foot":
            eq = n * 3
        elif unit1 == "Yard" and unit2 == "Inch":
            eq = n * 36
        #Foot#######################################
        elif unit1 == "Foot" and unit2 == "Kilometer":
            eq = n / 3281
        elif unit1 == "Foot" and unit2 == "Meter":
            eq = n / 3.281
        elif unit1 == "Foot" and unit2 == "Decimeter":
            eq = n * 3.048
        elif unit1 == "Foot" and unit2 == "Centimeter":
            eq = n * 30.48
        elif unit1 == "Foot" and unit2 == "Millimeter":
            eq = n * 304.8
        elif unit1 == "Foot" and unit2 == "Micrometer":
            eq = n * 304800
        elif unit1 == "Foot" and unit2 == "Nanometer":
            eq = n * 30480000
        elif unit1 == "Foot" and unit2 == "Mile":
            eq = n / 5280
        elif unit1 == "Foot" and unit2 == "Yard":
            eq = n / 3
        elif unit1 == "Foot" and unit2 == "Inch":
            eq = n * 12
        #Inch################################
        elif unit1 == "Inch" and unit2 == "Kilometer":
            eq = n / 39370
        elif unit1 == "Inch" and unit2 == "Meter":
            eq = n / 39.37
        elif unit1 == "Inch" and unit2 == "Decimeter":
            eq = n / 3.937
        elif unit1 == "Inch" and unit2 == "Centimeter":
            eq = n * 2.54
        elif unit1 == "Inch" and unit2 == "Millimeter":
            eq = n * 25.4
        elif unit1 == "Inch" and unit2 == "Micrometer":
            eq = n * 25400
        elif unit1 == "Inch" and unit2 == "Nanometer":
            eq = n * 25400000
        elif unit1 == "Inch" and unit2 == "Mile":
            eq = n / 63360
        elif unit1 == "Inch" and unit2 == "Foot":
            eq = n / 12
        elif unit1 == "Inch" and unit2 == "Yard":
            eq = n / 36
    

        eq = str(eq)
        n = str(n)
        eqLabel.set(f"{n} {unit1} = {eq} {unit2}")

    except Exception as e:
        eqLabel.set(f"error: {e}")

window = Tk()
window.geometry("400x200")
window.title("Length Calculator")
window.config(bg = "#000000")

entry = Entry(window, width = 20, font=25)
entry.pack()

options1 = [
    "Kilometer",
    "Meter",
    "Decimeter",
    "Centimeter",
    "Millimeter",
    "Micrometer",
    "Nanometer",
    "Mile",
    "Yard",
    "Foot",
    "Inch"
]

options2 = [
    "Kilometer",
    "Meter",
    "Decimeter",
    "Centimeter",
    "Millimeter",
    "Micrometer",
    "Nanometer",
    "Mile",
    "Yard",
    "Foot",
    "Inch"
]

clicked1 = StringVar()
clicked2 = StringVar()
clicked1.set(options1[0])
clicked2.set(options2[0])

drop1 = OptionMenu(window, clicked1, *options1)
drop1.pack()
to = Label(window, text="To", font= 25)
to.pack()
drop2 = OptionMenu(window, clicked2, *options2)
drop2.pack()

convert = Button(window, text = "Convert", font = 35, command=convert)
convert.pack()

eqLabel = StringVar()

label = Label(window, textvariable = eqLabel, font = 35, bg= "white")
label.pack()

window.mainloop()