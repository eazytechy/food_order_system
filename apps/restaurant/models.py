from django.db import models

class Restaurant(models.Model):

    class Status(models.IntegerChoices):
        PENDING        = 1, 'Pending'
        SUCCESS        = 2, 'Success'
        FAILED         = 3, 'Failed'

    name        = models.CharField(max_length=100, db_index=True)
    country     = models.ForeignKey('geography.Country', on_delete=models.CASCADE)
    state       = models.ForeignKey('geography.State', on_delete=models.CASCADE) 
    city        = models.ForeignKey('geography.City', on_delete=models.CASCADE) 
    status      = models.IntegerField(choices=Status.choices)
    is_deleted  = models.BooleanField(default=False, verbose_name='Soft Delete')
    created_at  = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'restaurant'
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


class RestaurantImage(models.Model):

    restaurant      = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    name            = models.CharField(max_length=100, db_index=True)
    image           = models.ImageField(upload_to ='images/rest-images')
    is_active       = models.BooleanField(default=True)
    is_deleted      = models.BooleanField(default=False, verbose_name='Soft Delete')
    created_at      = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'restaurant_image'
        verbose_name = 'Restaurant Image'
        verbose_name_plural = 'Restaurant Images'


class RestaurantItem(models.Model):

    class FoodCategory(models.IntegerChoices):
        VEG         = 1, 'Veg'
        NON_VEG     = 2, 'Non Veg'
        EGG         = 3, 'Egg'


    restaurant      = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    name            = models.CharField(max_length=100, db_index=True)
    description     = models.CharField(max_length=100, db_index=True)
    food_category   = models.IntegerField(choices=FoodCategory.choices)
    image           = models.ImageField(upload_to ='images/item-images')
    rating          = models.DecimalField(default=0)
    price           = models.DecimalField(default=0)
    discounted_price = models.DecimalField(default=0)
    is_active       = models.BooleanField(default=True)
    is_deleted      = models.BooleanField(default=False, verbose_name='Soft Delete')
    created_at      = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'restaurant_image'
        verbose_name = 'Restaurant Image'
        verbose_name_plural = 'Restaurant Images'