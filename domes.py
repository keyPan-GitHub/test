import helpers
from helpers import display
proson = {}
proson['first'] = '黑龙江'
proson['last'] = '辽宁'

susan = {'first':'北京', 'last':'上海'}

print(proson)
print(susan)

people = [proson,susan]
people.append({'first':'浙江', 'last':'福建'})
print(people)

helpers.display('Sample message',True)
display('Sample message',True)
