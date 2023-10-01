from django.http import HttpResponse, JsonResponse
from django.views import View

from services import validate_json

from .forms import RobotForm
from .services import excel_generator


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


class DownloadExcelView(View):
    def get(self, request):
        excel_file = excel_generator.generate_excel()

        with open(excel_file, 'rb') as file:
            response = HttpResponse(
                file.read(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        filename = excel_file.split('/')[-1]
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response
