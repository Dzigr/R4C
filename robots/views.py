from django.http import JsonResponse
from django.views import View

from services import validate_json

from .forms import RobotForm


class CreateRobotView(View):
    form_class = RobotForm

    def post(self, request):
        valid_json_data = validate_json(request.body)
        form = self.form_class(data=valid_json_data)

        if form.is_valid():
            robot_instance = form.save()
            robot_instance.serial = f"{robot_instance.model}-{robot_instance.version}"

            robot_instance.save()
            return JsonResponse(
                {"message": f"Robot with serial {robot_instance} created successfully"}
            )

        return JsonResponse(data={"error": form.errors}, status=400)
