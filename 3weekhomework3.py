This is 1 th homework:
# try:
#     hours=float(input("write here your work hours "))
#     rate=float(input("write here your rate "))
#     if hours > 40:
#         salary = 40 * rate + ((hours - 40) * 1.5 * rate)
#     else:
#         salary = rate * hours
#     print(salary)
# except:
#     print("wrong data")










this is the 2nd:

# try:
#     score=int(input("write here your score "))
#     if score >100 or score<0:
#         print("wrong data")
#         pass
#     elif score >=90:
#         print("your grade is A")
#     elif score >= 80:
#         print("your grade is B")
#     elif score >= 70:
#         print("your grade is C")
#     elif score >= 60:
#         print("your grade is D")
#     elif score < 60:
#         print("your grade is F")
# except:
#     print("wrong data")
# count = 0
# sum = 0
# number = int(input("write number here "))
# if number == 'done':
#     print("sum is ", sum, "and count is ", count)
#     sum += number
#     count+=1
# try:
#     sum += number
#     count+=1
#     while type(number)==int:
#         number = int(input("write number here "))
#         sum+=number
#         count+=1
# except:
#     print("wrong data,write numbers")


this is 3 code: 
obsheekolvo = 0
summa = 0
while True:
    number_inputed=input("write here your number:")
    if number_inputed=="done":
        break
    try:
        number2_inputed=float(number_inputed)
        summa+=number2_inputed
        obsheekolvo+=1
    except:
        print("wrong data,write number")
if obsheekolvo>0:
    srednee=summa/obsheekolvo
    print("sum is ",summa,"and count is ",obsheekolvo,"and average is ",srednee)
else:
    print("no numbers")
    print("no sum,counts and average number")










