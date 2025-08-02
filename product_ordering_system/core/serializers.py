# core/serializers.py
from rest_framework import serializers
from .models import CustomUser, Product, OrderItem, Order
from django.contrib.auth import authenticate

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError("Invalid credentials")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'created_at', 'items']
        read_only_fields = ['id', 'total_price', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        items_data = validated_data.pop('items')

        total_price = 0
        order_items = []

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']

            # Stock validation
            if product.stock_quantity < quantity:
                raise serializers.ValidationError(
                    f"Insufficient stock for product '{product.name}'"
                )

            product.stock_quantity -= quantity
            product.save()

            item_total = product.price * quantity
            total_price += item_total

            order_items.append(OrderItem(product=product, quantity=quantity))

        order = Order.objects.create(user=user, total_price=total_price)

        for item in order_items:
            item.order = order
            item.save()

        return order

       
