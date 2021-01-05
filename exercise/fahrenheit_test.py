# import fahrenheit as fah
from fahrenheit import conversion

print('press the celcius number')
celcius = float(input())
print('섭씨온도 : ', celcius)
print('화씨온도 : {:.2f}'.format(conversion(celcius)))
