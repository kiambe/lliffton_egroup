from appuser.Utils.menus import *
def level4(custom_text,member_id):
    if custom_text[-2] == '1':
        if custom_text[-1] == '1':
            savings_total = get_member_savings(custom_text,member_id)
            return response_menu_group_savings(custom_text,savings_total)
        elif custom_text[-1] == '2':
            savings_total = get_member_savings(custom_text,member_id)
            return response_menu_your_savings(custom_text,savings_total)
        elif custom_text[-1] == '3':
            return response_menu_want_to_save(custom_text,member_id)
    elif custom_text[-2] == '2':
        if custom_text[-1] == '1':
            return response_menu_welfare_group_balance(custom_text)
        elif custom_text[-1] == '2':
            return response_menu_welfare_total_savings(custom_text)
        elif custom_text[-1] == '3':
            return response_menu_pay_welfare_savings(custom_text)
    elif custom_text[-2] == '3':
        if custom_text[-1] == '1':
            return response_menu_view_penalties(custom_text)
        elif custom_text[-1] == '2':
            return response_menu_want_to_pay_penalties(custom_text)
    elif custom_text[-2] == '4':
        if custom_text[-1] == '1':
            loans_total = get_group_loans(custom_text,member_id)
            return response_menu_group_loan(custom_text,loans_total)
        elif custom_text[-1] == '2':
            loans_total = get_member_loan(custom_text,member_id)
            return response_menu_my_loan(custom_text,loans_total)
        elif custom_text[-1] == '3':
            return response_menu_apply_input_loan(custom_text)
    elif custom_text[-2] == '5':
        if custom_text[-1] == '1':
            return response_menu_inputs_normal_order(custom_text)
        elif custom_text[-1] == '2':
            return response_menu_market_select_product(custom_text)
    elif custom_text[-2] == '6':
        if custom_text[-1] == '1':
            return response_menu_market_select_product(custom_text)
        elif custom_text[-1] == '2':
            return response_menu_market_select_vendor(custom_text)    

        