from django.db.models.signals import post_save
from django.dispatch import receiver

from customers.services import EmailService
from orders.models import Order

from .models import Robot


@receiver(post_save, sender=Robot)
def check_robot(sender, instance, **kwargs):
    orders = Order.objects.filter(robot_serial=instance.serial).distinct()
    if orders.exists():
        customers = list(orders.values_list("customer__email", flat=True))
        EmailService.send_email_to_customers(instance, customers)
