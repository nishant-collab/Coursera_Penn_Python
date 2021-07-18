#Code
#for module 1
def calculator():
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)
        if d_age < 0:
            print(d_age, "is negative")

        elif d_age <= 1:
            human_age = d_age * 15
            human_age = round(human_age, 2)
            print("The given dog age {} is {} in human years.".format(d_age, human_age))

        elif d_age <= 2:
            human_age = d_age * 12
            human_age = round(human_age, 2)
            print("The given dog age {} is {} in human years.".format(d_age, human_age))

        elif d_age <= 3:
            human_age = d_age * 9.3
            human_age = round(human_age, 2)
            print("The given dog age {} is {} in human years.".format(d_age, human_age))

        elif d_age <= 4:
            human_age = d_age * 8
            human_age = round(human_age, 2)
            print("The given dog age {} is {} in human years.".format(d_age, human_age))

        elif d_age <= 5:
            human_age = d_age * 7.2
            human_age = round(human_age, 2)
            print("The given dog age {} is {} in human years.".format(d_age, human_age))

        elif d_age > 5:

        # inserting a new variable "a" to accommodate the age of dog after five years.
             a = d_age - 5
             human_age = (a * 7) + 36
             human_age = round(human_age, 2)
             print("The given dog age {} is {} in human years.".format(d_age, human_age))

