class NegativeNumberException(Exception):
    pass


class Calculator:
    def add(string):
        # if string == "":
        #     return 0

        lis = []
        temp_str = ""
        for i in string:
            if i.isdigit() == False:
                if i == "-":
                    raise NegativeNumberException("Negative number:")
                lis.append(temp_str)
                temp_str = ""
            else:
                temp_str += i

        lis.append(temp_str)
        
        sum = 0
        for i in lis:
            if i.isdigit():
                if int(i) < 1000:
                    sum += int(i)
        
        return sum 
                
        