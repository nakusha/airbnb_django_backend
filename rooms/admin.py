from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, object):
        return object.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rule"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    # ordering = ("name", "price")
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    list_filter = (
        "host__superhost",
        "city",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "country",
    )
    raw_id_fields = ("host",)
    search_fields = ("city", "^host__username")
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )

    def save_model(self, request, obj, form, change):
        print(obj, change)
        return super().save_model(request, obj, form, change)

    # self=admin class/ object=선택된 줄
    def count_amenities(self, object):
        return object.amenities.count()

    def count_photos(self, object):
        return object.photos.count()

    # 이름 수정
    count_amenities.short_description = "Count Amenities"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" width="50"/>')

    get_thumbnail.short_description = "thumbNail"
