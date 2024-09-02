# vim: set fileencoding=utf-8 :
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

import accounts.models as models


class JobTitleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("id", "name")
    search_fields = ("name",)

class CountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("id", "name")
    search_fields = ("name",)


class GovernorateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "name", "country")
    list_filter = ("country", "id", "name")
    search_fields = ("name",)


class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "name", "governorate")
    list_filter = ("governorate", "id", "name")
    search_fields = ("name",)


class UserProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "job_title",
        "city",
        "date_of_birth",
        "start",
        "address",
        "gender",
        "salary",
    )
    list_filter = (
        "user",
        "job_title",
        "city",
        "date_of_birth",
        "start",
        "id",
        "address",
        "gender",
        "salary",
    )


class SalaryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "user_profile", "amount", "start", "end")
    list_filter = ("id", "user_profile", "amount", "start", "end")


class DeductionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "user_profile", "name", "amount")
    list_filter = ("id", "user_profile", "name", "amount")

class JobTitleHistoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "job_title", "user_profile", "start", "end")
    list_filter = (
        "job_title",
        "user_profile",
        "start",
        "end",
        "id",
        "user_profile__user__is_active",
    )
    search_fields = (
        "job_title__name",
        "user_profile__user__username",
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.JobTitle, JobTitleAdmin)
_register(models.Country, CountryAdmin)
_register(models.Governorate, GovernorateAdmin)
_register(models.City, CityAdmin)
_register(models.UserProfile, UserProfileAdmin)
_register(models.JobTitleHistory, JobTitleHistoryAdmin)
_register(models.SalaryHistory, SalaryAdmin)
_register(models.Deduction, DeductionAdmin)
