from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.sub_category_set.update(is_active=self.is_active)

        for sub_category in self.sub_category_set.all():
            sub_category.product_set.update(is_active=self.is_active)
            for product in sub_category.product_set.all():
                product.productline_set.update(is_active=self.is_active)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product_set.update(is_active=self.is_active)

        for product in self.product_set.all():
            product.productline_set.update(is_active=self.is_active)

class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_countable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.productline_set.update(is_active=self.is_active)

class AttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.attribute.name} : {self.attribute_value}"

class ProductLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    attribute_values = models.ManyToManyField(AttributeValue, related_name="attribute_values")
    normal_price = models.DecimalField(decimal_places=2, max_digits=10)
    fawry_price = models.DecimalField(decimal_places=2, max_digits=10)
    stock_qty = models.IntegerField(default=0)
    min_stock_qty = models.IntegerField(default=1)
    is_active = models.BooleanField(default=False)
    deliver_date = models.IntegerField()
    admin_comment = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.stock_qty == 0 and self.product.is_countable:
            self.is_active = False
        super().save(*args, **kwargs)

    def values(self):
        attribute_values_str = ', '.join(str(attr_value.attribute_value) for attr_value in self.attribute_values.all())
        return attribute_values_str

    def __str__(self):
        attribute_values_str = ', '.join(str(attr_value) for attr_value in self.attribute_values.all())
        return f"{self.product.name} - {attribute_values_str}"

