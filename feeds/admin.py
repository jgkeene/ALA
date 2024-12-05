from django.contrib import admin
from .models import Reddit, Slashdot, Hackernews


admin.site.register(Reddit)
admin.site.register(Slashdot)
admin.site.register(Hackernews)


