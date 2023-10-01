import os

import pandas as pd
from django.conf import settings
from django.db.models import Count
from django.utils import timezone

from robots.models import Robot


class ExcelGenerator:
    model = Robot

    def generate_excel(self):
        current_date = timezone.now()
        file_path = self._get_file_path(current_date.date())

        start_date = current_date - timezone.timedelta(days=7)

        writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
        workbook = writer.book

        models = self.model.objects.values_list('model', flat=True).distinct()
        for model in models:
            robots = self.model.objects.filter(
                model=model,
                created__range=[start_date, current_date]).values(
                'model',
                'version',
            ).annotate(count=Count('version'))

            if robots.exists():
                df = pd.DataFrame(list(robots.values('model', 'version', 'count')))
                df = df.rename(columns={
                    'model': 'Модель',
                    'version': 'Версия',
                    'count': 'Количество за неделю'},
                )
                df.to_excel(writer, sheet_name=model, index=False)

                worksheet = writer.sheets[model]

                for i, column in enumerate(df.columns):
                    center_alignment = workbook.add_format({'align': 'center'})
                    column_width = max(df[column].astype(str).map(len).max(), len(column))
                    indent = 2
                    worksheet.set_column(i, i, column_width + indent, center_alignment)

        writer.close()
        return file_path

    @classmethod
    def _get_file_path(cls, current_date):
        folder_path = cls.__get_or_create_folder()
        file_name = f"robots_{current_date}.xlsx"
        return os.path.join(folder_path, file_name)

    @classmethod
    def __get_or_create_folder(cls):
        try:
            os.mkdir(f"{settings.MEDIA_ROOT}")
            os.mkdir(f"{settings.MEDIA_ROOT}/weekly_robots_stat")
        except FileExistsError:
            pass
        return os.path.join(settings.MEDIA_ROOT, "weekly_robots_stat")


excel_generator = ExcelGenerator()
