from django.db import models

# takımlar hakkında bilgileri içeren class
class Team(models.Model):
	name = models.CharField(max_length=50)

	
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
	

# üye-ol modelleri
