from django.db import models

class artist(models.Model):
	artistName = models.CharField(primary_key = True, max_length = 20)
	artistBirthPlace = models.CharField(max_length = 20)
	artistAge = models.IntegerField(default = 0)
	artistStyle = models.CharField(max_length = 20)
	def __str__(self):
		return self.artistName

class customer(models.Model):
	customerName = models.CharField(primary_key = True, max_length = 20)
	customerAddress = models.CharField(max_length = 20)
	customerAmount = models.IntegerField(default = 0)
	customerLikeArtist = models.ForeignKey(artist, db_column = 'artistName')
	def __str__(self):
		return self.customerName

class artwork(models.Model):
	artworkTitle = models.CharField(primary_key = True, max_length = 20)
	artworkYear = models.IntegerField(default = 0)
	artworkPrice = models.IntegerField(default = 0)
	artworkArtist = models.ForeignKey(artist, db_column = 'artistName')
	def __str__(self):
		return self.artworkTitle
	
class group(models.Model):
	groupName = models.CharField(primary_key = True, max_length = 20)
	groupArtist = models.ForeignKey(artist, db_column = 'artistName', default = 'NULL')
	def __str__(self):
		return self.groupName
