# # try: 
# #     a = int(input("a: "))
# #     b = int(input("b: "))
# #     c = a+b 
# #     d = a/b
# #     e = a*b

# #     if a == 0:
# #         f = fun1(a)
# #     print("try successful")
# # except ZeroDivisionError:
# #     print("zero division error occured")
# # except NameError:
# #     print("Name error occured")
# # except Exception:
# #     print("exception occured")

# # def fun1(n):
# #     print(n)


# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     C = a/b
#     d = a*b

#     print("try successfull")
# except ZeroDivisionError:
#     print("zero divisoin error")
# except ArithmeticError:
#     print("arthsmetic Error occured")
# except Exception:
#     print("exception occured")



try:
    a = int(input("a: "))
    def checakge(a):
        if a<0:
            raise ValueError("age should be equal and greater to zero")
        print("age is valid")
    checkage(a)
# except ValueError:
#     print("age should be equal and greater to zero")
finally:
    print("executed in any condition")





# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a*b
#     d = a/b 
#     print("try successful", c, d)

# except Exception:
#     print("exception occured")
# finally:
#     print("excuted in any conmdition")




