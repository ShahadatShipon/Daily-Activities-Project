
import datetime
def gettime():
    """This function return immediate date and time"""
    dt= datetime.datetime.now()
    return dt.strftime("%d/%m/%Y , %H:%M:%S")

def update(up_list):
    """This function is for update daily activities list"""
    if up_list==1:
        value = input("Which food have you take? :")
        with open("daily_food.txt" ,"a") as f:
            f.write(str([str(gettime())])+" : "+value+"\n")
        print("Successfully added "+value)

    elif up_list==2:
        amount=int(input("How much do you spend? : "))
        value = input("Where do you spend? :")
        with open("daily_spendings.txt" ,"a") as f:
            f.write(str([str(gettime())])+" : "+value+" : "+str(amount)+"\n")
        print("Successfully added "+value)
    elif up_list==3:
        value = input("What have you studied? :")
        duration=input(" Study duration :")
        with open("study.txt" ,"a") as f:
            f.write(str([str(gettime())])+" : "+value+" - Duration :"+duration+"\n")
        print("Successfully added "+value)

    elif up_list==4:
        value = input("Prayer Name :")
        with open("prayer.txt" ,"a") as f:
            f.write(str([str(gettime())])+" : "+value+"\n")
        print("Successfully added "+value)

    elif up_list==5:
        value = input("How much have slept? :")
        with open("sleep.txt" ,"a") as f:
            f.write(str([str(gettime())])+" : "+value+"\n")
        print("Successfully added "+value)

    elif up_list==6:
        value = input("Which other activities have you done? :")
        with open("other_activities.txt" ,"a") as f:
            f.write(str([str(gettime())])+" : "+value+"\n")
        print("Successfully added "+value)
    else:
        print("You entered wrong input.")

def preview(pre_list):
    """This function is for view daily activities list"""
    if pre_list==1:
        f=open("daily_food.txt")
        print(f.read())
        f.close()
    elif pre_list==2:
        f=open("daily_spendings.txt")
        print(f.read())
        f.close()
    elif pre_list==3:
        f=open("study.txt")
        print(f.read())
        f.close()
    elif pre_list==4:
        f=open("prayer.txt")
        print(f.read())
        f.close()
    elif pre_list==5:
        f=open("sleep.txt")
        print(f.read())
        f.close()
    elif pre_list==6:
        f=open("other_activities.txt")
        print(f.read())
        f.close()
    else:
        print("You entered wrong input.")



print("----------------------Welcome To Daily Activities Project---------------------------------")
loop=1
while(loop):
    print("What do you want to do?\n 1.Update.\n 2.Preview.")
    choice=int(input("Enter your choice : "))
    if choice==1:
        l=1
        while(l):
            print("Which one do you want to update?\n 1.Daily Food.\n 2.Daily Spendings.\n 3.study.\n 4.prayer.\n 5.sleep.\n 6.other acivities.")
            up_list=int(input("Enter your choice :"))
            update(up_list)
            a = input("Wanna update another list?(y/n)")
            if a == "n":
                l = 0
    elif choice==2:
        l=1
        while(l):
            print(
                "Which one do you want to update?\n 1.Daily Food.\n 2.Daily Spendings.\n 3.study.\n 4.prayer.\n 5.sleep.\n 6.other acivities.")
            pre_list = int(input("Enter your choice :"))
            preview(pre_list)
            a = input("Wanna preview another list?(y/n)")
            if a == "n":
                l = 0
    else:
        print("You entered wrong input.\n")
    again=input("Wanna update or preview again?(y/n)")
    if again == "n":
        loop=0