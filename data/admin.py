from django.contrib import admin
from .models import TwitterUser, Tweet


@admin.register(TwitterUser)
class ProductAdmin(admin.ModelAdmin):
		list_display = (
			'username',
			'id',
		)

@admin.register(Tweet)
class ProductAdmin(admin.ModelAdmin):
		list_display = (
			'username',
			'id'
		)
		list_select_related = (
            'username',
        )