from datetime import datetime
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 0: 'zero', 00: 'zero'}

def convert24(time):
    t = datetime.strptime(time, '%I:%M%p')
    return t.strftime('%H:%M')

def convertTimeToText(time):
    time_string = []
    time_list = time.split(":")
    hour = time_list[0]
    minutes = time_list[1]
    if int(hour) < 10:
        hour_list = list(hour)
        for i in range(len(hour_list)):
            time_string.append(num2words[int(hour_list[i])])
    else:
        time_string.append(convertNumberToText(hour))
    
    if minutes == "00":
        time_string.append("hundred hours")
    elif int(minutes) < 10:
        minutes_list = list(minutes)
        for i in range(len(minutes_list)):
            time_string.append(num2words[int(minutes_list[i])])
    elif int(minutes) >= 10 and int(minutes) <= 19:
        time_string.append(num2words[int(minutes)])
    elif int(minutes) == 20 or int(minutes) == 30 or int(minutes) == 40 or int(minutes) == 50:
        time_string.append(num2words[int(minutes)])
    else:
        minutes_list = list(minutes)
        minutes_list[0] = minutes_list[0] + "0"
        for i in range(len(minutes_list)):
            time_string.append(num2words[int(minutes_list[i])])
    return (' '.join(time_string))


def convertNumberToText(time):
    return num2words[int(time)]

time = convert24("1:33PM")
print(convertTimeToText(time))
