from datetime import datetime
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty-One', 22: 'twenty-two', 23: 'twenty-three', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 0: 'zero', 00: 'zero'}

def convert24(time):
    t = datetime.strptime(time, '%I:%M%p')

    return t.strftime('%H:%M')

def convertText(time):
    string = []
    time_list = time.split(":")
    hour = time_list[0]
    minutes_list = list(time_list[1])
    if int(hour) < 10 and int(hour) != 00:
      hour_list = list(time_list[0])
      for i in range(len(hour_list)):
          string.append(num2words[int(hour_list[i])])
    elif int(hour) == 00:
          string.append(num2words[int(hour)])
    else:
          string.append(num2words[int(hour)])
    if minutes_list[0] == "0" and minutes_list[1] == "0":
          string.append("hundred hours")
    else:
        if int(minutes_list[0]) > 1:
              minutes_list[0] = minutes_list[0] + "0"
        for i in range(len(minutes_list)):
              string.append(num2words[int(minutes_list[i])])
    return (' '.join(string))

time = convert24("4:00PM")
print(convertText(time))