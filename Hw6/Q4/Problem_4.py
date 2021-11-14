

def delete_keys(keys, dict):
    for a in keys:
        if a in dict:
            dict.pop(a)
    print(dict)





dict = {"firstname":"Mohamed", "lastname":"Farag", "birthYear":1990, "nationality": "Egpytian"}
delete_keys(["lastname", "birthYear"], dict)

