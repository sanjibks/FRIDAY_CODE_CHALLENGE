import json


"""Defining a function to convert string of address to json object with required components
   As the addresses are random strings there can't be a generic way to handle all the addresses. So, only considering the cases provided in the sample data.
   Assuming the addresses are passed one by one as arguments to the below function.
"""

def address_split(address):
    
    """
    Recursively parsing the "address" with conditions as per the sample data to convert it into a "," separated string. 
    where the street and the house number will be separated by ',' and then the "street" and "housenumber" components are extracted.
    Then returned as json object
    """

    """defining an empty dictionary to store the street and housenumber"""
    street_house={"street":'',"housenumber":''}
    

    """
    Checking if the address string has street and housenumber separated by ",".
    If it has, then the street and housenumber are collected and returned.
    """
    
    if ',' in address:

        """trying to satisfy the 3(iv) case in the "if" clause and "else" clause is for other cases"""
        if sum([int(any(map(str.isdigit, i))) for i in address.split()]) > 1:
            array_address=[val.strip() for val in address.split(',')]
            array_address.reverse()
        else:            
            array_address=sorted([val.strip() for val in address.split(',')])
        
        street_house["street"]=array_address[1]
        street_house["housenumber"]=array_address[0]

        return json.dumps(street_house, ensure_ascii=False)

    
    """converting the "addesss" into "," separated addeass """ 
   
    if address[0].isdigit():
        address_new=address.replace(' ', ',', 1)
         
    elif sum([int(any(map(str.isdigit, i))) for i in address.split()]) > 1:
        for i in address.split():
            if any(map(str.isdigit, i)):
                num = i
                break
            
        address_new= address[0:address.index(num)+len(num)]+','+address[address.index(num)+len(num):]
        
    elif sum([int(any(map(str.isdigit, i))) for i in address.split()]) == 1:
        for i in address.split():
            if any(map(str.isdigit, i)):
                num = i
                break
            
        address_new= address[0:address.index(num)]+','+address[address.index(num):]

    return address_split(address_new)


if __name__ == "__main__":
    address="Calle 39 No 1540"
    print(address_split(address))
