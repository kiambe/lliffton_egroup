from accounts.models import *
from accounts.serializer import *
from appuser.Utils.utils import getRealIDForRepID
import json

def get_member_details_from_phone(phone_number="254791836987"):
    try:
        member = Member.objects.get(primary_phone_number=phone_number)
        try:
            serializer_member = MemberSerializer(member).data
            # print(serializer_member)
        except:
            print("error!")
            return None
            
        return {"dict":member,"json":serializer_member}
    except:
        return None

def get_member_groups(member_id):
    try:
        groups = GroupMembers.objects.filter(member_id=member_id)
        serializer_groups = GroupMembersSerializer(groups,many=True).data
        
        return serializer_groups
    except:
        print("groups not found")
        return None
        
def Put_Groups_to_String(member_id): 
    
    print(f" member_id is {member_id}")
    groups = []
    member_groups = get_member_groups(member_id=member_id)
    
    if member_groups == None:
        return None
    
    for x in member_groups:
        my_object= {
            "id":x["group_id"],
            "group_name":x['group_name'],
            "group_code":x['group_code'],
            
        }
        
        groups.append(my_object)
    
    
    
    print(f" groups is {groups}")
    

    group_rep_id_plus_id = []
    group_rep_id = []

    # groups = json.loads(groups)

    response = ""

    for idx, val in enumerate(groups):
        group_db_id = val['id']
        group_code=val['group_code']
        group_name=val['group_name']
        
        group_rep_id_plus_id.append({"rep_id": idx+1, "id": group_db_id})
        
        group_rep_id.append(idx+1)
        
        response_to_be_added = f'{idx+1}' + ". " +  group_name + "\n"
        response += response_to_be_added
        

    print(f"rep_id {group_rep_id}")

    return {"response": response, "rep_id_plus_id": group_rep_id_plus_id,
            "rep_id": group_rep_id}


def get_vendors():
        
    try:
        data = Vendor.objects.all()
        serializer_data = VendorsSerializer(data,many=True).data
        return serializer_data
    except:
        print("error!")
        return None
 
def get_products():
        
    try:
        data = Product.objects.all()
        serializer_data = ProductsSerializer(data,many=True).data
        return serializer_data
    except:
        print("error!")
        return None           

def Put_Product_to_String():
    product = get_products()
    print("product")
    print(product)
    
    product_rep_id_plus_id = []
    product_rep_id = []

    # groups = json.loads(groups)

    response = ""

    for idx, val in enumerate(product):
        product_db_id = val['id']
        
        name=val['name']
        
        product_rep_id_plus_id.append({"rep_id": idx+1, "id": product_db_id})
        
        product_rep_id.append(idx+1)
        
        response_to_be_added = f'{idx+1}' + ". " +  name + "\n"
        response += response_to_be_added
        

    print(f"rep_id {product_rep_id}")

    return {"response": response, "rep_id_plus_id": product_rep_id_plus_id,
            "rep_id": product_rep_id}


def Put_Vendors_to_String():
    vendors = get_vendors()
    print("vendors")
    print(vendors)
    
    vendor_rep_id_plus_id = []
    vendor_rep_id = []

    # groups = json.loads(groups)

    response = ""

    for idx, val in enumerate(vendors):
        vendor_db_id = val['id']
        
        name=val['business_name']
        
        vendor_rep_id_plus_id.append({"rep_id": idx+1, "id": vendor_db_id})
        
        vendor_rep_id.append(idx+1)
        
        response_to_be_added = f'{idx+1}' + ". " +  name + "\n"
        response += response_to_be_added
        

    print(f"rep_id {vendor_rep_id}")

    return {"response": response, "rep_id_plus_id": vendor_rep_id_plus_id,
            "rep_id": vendor_rep_id}


def SumMemberSavings(array):
    
    if len(array) != 0:
        savings_sum = 0
        for x in array:
            saving = x['amount']
            savings_sum += saving
        return savings_sum
    else:
        return f"0.00"
  
def get_member_savings(custom_text,member_id):
    group_selected = custom_text[1]
    member_groups_string = Put_Groups_to_String(member_id=member_id)


    member_id_rep_plus_id = member_groups_string["rep_id_plus_id"]

    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    
    savings = Saving.objects.filter(group_id=group_id).filter(member_id=member_id)
    savings_serializer = SavingsSerializer(savings,many=True).data
    
    
    return SumMemberSavings(savings_serializer)

def get_group_savings(custom_text,member_id):
    group_selected = custom_text[1]
    member_groups_string = Put_Groups_to_String(member_id=member_id)


    member_id_rep_plus_id = member_groups_string["rep_id_plus_id"]

    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    
    savings = Saving.objects.filter(group_id=group_id)
    savings_serializer = SavingsSerializer(savings,many=True).data
    
    return SumMemberSavings(savings_serializer)


def get_member_loan(custom_text,member_id):
    group_selected = custom_text[1]
    member_groups_string = Put_Groups_to_String(member_id=member_id)


    member_id_rep_plus_id = member_groups_string["rep_id_plus_id"]

    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    
    loans = Loan.objects.filter(group_id=group_id).filter(group_member_id=member_id)
    loans_serializer = LoansSerializer(loans,many=True).data
    
    
    return SumMemberSavings(loans_serializer)

def get_group_loans(custom_text,member_id):
    group_selected = custom_text[1]
    member_groups_string = Put_Groups_to_String(member_id=member_id)

    member_id_rep_plus_id = member_groups_string["rep_id_plus_id"]

    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    
    loans = Loan.objects.filter(group_id=group_id)
    loans_serializer = LoansSerializer(loans,many=True).data
    
    return SumMemberSavings(loans_serializer)

def get_group_member_id_from_text(custom_text,member_id):
    group_selected = custom_text[1]
    
    member_groups_string = Put_Groups_to_String(member_id=member_id)

    member_id_rep_plus_id = member_groups_string["rep_id_plus_id"]
    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    print(member_id_rep_plus_id)
    print(group_id)
    
    
    
    group_id_object = Group.objects.get(id=group_id)
    member_id_object = Member.objects.get(id=member_id)
    
    return {
        "group_id_object":group_id_object,
        "member_id_object":member_id_object,
        "group_id":group_id,
        "member_id":member_id,
        "group_code":group_id_object.special_code,
        "group_name":group_id_object.name
        
    }

def member_save_to_group(custom_text,member_id):
    amount = custom_text[-1]
    
    my_object = get_group_member_id_from_text(custom_text,member_id)
    
    group_id_object = my_object["group_id_object"]
    member_id_object = my_object["member_id_object"]
    
    print(group_id_object.special_code)
    print("------")
    
    savings = Saving(member_id=member_id_object,group_id=group_id_object,amount=amount)
    savings.save()

    
    
    