from django.db import models

class Country(models.Model):
    name        = models.CharField(max_length=50, db_index=True)
    is_active   = models.BooleanField(default=True, verbose_name='Active/Inactive')
    is_deleted  = models.BooleanField(default=False, verbose_name='Soft Delete')
    created_at  = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'country'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class State(models.Model):
    name        = models.CharField(max_length=50, db_index=True)
    country     = models.ForeignKey('geography.Country', on_delete=models.CASCADE)
    is_active   = models.BooleanField(default=True, verbose_name='Active/Inactive')
    is_deleted  = models.BooleanField(default=False, verbose_name='Soft Delete')
    created_at  = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'state'
        verbose_name = 'State'
        verbose_name_plural = 'States'


class City(models.Model):
    name        = models.CharField(max_length=50, db_index=True)
    country     = models.ForeignKey('geography.Country', on_delete=models.CASCADE)
    state       = models.ForeignKey('geography.State', on_delete=models.CASCADE)
    is_active   = models.BooleanField(default=True, verbose_name='Active/Inactive')
    is_deleted  = models.BooleanField(default=False, verbose_name='Soft Delete')
    created_at  = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'