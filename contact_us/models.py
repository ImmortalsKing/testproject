from django.db import models

# Create your models here.

class contactUs(models.Model):
    subject = models.CharField(max_length=200,verbose_name='عنوان')
    full_name = models.CharField(max_length=200,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='زمان ایجاد',auto_now_add=True)
    response = models.TextField(verbose_name='پاسخ تماس با ما',null=True,blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='دیده شده توسط ادمین')

    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='لیست تماس با ما'

    def __str__(self):
        return self.subject