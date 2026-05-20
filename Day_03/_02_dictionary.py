# dictionary are used for storing data in key-value pairs

daysConversion = {
    "1" : "Sunday",
    "2" : "Monday",
    "3" : "Tuesday",
    "4" : "Wednesday",
    "5" : "Thursday",
    "6" : "Friday",
    "7" : "Saturday",
}

# if the key exists, it will return the value
# if the key does not exist, it will return the default value
# in this case, "Invalid day"
print(daysConversion.get("1", "Invalid day"))

