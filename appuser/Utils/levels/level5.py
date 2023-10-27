from appuser.Utils.menus import *
def level5(custom_text):
    if custom_text[-3] == '1':
        if custom_text[-1] == '1':
            # savings
            
            return response_menu_want_to_save_yes(custom_text)
        elif custom_text[-1] == '2':
            return response_menu_want_to_save_no(custom_text)
    elif custom_text[-3] == '2':
        return response_menu_pay_welfare_savings_stk(custom_text)
    elif custom_text[-3] == '3':
        if custom_text[-1] == '1':
            return response_menu_pay_penalties_yes(custom_text)
        elif custom_text[-1] == '2':
            return response_menu_pay_penalties_no(custom_text)
        
    elif custom_text[-3] == '5':
        if custom_text[-2] == '1':
            if custom_text[-1] == '1':
                return response_menu_inputs_normal_select_product(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_inputs_normal_select_vendor(custom_text)
        elif custom_text[-2] == '2':
            if custom_text[-1] == '1':
                return response_menu_inputs_voucher_select_indicate_id_number(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_inputs_normal_select_vendor(custom_text) 
            elif custom_text[-1] == '3':
                return response_menu_inputs_voucher_accept_voucher(custom_text) 
        else:
            pass