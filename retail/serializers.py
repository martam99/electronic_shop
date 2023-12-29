from django.db.models import Count
from rest_framework import serializers
from SP.models import SP
from factory.models import Factory
from retail.models import Retail, Store, Contacts, Products
from django_filters import rest_framework as filters


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


class FilterCountryListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(country=data)
        return super(FilterCountryListSerializer, self).to_representation(data)


class StoreSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(source='contacts_set', read_only=True, many=True)
    products = ProductsSerializer(source='products_set', read_only=True, many=True)

    class Meta:
        model = Store
        fields = ['company_name', 'store_name', 'contacts', 'products', 'debt_to_supplier', 'creating_date']
