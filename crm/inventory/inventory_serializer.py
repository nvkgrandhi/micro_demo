from rest_framework import serializers
from inventory.models import Inventory, Sales


class InventorySalesSerializer(serializers.ModelSerializer):
    sales_data = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Inventory
        fields = ('item', 'quantity_left', 'quantity_sold', 'price', 'sales_details', 'sales_data')