#Creating Library and use the same
class multifunctions():
    def Subfields():
        subfields=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for i in subfields:
           print(i)

    def OddEven():
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(num, "is Even number")
        else:
            print(num, "is Odd number")

    def Elegible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if gender == "Male":
            if age < 21:
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        else:
            if age < 18:
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")

    def percentage():
        sub1 = int(input("Subject1= "))
        sub2 = int(input("Subject2= "))
        sub3 = int(input("Subject3= "))
        sub4 = int(input("Subject4= "))
        sub5 = int(input("Subject5= "))
        total = sub1+sub2+sub3+sub4+sub5
        print("Total: ", total)
        percent = (total/500) * 100
        print("Percentage: ", percent)

    def triangle():
        h = int(input("Height: "))
        b = int(input("Breath: "))
        area = (h*b)/2
        print("Area of Triangle: ", area)
        h1 = int(input("Height1: "))
        h2 = int(input("Height2: "))
        b = int(input("Breath: "))
        peri = h1+h2+b
        print("Perimeter of Triangle: ", peri)

    def BMI():
        bmi=int(input("Enter the BMI Index:"))
        if bmi<18.5:
            print("Under Weight")
        elif bmi<24.9:
            print("Normal Weight")
        elif bmi<29.5:
            print("Over Weight")
        else:
            print("Very Over Weight")
