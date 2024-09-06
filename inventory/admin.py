from django.contrib import admin

import inventory.models as models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'is_active')
    list_filter = ('is_active', 'id', 'name')
    search_fields = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'category', 'name', 'is_active')
    list_filter = ('category', 'is_active', 'id', 'name')
    search_fields = ('name',)


class AttributeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description')
    list_filter = ('id', 'name', 'description')
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'sub_category',
        'name',
        'description',
        'is_active',
        'is_countable',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'sub_category',
        'is_active',
        'is_countable',
        'created_at',
        'updated_at',
        'id',
        'name',
        'description',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class AttributeValueAdmin(admin.ModelAdmin):

    list_display = ('id', 'product', 'attribute', 'attribute_value')
    list_filter = ('product', 'attribute', 'id', 'attribute_value')


class ProductLineAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product',
        'normal_price',
        'fawry_price',
        'stock_qty',
        'min_stock_qty',
        'is_active',
        'deliver_date',
        'admin_comment',
    )
    list_filter = (
        'product',
        'is_active',
        'id',
        'normal_price',
        'fawry_price',
        'stock_qty',
        'min_stock_qty',
        'deliver_date',
        'admin_comment',
    )
    raw_id_fields = ('attribute_values',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.SubCategory, SubCategoryAdmin)
_register(models.Attribute, AttributeAdmin)
_register(models.Product, ProductAdmin)
_register(models.AttributeValue, AttributeValueAdmin)
_register(models.ProductLine, ProductLineAdmin)
