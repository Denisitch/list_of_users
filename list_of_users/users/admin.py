from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    """Пользователи"""

    list_display = (
        "first_name",
        "last_name",
        "patronymic",
        "date_of_birth",
        "phone_number",
        "status",
        "get_photo",
    )
    list_editable = ("status",)
    list_filter = (
        "first_name",
        "last_name",
        "patronymic",
        "date_of_birth",
        "phone_number",
    )
    readonly_fields = ("get_photo",)

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="50"')

    get_photo.short_description = "Фото"
