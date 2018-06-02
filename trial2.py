def forecastload():
    wb = load_workbook(filename = 'pjmactualload.xlsx')
    ws = wb['PJM Load']    
    printRow = 13
    #put this in iteration to pull 2 rows of data at a time (one for each day) for 7 days max
    day = 239
    while day < 251:
        #pulls in first day only
        data = pd.read_csv("http://oasis.pjm.com/doc/projload.txt", skiprows=day, delim_whitespace=True, header=None, nrows=2)

        #sets data at HE 24 = to data that is in HE 13- so I can delete column 0 data to allow checking 'max'
        data.at[1,13]= data.at[1,1]

        #get date for printing it with max load later on
        newDate = str(data.at[0,0])

        #now delete first column to get rid of date data.  date already saved as newDate
        data = data.drop(0,1)
        data = data.drop(1,1)

        #pull out max value of day
        #add index to this for iteration ie dayMax[x] = data.values.max()
        dayMax = data.max().max()
        dayMin = data.min().min()
        #print date and max load for that date
        actualMax = "Forecast Max"
        actualMin = "Forecast Min"
        dayMax = int(dayMax)
        maxResults = [str(newDate),int(dayMax),actualMax,dayMin,actualMin]
        d = 1
        for items in maxResults:
            ws.cell(row=printRow, column=d).value = items
            d += 1        
        printRow += 1        
        #print maxResults
        #l.writerows(maxResults)    
        day = day + 2
    wb.save('pjmactualload.xlsx')