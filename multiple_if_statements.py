province = input('你来自那个省份:')
tax = 0

if province == '黑龙江' or province == '辽宁' or province == '吉林':
    tax = 0.80
elif province in ('浙江','福建'):
    tax = 0.15
else:
    tax = 0.05
print(tax)