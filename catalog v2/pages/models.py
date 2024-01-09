from django.db import models

# takımlar hakkında bilgileri içeren class
class Team(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

	
# maç ile ilgili bilgileri içersen class
class Match(models.Model):
	home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
	away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
	#maç başladı mı başlamadı mı kelimesi status
	status = models.CharField(max_length=20)
	score = models.CharField(max_length=10)
	match_date = models.DateTimeField()
	isPublished = models.BooleanField(default=True)

	def __str__(self):
		return self.home_team.name + ' ' + self.away_team.name
	

# Lig tablo modelleri
class LeagueTable(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	played_game = models.IntegerField(default=0)
	win = models.IntegerField(default=0)
	draws = models.IntegerField(default=0)
	loses = models.IntegerField(default=0)
	points = models.IntegerField(default=0)
	
	def update_table(self):
		self.played_game = self.team.home_matches.count() + self.team.away_matches.count()
		self.wins = self.team.home_matches.filter(status='Kazandı').count() + self.team.away_matches.filter(status='Kazandı').count()
		self.draws = self.team.home_matches.filter(status='Berabere').count() + self.team.away_matches.filter(status='Berabere').count()
		self.losses = self.team.home_matches.filter(status='Kaybetti').count() + self.team.away_matches.filter(status='Kaybetti').count()
		self.points = (self.wins * 3) + self.draws
		self.save()

	def __str__(self):
		return self.team.name
# üye-ol modelleri
