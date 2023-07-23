file = open("tNmieVFn.txt", "r")
line = 1

for i in file.readlines():

    line_list = i.split(";")

    if len(line_list) == 4:

        if line_list[0].isspace():
            print(f"Missing title one line: {line}")

        if line_list[1].isspace():
            print(f"Missing author one line: {line}")

        if line_list[2].isspace():
            print(f"Missing ISBN one line: {line}")

        #assuming that valid ISBN number consists from 10 integers
        elif len(line_list[2]) == 10 and line_list[2].isnumeric():
            pass
        else:
            print(f"Invalid ISBN on line: {line}")

        if line_list[3].isspace():
            print(f"Missing price one line: {line}")

        #after loading the file, € switched to "â‚¬" and Kč to "KÄŤ" - firstly checking if price contains these signs
        elif "â‚¬" in line_list[3] or "KÄŤ" in line_list[3]:
            value = line_list[3]

            #delete currency from price and replace , by . so the price can be converted to float
            price = value.replace("â‚¬", "").replace("KÄŤ", "").replace(",",".")
            try:
                price_float = float(price)
                #if the price < 0, it is considered as invalid
                if price_float < 0:
                    print(f"Invalid price on line: {line}")
            except:
                # if the price cannot be converted to float, it is considered as not valid
                print(f"Invalid price on line: {line}")
        else:
            #if currency is missing, price is considered as invalid
            print(f"Invalid price on line: {line}")

    else:
        #in the case if there are less than 4 fields in line, we are not able to find out, what exactly is missing -
        #anything can be considered as title and title cannot be distinguished from author name
        print(f"Invalid CSV line format on line: {line}")

    line += 1


