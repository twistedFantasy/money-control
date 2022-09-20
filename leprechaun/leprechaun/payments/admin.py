from django.contrib import admin

from leprechaun.payments.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    ...
