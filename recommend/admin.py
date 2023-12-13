from django.contrib import admin
from .models import Recommend, RecommendComment, RecommendLike, Category

admin.site.register(Recommend)
admin.site.register(RecommendComment)
admin.site.register(RecommendLike)
admin.site.register(Category)
