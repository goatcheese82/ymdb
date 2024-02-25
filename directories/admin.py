from django.contrib import admin

# Register your models here.
from .models import Quorum, Stake, Ward, User, Family, Calling, Event, Assignment


class QuorumAdmin(admin.ModelAdmin):
   fields = ["quorum_name", "quorum_min_date", "quorum_max_date"]
   list_display = ["quorum_name", "quorum_min_date"]
   list_filter = ["quorum_min_date"]
   search_fields = ["quorum_name"]

admin.site.register(Quorum, QuorumAdmin)
admin.site.register(Stake)
admin.site.register(Ward)
admin.site.register(User)
admin.site.register(Family)
admin.site.register(Calling)

class EventAdmin(admin.ModelAdmin):
   fieldsets = [
      (None, {"fields": ["title"]}),
      ("Event Info:", {"fields": ["description", "date", "time", "location"]}),
      ("Attending:", {"fields": ["attendees"]})
   ]
admin.site.register(Event, EventAdmin)
admin.site.register(Assignment)
