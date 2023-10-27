from appuser.Utils.menus import response_menu_one,response_decline_conditions
def level2(custom_text):
    if custom_text[-2] == '1':
        return response_menu_one(custom_text)
    elif custom_text[-2] == '2':
        return response_decline_conditions(custom_text)