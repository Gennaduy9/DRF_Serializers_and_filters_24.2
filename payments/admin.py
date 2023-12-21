from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pay_date', 'pay_course', 'pay_lesson', 'money', 'pay_method',)