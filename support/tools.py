from django.utils import timezone

from orders.models import Order


def get_order_details(order_id):
    try:
        order = Order.objects.get(id=order_id)
        return{
            "order_id": order.id,
            "product_name": order.product_name,
            "amount": str(order.amount),
            "status": order.status,
            "carrier": order.carrier,
            "tracking_number": order.tracking_number,
            "delivery_address": order.delivery_address,
            "ordered_on": order.created_at.strftime("%Y-%m-%d %H:%M:%S"), # 25 may 2026
            "day_since_order": (timezone.now() - order.created_at).days, # 20
        }
    except Order.DoesNotExist:
        return {
            "error": f"Order {order_id} not found"
        }
    