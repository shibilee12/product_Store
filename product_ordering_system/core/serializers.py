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
        fields = ['id', 'items', 'total_price', 'created_at']
        read_only_fields = ['id', 'total_price', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user, total_price=0)

        total_price = 0
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']

            # Validate stock
            if product.stock < quantity:
                raise serializers.ValidationError({
                    "detail": f"Insufficient stock for {product.name}. Only {product.stock} left."
                })

            # Deduct stock
            product.stock -= quantity
            product.save()

            # Create order item
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

            # Update total
            total_price += product.price * quantity

        order.total_price = total_price
        order.save()
        return order
