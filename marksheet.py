# marksheet
name = input('please enter your name : ')
roll_no = input('please enter your roll no. : ')
eng = int(input('please enter your english marks ='))
pak_studies = int(input('please enter your pak_studies marks = '))
bio_comp = int(input('please enter your biology or computer marks = '))
chem = int(input('please neter your chemistry makrs = '))
sindhi = int(input('please enter your sindhi marks = '))
obtained_marks = eng + pak_studies + bio_comp + chem + sindhi
print('you have obtained ' + str(obtained_marks) + ' marks in your exam ')
total_marks = 500
per
centage = obtained_marks / total_marks * 100
print('you  have secured ' + str(percentage) + '%  ')

if percentage < 100 and perdentage >= 80:
    print("Congratulations! you got A-1 Grade.")
elif percentage < 80 and percentage>=70:
    print("Congratulations! you got A Grade.")
elif percentage < 70 and percentage>=60:
    print("You got B Grade.")
else:
    print("You are Fail!")