from .models import *
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ('id',"first_name","last_name",)
        

class GroupMembersSerializer(serializers.ModelSerializer):
    member_name = serializers.ReadOnlyField(
        source='member_id.name')
    group_name = serializers.ReadOnlyField(
        source='group_id.name')
    group_code = serializers.ReadOnlyField(
        source='group_id.special_code')
    
    class Meta:
        model = GroupMembers
        fields = ('id',"member_id","group_id","group_name","member_name","group_code",)
        

class SavingsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Saving
        fields = ('id',"member_id","amount",)
    
    
class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id',"vendor_id","name","category","retail_price","wholesale_price")


class VendorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = ('id',"business_name")


class LoansSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loan
        fields = ('id',"group_id","group_member_id","amount","amount_due","duration_days","penalty_rate","interest","loan_type","due_date","approved_date","status")
    
    