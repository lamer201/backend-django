from django.contrib import admin
from learn.models import Group, Product, Student, Learn

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'pub_date',
        'max_user',
        'min_user',
    )
    search_fields = ('name',)
    list_filter = ('pub_date',)
    filter_horizontal = ('users',)
    empty_value_display = '-пусто-'

    def get_users(self,obj):
        return [users.name for users in obj.users.all()]


@admin.register(Learn)
class LearnAdmin(admin.ModelAdmin):
    pass

