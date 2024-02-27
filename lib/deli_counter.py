katz_deli = []

def line(waiting_list):
    if waiting_list == []:
       message = "The line is currently empty."
    else:
        numbered_names = [f"{index+1}. {name}" for index, name in enumerate(waiting_list)]
        all_names = " ".join(numbered_names)
        message =  f"The line is currently: {all_names}"
    print(message)

def take_a_number(waiting_list, name):
    print(f"Welcome, {name}. You are number {len(waiting_list)+1} in line.")
    new_list = waiting_list.append(name)
    return new_list

def now_serving(waiting_list):
    if waiting_list == []:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {waiting_list[0]}.")
        del(waiting_list[0])
    return waiting_list
    

