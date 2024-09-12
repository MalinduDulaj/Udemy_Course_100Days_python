def format_names(f_name,l_name):
    if f_name == "" or  l_name == "":
        return
    
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result : {format_f_name} {format_l_name}"

print(format_names(input("What is your first name?"), input("What is your last name?")))
