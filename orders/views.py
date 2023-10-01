from django.http import JsonResponse
from django.views import View

from services import validate_json

from .forms import OrderForm
from .services import OrderService


class OrderRobotView(View):
    form_class = OrderForm

    def post(self, request):
        valid_json_data = validate_json(request.body)
        form = self.form_class(valid_json_data)

        if form.is_valid():
            order_data = OrderService.create(form.cleaned_data)

            return JsonResponse({"message": order_data}, status=200)

        return JsonResponse({"error": form.errors}, status=400)
