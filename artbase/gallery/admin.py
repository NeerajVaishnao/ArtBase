from django.contrib import admin

from .models import artist
class artistAdmin(admin.ModelAdmin):
	list_display = ('artistName', 'artistAge', 'artistBirthPlace','artistStyle')
	list_filter = ['artistName', 'artistAge', 'artistBirthPlace','artistStyle']
	search_fields = ['artistName', 'artistAge', 'artistBirthPlace','artistStyle'] 
admin.site.register(artist, artistAdmin)


from .models import customer
class customerAdmin(admin.ModelAdmin):
	list_display = ('customerId', 'customerName', 'customerAddress', 'customerAmount')
	list_filter = ['customerId', 'customerName', 'customerAddress', 'customerAmount']
	search_fields = ['customerId', 'customerName', 'customerAddress', 'customerAmount']
admin.site.register(customer, customerAdmin)


from .models import artwork
class artworkAdmin(admin.ModelAdmin):
	list_display = ('artworkTitle', 'artworkYear', 'artworkYear', 'artworkPrice', 'artworkArtist')
	list_filter = ['artworkTitle', 'artworkYear', 'artworkYear', 'artworkPrice', 'artworkArtist']
	search_fields = ['artworkTitle', 'artworkYear', 'artworkYear', 'artworkPrice', 'artworkArtist']
admin.site.register(artwork, artworkAdmin)


from .models import group
class groupAdmin(admin.ModelAdmin):
	list_filter = ['groupName']
	search_fields = ['groupName']
admin.site.register(group, groupAdmin)

from .models import likeGroup
class likeGroupAdmin(admin.ModelAdmin):
	list_display = ('likeGroupCustomerId', 'likeGroupName')
	list_filter = ['likeGroupCustomerId', 'likeGroupName']
	search_fields = ['likeGroupCustomerId', 'likeGroupName']
admin.site.register(likeGroup, likeGroupAdmin)

from .models import likeArtist
class likeArtistAdmin(admin.ModelAdmin):
	list_display = ('likeArtistCustomerId', 'likeArtistArtistName')
	list_filter = ['likeArtistCustomerId', 'likeArtistArtistName']
	search_fields = ['likeArtistCustomerId', 'likeArtistArtistName']
admin.site.register(likeArtist, likeArtistAdmin)

from .models import classifiedInto
class classifiedIntoAdmin(admin.ModelAdmin):
	list_display = ('classifiedIntoGroupName', 'classifiedIntoArtworkTitle')
	list_filter = ['classifiedIntoGroupName', 'classifiedIntoArtworkTitle']
	search_fields = ['classifiedIntoGroupName', 'classifiedIntoArtworkTitle']
admin.site.register(classifiedInto, classifiedIntoAdmin)
