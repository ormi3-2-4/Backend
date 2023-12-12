from django.contrib import admin
from .models import Community, CommunityComment, CommunityLike

admin.site.register(Community)
admin.site.register(CommunityComment)
admin.site.register(CommunityLike)
