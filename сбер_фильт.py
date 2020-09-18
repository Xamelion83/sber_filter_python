import json
import re
new = []
chikol = 0

with open('operations.json', 'r' , encoding='utf-8') as operations:
    lines = json.load(operations)
    new_file=lines[::-1]

for chikol in range(len(new_file)):
    if chikol < 6:
        chikol+=0
        kil = new_file[chikol]
        if kil['state'] == 'EXECUTED':
            new.append(kil)

def kuda():
    to_chet = j["to"]
    res_to_num = "".join(re.findall(r'\d+', to_chet))
    res_to_cart = "".join(re.findall(r'\D', to_chet))
    if len(res_to_num) < 17:
        to_itog = res_to_cart+' '+res_to_num[0:4]+' '+res_to_num[5:7]+'** ****'+' '+res_to_num[12:16]
    else:
        to_itog = res_to_cart+' '+'**'+res_to_num[16:20]
    if j['description'] != "Открытие вклада":
        from_chet = j["from"]
        res_from = "".join(re.findall(r'\d+', from_chet))
        res_from1 = "".join(re.findall(r'\D', from_chet))
        if len(res_from) < 17:
            from_itog = res_from1+' '+res_from[0:4]+' '+res_from[5:7]+'** ****'+' '+res_from[12:16]
        else:
            from_itog = res_from1+' '+'**'+res_from[16:20]
    else:
        from_itog = 'Открытие вклад'
    print (from_itog+' -> '+to_itog)
    
for j in new:
    #дата перевода и описание перевода
    year = j['date'][0:4]
    moth = j['date'][5:7]
    day = j['date'][8:10]
    description = j['description']
    print(day+'.'+moth+'.'+year+' '+description)
    
    kuda()
    
    #сумма перевода и валюта
    operationAmount = j['operationAmount']
    amount = operationAmount['amount']
    currency = operationAmount['currency']
    name = currency['name']
    print(amount+' '+name,'\n')

    


            
    

