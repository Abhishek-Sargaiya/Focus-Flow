# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print(str(a) + " - "  + chr(a))
# print(str(b) + " - "  + chr(b))
# print(str(c) + " - "  + chr(c))
# print(str(d) + " - "  + chr(d))


# print("Enter the number of liters to fill the tank")
# a = int(input())

# print("\nEnter the distance covered")
# b = int(input())

# print("\nLiteres/KM")
# fuel = round((a/b)*100, 2)
# print(fuel)



# dis = b * 0.6214
# print("\nMiles/gallons")
# gal = round(a * 0.2642, 2)
# print(round(dis/gal, 2))





# a = int(input("Enter the no of pizzas bought: "))
# b = int(input("Enter the no of puffs bought: "))
# c = int(input("Enter the no of cold drinks bought: "))

# print("Bill Details")

# print("No of pizzas:", a)
# print("No of puffs:", b)
# print("No of cold drinks:", c)
# sum = ((a * 100) + (b * 20) + (c * 10))
# print("No of pizzas:", sum)


# cse = int(input("Enter the no of students placed in CSE: "))
# ece = int(input("Enter the no of students placed in ECE: "))
# mech = int(input("Enter the no of students placed in MECH: "))

# if cse < 0 or mech < 0 or ece < 0:
#     print("invalid input")
#     exit()
    
# if(cse == 0 and mech == 0 and ece == 0):
#     print("None of the department has got the highest placement")
#     exit()

# maxi = max(cse, ece, mech)

# print("Highest Placement")
# if(cse == maxi):
#     print("cse")
#     exit()
    
# if(ece == maxi):
#     print("ece")
#     exit()

# if(mech == maxi):
#     print("mech")
#     exit()
    
    
    
    
    
# a = abs(int(input()))

# for i in range(1, a + 1):
#     if a % i == 0:
#         if i != a:
#             print(i, end=",")
#         else:   print(i)
        
        
        
        
        
        
# a = int(input("Enter the number of semester "))

# subject = list()
# for i in range (a):
#     print("Enter the number of subjects in semester ", i + 1)
#     subject.append(list(range(int(input()))))
    
# for i in range(a):
#     print("Marks obtained in semester", i + 1)
#     for j in range(len(subject[i])):
#         subject[i][j] = int(input())
        
#         if not subject[i][j] in range(0, 101):
#             print("Enter the valid marks")
#             exit()
            
# count = 1
# for i in subject:
#     print("Maximum marks in ", count, " semester", max(i))
#     count += 1
        
        
        
        
        
        
# number_of_items = int(input())

# items = list()

# for i in range(number_of_items):
#     items.append(input().split(" , "))

# dis = list()
# for i in items:
#     dis.append((int(i[1]) * int(i[2]) )// 100)
    
# mini = min(dis)
# result = list()

# for i in dis:
#     if mini == i[3]:
#         result.append(i[0])
        
# for i in result:
#     print(i)
    
    
    
    
# num = int(input("Enter no of courses: "))

# print("Enter the courses name:")

# courses = list()
# for i in range(num):
#     courses.append(input())
    
# search = str(input("Enter the course to be searched: "))

# if search in courses:   print(search, "course is available")
# else:   print(search, "course is not available")
        
        
        
        
        
# car_no = int(input("Enter the car no: "))


# if car_no <= 0 or len(str(car_no)) != 4:
#     print(car_no, "is not a valid number")
#     exit()
    
# sum = 0
# for digit in str(car_no):
#     sum += int(digit)
    
# if sum % 3 == 0 or sum % 5 == 0 or sum % 7 == 0:
#     print("Lucky Number")

# else: print("Sorry its not my lucky number")     





# salary = int(input("Enter the salary: "))
# appraisal = float(input("Enter the performance appraisal rating: "))

# if salary <= 0 or appraisal <= 0 or appraisal > 5:
#     print("Invalid Input")
    
# if appraisal > 0 and appraisal <= 3:
#     inc = salary * 0.1
#     salary += inc
#     print(int(salary))
#     exit()
    
# if appraisal > 3 and appraisal <= 4:
#     inc = salary * 0.2
#     salary += inc
#     print(int(salary))
#     exit()
    
# if appraisal > 4 and appraisal <= 5:
#     inc = salary * 0.3
#     salary += inc
#     print(int(salary))
#     exit()




# number = int(input("Enter number: "))

# number = str(number)
# # rev = "".join(reversed(number))

# rev = number[::-1]
# print("Reversed: ", rev)

# if rev == number:   print("Palindrome")
# else: print("Not Palindrome")


# a = int(input("Enter the starting number: "))
# b = int(input("Enter the ending number: "))

# if a < 2 or b < 2 or a >= b:
#     print("Provide valid input")
#     exit()
    
# for num in range(a, b + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                break
#         else:
#             print(num, end=" ")
        
        
        
        
        
# a = int(input("Enter the month: "))

# if not a in range(0, 13):   print("Enter a valid month")

# if a >= 3 and a <= 5:   
#     print("Season: Spring") 
#     exit()

# if a >= 6 and a <= 8:   
#     print("Season: Summer") 
#     exit()

# if a >= 9 and a <= 11:   
#     print("Season: Autumn") 
#     exit()

# if a == 1 or a == 12 or a == 2:   
#     print("Season: Winter") 
#     exit()



# words = ['Hello', 'World', 'Pyhton']
 
# merge = ' '.join(words)
# print(merge)


# a = ' Hello, World!   '

# b = a.rstrip()
# print(b)



# import sys
# print(sys.version)


# a = int(input("Enter the number of liters to fill the tank: "))
# b = int(input("Enter the distance covered: "))

# if a < 0:
#     print('{} invalid input'.format(a))
#     exit()
# if b < 0:   
#     print('{} invalid input'.format(b))
#     exit()

# liters = ((a/b) * 100)

# print("Liters/100KM", round(liters, 2))


# miles = b * 0.6214
# gallons = a * 0.2642

# print("Miles/Gallons: ", round(miles/gallons, 2))



# pz = int(input("Enter the number of pizzas bought: "))
# pf = int(input("Enter the number of puffs bought: "))
# cd = int(input("Enter the number of cold drinks bought: "))

# total = (pz * 100) + (pf * 20) + (cd * 10)

# print("No. of pizzas bought: {}".format(pz)) 
# print("No. of puffs bought: {}".format(pf)) 
# print("No. of cold drinks bought: {}".format(cd)) 
# print("Total price: {}".format(total))


# print("Enter the digits: ")
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print(str(a) + " - " + chr(a))
# print(str(b) + " - " + chr(b))
# print(str(c) + " - " + chr(c))
# print(str(d) + " - " + chr(d))


# cse = int(input("Enter the number of students placed in CSE: "))
# ece = int(input("Enter the number of students placed in ECE: "))
# mech = int(input("Enter the number of students placed in MECH: "))

# if cse == ece and ece == mech:
#     print("None of the departments has got the highest placement")
#     exit()

# if cse < 0 or ece < 0 or mech < 0:  
#     print("invalid input")
#     exit()

# maxi = max(cse, max(ece, mech))

# if maxi == cse: 
#     print("CSE")

# if maxi == ece: 
#     print("ECE")

# if maxi == mech: 
#     print("MECH")