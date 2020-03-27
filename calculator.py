class Calculator:
    def add(string):
        if string == "":
            return 0

        lis = []
        temp_str = ""
        for i in string:
            if i.isdigit() == False:
                lis.append(int(temp_str))
                temp_str = ""
            else:
                temp_str += i

        lis.append(int(temp_str))
        
        sum = 0
        for i in lis:
            if i < 1000:
                sum += i
        
        return sum 
                
        