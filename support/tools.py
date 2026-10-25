from django.utils import timezone
from .tracking_data import DELIVERY_DATA
from orders.models import Order,RefundRequest


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
    
    
def get_refund_history(order_id):
    refunds = RefundRequest.objects.filter(order_id=order_id).order_by('-created_at')
    history = []
    for refund in refunds:
        history.append({
            "refund_id": refund.order.id,
            "product":refund.order.product_name,
            "reason": refund.reason,
            "status": refund.status,
            "requested_on": refund.created_at.strftime("%d %b %Y %H:%M:%S"),  # 25 May 2026 14:30:00
        })
    return{
        "total_refund_requests": len(history),
        "history": history
    }
    

def check_delivery_status(tracking_number, carrier):
    default_response = {
        "status": "Unknown",
        "last_location": "Tracking info unavailable",
        "last_update": "N/A",
        "estimated_delivery": "Contact carrier directly",
        "delay_reason": "No updates from carrier",
    }
    result = DELIVERY_DATA.get(tracking_number, default_response)
    result["tracking_number"] = tracking_number
    result["carrier"] = carrier
    return result