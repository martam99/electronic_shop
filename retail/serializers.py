from django.db.models import Count
from rest_framework import serializers
from SP.models import SP
from employee.permissions import UserPermissionsAll
from factory.models import Factory
from retail.models import Retail, Store, Contacts, Products


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class SPSerializer(serializers.ModelSerializer):
    class Meta:
        model = SP
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):
    store_count = serializers.SerializerMethodField()

    def get_store_count(self, obj):
        store_count = Store.objects.filter(company_name=obj).values('id').annotate(total=Count('company_name'))
        return store_count.count()

    class Meta:
        model = Retail
        fields = '__all__'
        permission_classes = [UserPermissionsAll]


class StoreSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(source='contacts_set', read_only=True, many=True)
    products = ProductsSerializer(source='products_set', read_only=True, many=True)

    class Meta:
        model = Store
        fields = ['company_name', 'store_name', 'contacts', 'products', 'debt_to_supplier', 'creating_date']
        permission_classes = [UserPermissionsAll]

