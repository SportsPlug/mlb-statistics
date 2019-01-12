from django.contrib import admin
from polls.models import People, Pitching, Batting, Teams, Appearances
# Register your models here.

admin.site.register(People)
admin.site.register(Pitching)
admin.site.register(Batting)
admin.site.register(Teams)
admin.site.register(Appearances)