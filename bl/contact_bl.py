from dal.sourcefile_management import save_data


CONTACT_FILE_PATH = r"file/contact.txt"

def save_contact(contact: tuple):
    function_res = {
        "SUCCESS": True,
        "ERR_MSG": {},
        "SUCC_MSG": {},
        "RETURN_DATA": None
    }

    name = contact[0].strip()
    family = contact[1].strip()
    phone = contact[2].strip()
    gender = contact[3].strip()
    description = contact[4].strip()

    # region validation
    if not name:
        function_res['ERR_MSG']["name"] = "Name is empty!"
    elif not name.replace(" ", "").isalpha():
        function_res['ERR_MSG']["name"] = "Name is not alphabetic!!"

    if not family:
        function_res['ERR_MSG']["family"] = "Family is empty!"
    elif not family.replace(" ", "").isalpha():
        function_res['ERR_MSG']["family"] = "Family is not alphabetic!!"

    if not phone:
        function_res['ERR_MSG']["phone"] = "Phone is empty!"
    elif not phone.isdecimal():
        function_res['ERR_MSG']["phone"] = "Phone TypeError !!"
    elif len(phone) != 11:
        function_res['ERR_MSG']["phone"] = "Phone lenError !!"
    
    with open('file/contact.txt', 'r') as file:
                lines = file.readlines()
    with open('file/contact.txt', 'r') as file:
        for line in lines:
            if phone in line:
                function_res['ERR_MSG']["phone"] = "This number exists"


    if not gender:
        function_res['ERR_MSG']["gender"] = "gender is empty!"
    elif gender not in ("male", "female", "other"):
        function_res['ERR_MSG']["gender"] = "gender Valuerror !!"

    # endregion

    if function_res["ERR_MSG"]:
        function_res["SUCCESS"] = False
        return function_res
    

    result = save_data(
        file= CONTACT_FILE_PATH,
        user_data = f"Name: {name} - Family: {family} - Gender: {gender} - Phone: {phone} - Description: {description}\n"
           )

    if not result["SUCCESS"]:
        function_res["SUCCESS"] = False
        function_res["ERR_MSG"]["Data source"] = "Data source error"
        return function_res

    function_res["SUCC_MSG"]["hora"] = "Success msg"
    return function_res
