class Calculator:
    def add(string):
        if string == "":
            return 0
            
        lis = []
        temp_str = ""
        for i in string:
            if i == "," or i.isdigit() == False:
                lis.append(int(temp_str))
                temp_str = ""
            else:
                temp_str += i

        lis.append(int(temp_str))
        return sum(lis)
        