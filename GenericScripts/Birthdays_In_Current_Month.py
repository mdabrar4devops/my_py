birthdays={"abrar":'Nov 4',"nadeem":'Apr 4',"vikram":'Jan 5'}
print ("Enter the name of your friend: ")
name=raw_input()
if name in birthdays:
        print ("This is the birth date of " + name + "  " + birthdays[name])
else:
        print ("Do you want to add as a friend ?")
        response=raw_input("Please Enter y/n ")
        if response=='y':
                new_addition_date=raw_input("Please Enter DOB ")
                birthdays.update({name:new_addition_date})
                print ("Updated the friendlist as below")
                print ( birthdays.keys())
                print ("                ")
                print ("These are the entries")
                print (birthdays)
        else:
                print ("You have choosen not to add them to your birthday reminders")
