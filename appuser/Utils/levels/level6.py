from appuser.Utils.menus import *
def level6(custom_text,member_id,phone_number):
    if custom_text[-2] == '1':

        if custom_text[-4] == '4':
            return response_menu_input_loan_confirm(custom_text,member_id,phone_number)
        # post to db
        member_save_to_group(custom_text,member_id)
        return response_menu_want_to_save_yes_amount(custom_text,member_id,phone_number)
    elif custom_text[-2] == '2':
        return response_menu_pay_welfare_savings_stk(custom_text)
    elif custom_text[-2] == '3':
        return response_menu_pay_penalties_stk(custom_text)

    