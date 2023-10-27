from appuser.Utils.menus import response_select_group,response_decline_conditions
def level1(custom_text,member_id):
    if custom_text[-1] == '1':
            # return response_menu_one(custom_text)
        return response_select_group(custom_text,member_id)
    elif custom_text[-1] == '2':
        return response_decline_conditions(custom_text)