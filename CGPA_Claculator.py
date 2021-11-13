def calculate_cgpa(grade_point, credits, num):
    Mark_sum = list()

    for i in range(num):
        Mark_sum.append(grade_point[i] * credits[i])

    cgpa = sum(Mark_sum) / sum(credits)

    return cgpa

if __name__ ==  '__main__': 
    num = int(input("Enter number of subjects : "))

    grade_point = list()
    credits = list()

    for i in range(1, num+1):
        mark = int(input("\nEnter marks of Subject " + str(i) +"  : "))
        credit = int(input("Enter credit of Subject " + str(i) +" : "))

        if 90 <= mark <= 100:
            grade_point.append(10)
        elif 80 <= mark <= 89:
            grade_point.append(9)
        elif 70 <= mark <= 79:
            grade_point.append(8)
        elif 60 <= mark <= 69:
            grade_point.append(7)
        elif 50 <= mark <= 59:
            grade_point.append(6)
        else:
            grade_point.append(0)

        credits.append(credit)

    print("\nCGPA is {:.2f}".format(calculate_cgpa(grade_point, credits, num)))
    