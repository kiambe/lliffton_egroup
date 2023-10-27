from members.models import *


def get_member_details_from_phone(phone_number="254791836987"):
    try:
        member = Member.objects.get(primary_phone_number=phone_number)
        print(member)
        
        return member
    except:
        print("user not found")

def get_member_groups(member_id):
    try:
        groups = GroupMembers.objects.get(member_id=id)
        print(groups)
        return groups
    except:
        print("user not found")