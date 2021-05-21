def crawling(accountList):
    currencyList =[]
    for a in accountList :
        if(a['currency'] == 'KRW'):
            continue
        currencyList.append(a['currency'])
    print(currencyList)