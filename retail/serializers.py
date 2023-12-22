from rest_framework import serializers

from retail.models import Retail, Store, Contacts, Products


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):
    store_count = serializers.SerializerMethodField()

    def get_store_count(self, obj):
        obj = Store.objects.all()
        return obj.count()

    class Meta:
        model = Retail
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(source='contacts_set', read_only=True, many=True)
    products = ProductsSerializer(source='products_set', read_only=True, many=True)

    class Meta:
        model = Store
        fields = ['company_name', 'store_name', 'contacts', 'products', 'debt_to_supplier', 'creating_date']
