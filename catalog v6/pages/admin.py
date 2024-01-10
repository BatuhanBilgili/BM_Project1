from django.contrib import admin
from .models import *

class MatchesAdmin(admin.ModelAdmin):
	list_display = ('home_team', 'away_team', 'match_date', 'isPublished')
	list_display_links = ('home_team', 'away_team')
	list_filter = ('match_date',)
	# kayıtların yayında olup olmadığı belirten ifade 1-> yayında 0->değil
	list_editable = ('isPublished',)
	# her sayfada kaç kayıt gösterileceği
	list_per_page = 10

class LeagueTableAdmin(admin.ModelAdmin):
	list_display = ('team', 'played_game', 'points')
	list_per_page = 10

# Register your models here.
admin.site.register(Team)
admin.site.register(Match, MatchesAdmin)
admin.site.register(LeagueTable, LeagueTableAdmin)