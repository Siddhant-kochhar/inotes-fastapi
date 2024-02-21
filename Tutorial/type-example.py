#firstname:str -- means we are defining the type ki kis type ka hoga
def add(first_name:str,last_name:str):
    first_name = first_name.capitalize()
    return first_name+" "+last_name
fname = "bill"
lname="Gates"
name = add(fname,lname)
print(name)