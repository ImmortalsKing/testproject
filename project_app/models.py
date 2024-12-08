from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='title')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/ نشده')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'{self.title} {self.url_title}'


class ProductBrand(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/ نشده')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    category = models.ManyToManyField(ProductCategory,
                                      related_name='product_categories',
                                      verbose_name='دسته بندی')
    brand = models.ForeignKey(ProductBrand,
                              on_delete=models.CASCADE,
                              related_name='product_brand',
                              verbose_name='برند',
                              null=True)
    short_description = models.CharField(max_length=350, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات کامل', db_index=True, null=True)
    slug = models.SlugField(default='', null=False, db_index=True, blank=True, unique=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/ نشده')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductTag(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان', db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='محصول',
                                related_name='product')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/ نشده')

    class Meta:
        verbose_name= 'تگ'
        verbose_name_plural = 'تگ ها'

    def __str__(self):
        return self.title