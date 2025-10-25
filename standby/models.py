# standby/models.py
from django.db import models

class StandbyAssignment(models.Model):
    date = models.DateField("التاريخ")
    period_index = models.PositiveSmallIntegerField("رقم الحصة")
    class_name = models.CharField("الفصل", max_length=50)
    teacher_name = models.CharField("اسم المعلّم", max_length=100)
    notes = models.CharField("ملاحظة", max_length=200, blank=True)

    class Meta:
        verbose_name = "تكليف انتظار"
        verbose_name_plural = "تكليفات انتظار"
        ordering = ("-date", "period_index")

    def __str__(self) -> str:
        return f"{self.date} — حصة {self.period_index} — {self.class_name} — {self.teacher_name}"
