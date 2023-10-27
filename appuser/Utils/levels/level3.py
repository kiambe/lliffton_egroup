from appuser.Utils.menus import *
from members.Utils.database_queries import *


def level3(custom_text,member_id=None):
    if custom_text[-1] == '1':
        
        return response_menu_savings(custom_text,member_id)
    if custom_text[-1] == '2':
        return response_menu_welfare(custom_text)
    if custom_text[-1] == '3':
        return response_menu_penalties(custom_text)
    if custom_text[-1] == '4':
        return response_menu_loan(custom_text)
    if custom_text[-1] == '5':
        return response_menu_inputs(custom_text)
    if custom_text[-1] == '6':
        return response_menu_market(custom_text)
        