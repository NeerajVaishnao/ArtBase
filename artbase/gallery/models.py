from django.db import models

class artist(models.Model):
	artistName = models.CharField(primary_key = True, max_length = 20)
	artistBirthPlace = models.CharField(max_length = 20)
	artistAge = models.IntegerField(default = 0)
	artistStyle = models.CharField(max_length = 20, default = 'NULL')
	def __str__(self):
		return self.artistName

class customer(models.Model):
	customerId = models.IntegerField(primary_key = True)
	customerName = models.CharField(max_length = 20)
	customerAddress = models.CharField(max_length = 20)
	customerAmount = models.IntegerField(default = 0)
	def __str__(self):
		return self.customersName

class artwork(models.Model):
	artworkTitle = models.CharField(primary_key = True, max_length = 20)
	artworkYear = models.IntegerField(default = 0)
	artworkPrice = models.IntegerField(default = 0)
	artworkArtist = models.ForeignKey(artist, db_column = 'artistName')
	artworkType = models.CharField(default = 'NULL', max_length = 20)
	def __str__(self):
		return self.artworkTitle
	
class group(models.Model):
	groupName = models.CharField(primary_key = True, max_length = 20)
	def __str__(self):
		return self.groupName

class likeGroup(models.Model):
	likeGroupCustomerId = models.ForeignKey(customer, db_column = 'customersId')
	likeGroupName = models.CharField(default = 'NULL', max_length = 20)
	def __str__(self):
		return self.likeGroupName

class classifiedInto(models.Model):
	classifiedIntoGroupName = models.ForeignKey(group, db_column = 'groupName')
	classifiedIntoArtworkTitle = models.ForeignKey(artwork, db_column = 'artworkTitle')
	def __str__(self):
		return self.classifiedGroupName

class likeArtist(models.Model):
	likeArtistCustomerId = models.ForeignKey(customer, db_column = 'customerId')
	likeArtistArtistName = models.ForeignKey(artist, db_column = 'artistName')
	def __str__(self):
		return self.likeArtistArtistName


