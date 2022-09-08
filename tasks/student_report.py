# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-26 14:16:31
#  * @modify date 2022-08-26 14:16:31
#  * @desc [description]
#  */
# Actual code starts below this line
# --------------------------------------------------------------


def make_student_report(name : str, roll_no : str, grades : list) -> str:
    
    """
    Input : name, roll_no, grades
    Output : Prints the student report in the following format
                # Student Name: <name>
                # Roll No: <roll_no>
                # Status: <status>
                # GPA: <gpa>
                
    Do not return anything.
    """
    
    # Write your code here
    s = 0
    for i in grades:
        s += i
    gpa = s / len(grades)

    flag = 1
    for i in range(len(grades)):
        if grades[i] <= 5:
            flag = 0

    if flag == 1:
        print('Student Name:',name)
        print('Roll No:', roll_no)
        print('Status: Pass')
        print('GPA:',gpa)
    else:
        print('Student Name:',name)
        print('Roll No:', roll_no)
        print('Status: Fail')
        print('GPA: None')

    return 0


