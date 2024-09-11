from typing import Any
from django.contrib import admin, messages
from django.db.models.functions import Length
from django.db.models.query import QuerySet
from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = "Статус женщин"
    parameter_name = "status"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ("married", "Замужем"),
            ("single", "Не замужем"),
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == "married":
            return queryset.filter(husband__isnull=False)
        if self.value() == "signle":
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    # fields = ("title", "content", "slug", "cat",)
    # exclude = ("tags", "is_published", )
    # readonly_fields = ("slug", )
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    list_display = ("title", "time_create", "is_published", "cat", "brief_info")
    list_display_links = ("title",)
    ordering = ("-time_create", "title")
    list_editable = ("is_published",)
    list_per_page = 5
    actions = (
        "set_published",
        "set_draft",
    )
    search_fields = (
        "title",
        "cat__name",
    )
    list_filter = (
        MarriedFilter,
        "cat__name",
        "is_published",
    )

    @admin.display(description="Краткое описание", ordering=Length("content"))
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов"

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Опубликовано {count} записей")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(
            request, f"Снято с публикации {count} записей", messages.WARNING
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


# admin.site.register(Women)
