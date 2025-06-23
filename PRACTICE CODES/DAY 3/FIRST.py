#dictionary
d ={'sr.':'fruits',1:'apple',2:'banana',3:'grapes'}
print (d)
print(type(d))
print(d['sr.'])
print(type(d['sr.']))
print(d[1])

d[4]='kiwi' #adding an element to the dictionary
print(d)

dictionary = {}
dic = int(input("enter number of dic elements:"))
for i in range(dic):
    value = int(input("enter key of dic elements:"))
    element = input("enter values of dic elements:")
    dictionary[value] = element
    print(f"\n{dictionary}")

final_dic = dictionary.copy()
print(f" \nfinal dictionary : {final_dic}")

clear_dic = dictionary.clear()
print(f" \nclear dictionary : {clear_dic}")

print(f"all the values in final_dic : {final_dic.values()}")
# print(f"all the values in final_dic : {final_dic.pop(2)}")
print(final_dic)

d.update(final_dic)
print(d)
