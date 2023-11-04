from django.contrib import admin
from .models import Expense,Category


#自訂管理介面顯示
class ExpenseAdmin(admin.ModelAdmin):  
    list_display = ('amount', 'description', 'owner', 'category', 'date',)
    search_fields = ('description', 'category', 'date',)

    list_per_page = 5   #顯示5列

admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Category)