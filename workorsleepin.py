# Accept an input from 0-6 to correspond to each day of the week
day = int(input("Day(0-6)?: "))

# if day is a weekday (from Monday (=1) up to and including Fri (=5)), print "Go to Work!". 
if day in range(1,6):
    print("Go to Work!")

# if day is a weekend (Satuday (=6) or Sunday (=0), print "Sleep In")
elif day == 0 or day == 6:
    print("Sleep In")

# if user can't follow simple instructions :-[
else:
    print("Wrong input, Bucko!  Try Again.")





