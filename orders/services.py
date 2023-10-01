from django.core.exceptions import ObjectDoesNotExist

from customers.models import Customer
from robots.models import Robot

from .models import Order


class OrderService:
    order = Order
    customer = Customer
    robot = Robot

    @classmethod
    def create(cls, data):
        customer, created = cls.customer.objects.get_or_create(email=data.get('email'))
        robot_serial = data.get('robot_serial')

        cls.order.objects.create(
            customer=customer, robot_serial=robot_serial
        )
        try:
            robot = cls.robot.objects.get(serial=robot_serial)
            message = f"Robot with serial {robot} is available for purchase"
        except ObjectDoesNotExist:
            message = (f"Sorry, the robot with serial {robot_serial} is not available now."
                       "We will email you as soon as this change.")

        return message
