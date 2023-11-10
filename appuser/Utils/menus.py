from appuser.Utils import constants
from accounts.Utils.database_queries import *

from .sms_module import App_SMS
from .utils import *
def response_session_ended():
    response = ''
    response = f'END This session has ended. \n'

    return response


def response_menu_landing(custom_text_two):
    # Level 1
    response = f'CON Welcome to {constants.APP_NAME} \n'
    response += "1. Accept terms and conditions \n"
    response += "2. Decline \n"
    
    
    return response

def response_decline_conditions(custom_text_two,msg=""):
    response = f'END {msg}\n'
    response += "Thank you for using the E-Group system \n"
    return response

def response_have_no_groups(custom_text_two):
    response = f'END '
    response += "You seem not to be registered in any group. Kindly contact your admin. Thank you for using the E-Group system \n"
    return response

def response_not_registered(custom_text_two):
    response = f'END '
    response += "You seem not to be registered in the E-Group system. Kindly contact your admin. Thank you for using the E-Group system \n"
    return response

def response_select_group(custom_text_two,member_id):
    # Level 1
    response_groups = Put_Groups_to_String(member_id)
    
    # print(response_groups)
    response = f'CON Select group\n'
    response += response_groups['response']
    
    
    return response


def response_menu_one(custom_text_two):
    # Level 1
    response = f'CON '
    response += "1. Savings \n"
    response += "2. Welfare \n"
    response += "3. Penalties \n"
    response += "4. Loans \n"
    response += "5. Inputs \n"
    response += "6. Market \n"
    

    return response


# Savings

def response_menu_savings(custom_text_two,member_id):
    group_code =get_group_member_id_from_text(custom_text_two,member_id)["group_code"]
    group_name =get_group_member_id_from_text(custom_text_two,member_id)["group_name"]
    
    response = f'CON Savings for group {group_name}\n'
    response += "1. Group Savings balance \n"
    response += "2. Your savings balance \n"
    response += "3. Do you want to save? \n"
    response += constants.FOOTER_RESPONSE
    return response

def response_menu_group_savings(custom_text_two,savings):
    response = f'END Savings\n'
    response += f"Group Savings balance is ksh {savings} \n"
    return response

def response_menu_your_savings(custom_text_two,savings):
    response = f'END Savings\n'
    response += f"Your Group Savings balance is ksh {savings} \n"
    return response

def response_menu_want_to_save(custom_text_two,member_id):
    group_code =get_group_member_id_from_text(custom_text_two,member_id)["group_code"]
    group_name =get_group_member_id_from_text(custom_text_two,member_id)["group_name"]
    response = f'CON Sure to save for group {group_name}?\n'
    response += "1. Yes \n"
    response += "2. No \n"
    return response

def response_menu_want_to_save_yes(custom_text_two):
    response = f'CON Savings\n'
    response += "Enter the amount you want to save \n"
    response += constants.FOOTER_RESPONSE
    return response

def response_menu_want_to_save_yes_amount(custom_text_two,member_id,phone_number):
    response = f'END Savings\n'
    amount = custom_text_two[-1]

    if amount.isnumeric():
        phone_number = phone_number
        group_code =get_group_member_id_from_text(custom_text_two,member_id)["group_code"]
        group_name =get_group_member_id_from_text(custom_text_two,member_id)["group_name"]
        
        
        member_object =get_group_member_id_from_text(custom_text_two,member_id)["member_id_object"]
        # member_object_first_name = member_object.firts_name
        # print(member_object.first_name)
        
        # send MPESA stk in future
        # response += f"You are saving Ksh {amount}. An STK push will be sent to your phone \n"
        response += f"Success! You have saved Ksh {amount} for group {group_name} \n"
        
        # send sms here
        msg = None
        
        if member_object.first_name != None:
        
            msg = f"Dear {member_object.first_name}, You have saved KSH {amount} for group {group_name}"
        else:
            msg = f"You have succcessfully saved KSH {amount} for group {group_name}"
            
        

        sms_to_send = App_SMS(phone=phone_number,msg=msg)
        
        sms_to_send.send_sms()
        
        return response
    else:
        return "END Amount is not numeric. Please try again."

def response_menu_want_to_save_no(custom_text_two):
    response = f'END Savings\n'
    response += "Thank you for using the E-Group system \n"
    return response

# end savings



# welfare

def response_menu_welfare(custom_text_two):
    response = f'CON Welfare\n'
    response += "1. View Welfare group balance \n"
    response += "2. View Your welfare total savings \n"
    response += "3. Pay for your welfare savings \n"
    response += constants.FOOTER_RESPONSE
    return response


def response_menu_welfare_group_balance(custom_text_two):
    response = f'END Welfare\n'
    response += "Welfare group balance is ksh 10,000 \n"
    return response
def response_menu_welfare_total_savings(custom_text_two):
    response = f'END Welfare\n'
    response += "Your welfare total savings is ksh 10,000 \n"
    return response

def response_menu_pay_welfare_savings(custom_text_two):
    response = f'CON Welfare\n'
    response += "Enter the amount you want to save \n"
    return response

def response_menu_pay_welfare_savings_stk(custom_text_two):
    response = f'END Welfare\n'
    amount = custom_text_two[-1]
    # response += f"Welfare amount Ksh {amount}. An STK push will be sent to your phone \n"
    response += f"Success! Saved welfare amount Ksh {amount}. \n"
    
    return response


# penalties

def response_menu_penalties(custom_text_two):
    response = f'CON Penalties\n'
    response += "1. View penalties\n"
    response += "2. Do you want to pay for penalties  \n"
    response += constants.FOOTER_RESPONSE
    return response
def response_menu_view_penalties(custom_text_two):
    response = f'END Penalties\n'
    response += "Penalties is ksh 10,000 \n"
    return response


def response_menu_want_to_pay_penalties(custom_text_two):
    response = f'CON Penalties\n'
    response += "1. Yes \n"
    response += "2. No \n"
    return response

def response_menu_pay_penalties_yes(custom_text_two):
    response = f'CON Penalties\n'
    response += "Enter the amount you want to save \n"
    return response

def response_menu_pay_penalties_stk(custom_text_two):
    response = f'END Penalties\n'
    amount = custom_text_two[-1]
    # response += f"Penalty of Ksh {amount}. An STK push will be sent to your phone \n"
    response += f"Penalty of Ksh {amount}. \n"
    
    
    return response

def response_menu_pay_penalties_no(custom_text_two):
    response = f'END Penalties\n'
    response += "Thank you for using the E-Group system \n"
    return response


# loan

# View group no of loans outstanding  (output-> 4 members)
# -View your loan amount outstanding 
# -Apply for input loan(receive message for with voucher code once loan approved )***Only applicable if the member doesn’t have any ousstanding bal,max 3 times savings *** 

def response_menu_loan(custom_text_two):
    response = f'CON Loan\n'
    response += "1. View group no of loans outstanding\n"
    response += "2. View your loan amount outstanding   \n"
    response += "3. Apply for input loan   \n"
    response += constants.FOOTER_RESPONSE
    return response

def response_menu_group_loan(custom_text_two,loan):
    response = f'END Loan\n'
    response += f"Group loan is ksh {loan} \n"
    return response

def response_menu_my_loan(custom_text_two,loan):
    response = f'END Loan\n'
    response += f"Your loan is ksh {loan} \n"
    return response
def response_menu_apply_input_loan(custom_text_two):
    response = f'END Loan\n'
    response += "You will receive an SMS message with voucher code once loan approved \n"
    return response



# input


# Inputs
# -Make order from inputs (normal order,or using voucher order ) 
# 1.Normal Order
# 2.Voucher
# -If normal order
# 1.	Select product
# 2.	Select vendor
# 3.	Pay
# If voucher
# 1.	Indicate id no.(generate the voucher no)
# 2.	Select vendor
# 3.	Accept redeeming the voucher

def response_menu_inputs(custom_text_two):
    response = f'CON Make order from inputs\n'
    response += "1. Make normal order\n"
    response += "2. Make order with voucher\n" 
    response += constants.FOOTER_RESPONSE   
    return response

# If normal order
def response_menu_inputs_normal_order(custom_text_two):
    response = f'CON Make order from inputs\n'
    response += "1. Select product\n"
    response += "2. Select vendor\n" 
    response += "3. Pay\n"    
    response += constants.FOOTER_RESPONSE
       
    return response


def response_menu_inputs_normal_select_product(custom_text_two):
    # Put_Product_to_String
    products = Put_Product_to_String()
    response = f'CON Make order from inputs\n'
    response += products['response']
    response += constants.FOOTER_RESPONSE    
    
    return response

def response_menu_inputs_normal_select_vendor(custom_text_two):
    vendors = Put_Vendors_to_String()
    
    response = f'CON Make order from inputs\n'
    response += vendors['response']
    response += constants.FOOTER_RESPONSE   
    
    return response

# If voucher

def response_menu_inputs_voucher_order(custom_text_two):
    response = f'CON Make order from inputs\n'
    response += "1. Indicate ID number\n"
    response += "2. Select vendor\n" 
    response += "3. Accept redeeming the voucher\n"
    response += constants.FOOTER_RESPONSE  
    return response
    

def response_menu_inputs_voucher_select_indicate_id_number(custom_text_two):
    response = f'CON Enter your ID number\n'
    
    return response

def response_menu_inputs_voucher_generate_voucher(custom_text_two,member_id,phone_number):
    voucher = generateRandomInt()
    saveVoucherToDatabase(voucher)

    group_name =get_group_vender_id_from_text(custom_text_two,member_id)["group_name"]
    vendor_name =get_group_vender_id_from_text(custom_text_two,member_id)["vendor_name"]
    product_name =get_group_vender_id_from_text(custom_text_two,member_id)["product_name"]
    product_retail_price =get_group_vender_id_from_text(custom_text_two,member_id)["product_retail_price"]
    


    # get_group_vender_id_from_text
    message = f"Loan has been approved for group {group_name}.KSH {product_retail_price}, Product loan for {product_name} from Vendor {vendor_name}. Voucher code is {voucher}"
    # member_save_loan

    member_save_loan(custom_text_two,member_id,"Product loan",product_retail_price)
    sms_to_send = App_SMS(phone=phone_number,msg=message)
    
    sms_to_send.send_sms()

    response = f'END  {message}\n'
    
    return response
def response_menu_inputs_voucher_accept_voucher(custom_text_two):
    response = f'END Voucher accepted\n'
    
    return response


# end inputs

# market

# Market
# -List product
# -look for vendors for aggregation 
def response_menu_market(custom_text_two):
    response = f'CON Market\n'
    response += "1. List products\n"
    response += "2. Look for vendors for aggregation \n"   
    response += constants.FOOTER_RESPONSE 
    return response

def response_menu_market_select_product(custom_text_two):
    products = Put_Product_to_String()
    response = f'CON List of products\n'
    response += products['response']
    response += constants.FOOTER_RESPONSE
    
    return response

def response_menu_market_select_vendor(custom_text_two):
    response = f'CON List of vendors\n'
    vendors = Put_Vendors_to_String()
    response += "1. Vendor 1\n"
    response += vendors['response']
    response += constants.FOOTER_RESPONSE
    
    return response

def response_menu_input_loan_select_vendor(custom_text_two):
    response = f'CON Select vendor\n'
    vendors = Put_Vendors_to_String()

    response += vendors['response']
    response += constants.FOOTER_RESPONSE   
    
    return response


def response_menu_input_loan_select_product(custom_text_two):
    products = Put_Product_to_String()
    response = f'CON Select product\n'
    response += products['response']
    response += constants.FOOTER_RESPONSE
    
    return response


def response_menu_input_loan_confirm(custom_text_two,member_id,phone_number):

    group_name =get_group_vender_id_from_text(custom_text_two,member_id)["group_name"]
    vendor_name =get_group_vender_id_from_text(custom_text_two,member_id)["vendor_name"]
    product_name =get_group_vender_id_from_text(custom_text_two,member_id)["product_name"]
    product_retail_price =get_group_vender_id_from_text(custom_text_two,member_id)["product_retail_price"]

    # product_retail_price
    
    response = f'CON Are you sure you want to take KSH {product_retail_price} {product_name} loan form {vendor_name}?\n'
    response += f"1. Yes \n"
    response += f"2. No \n"
    response += constants.FOOTER_RESPONSE
    
    return response

