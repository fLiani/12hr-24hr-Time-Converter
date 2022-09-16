def timeConversion(s):
    
    hour = s[:2]                                        # Creating a variable for the hour (HH)
    
    if s[-2:] == "AM" and hour == "12":                 # Checking for midnight
        hour = "00"                                     # If true convert to 24hr
        return hour + s[2:8]                            # Return new 24hr hour + the rest of the time
    
    elif s[-2:] == "PM" and hour != "12":               # Checking for afternoon times
        hour = str(int(hour) + 12)                      # Add 12 hours to the hour and convert back to string
        return hour + s[2:8]                            # Add the rest of the time
    
    else:
        return s[:8]                                    # Remove AM/PM
    
time = input("Enter a 12hr time (HH:MM:SS(AM/PM)): ")

print(timeConversion(time))