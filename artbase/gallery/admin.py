from django.contrib import admin

from .models import artist
class artistAdmin(admin.ModelAdmin):
	list_display = ('artistName', 'artistAge', 'artistBirthPlace', 'artistStyle')
	list_filter = ['artistName', 'artistAge', 'artistBirthPlace', 'artistStyle']
	search_fields = ['artistName', 'artistAge', 'artistBirthPlace', 'artistStyle'] 
admin.site.register(artist, artistAdmin)


from .models import customer
class customerAdmin(admin.ModelAdmin):
	list_display = ('customerName', 'customerAddress', 'customerAmount', 'customerLikeArtist')
	list_filter = ['customerName', 'customerAddress', 'customerAmount', 'customerLikeArtist']
	search_fields = ['customerName', 'customerAddress', 'customerAmount', 'customerLikeArtist']
admin.site.register(customer, customerAdmin)


from .models import artwork
class artworkAdmin(admin.ModelAdmin):
	list_display = ('artworkTitle', 'artworkYear', 'artworkYear', 'artworkPrice', 'artworkArtist')
	list_filter = ['artworkTitle', 'artworkYear', 'artworkYear', 'artworkPrice', 'artworkArtist']
	search_fields = ['artworkTitle', 'artworkYear', 'artworkYear', 'artworkPrice', 'artworkArtist']
admin.site.register(artwork, artworkAdmin)


from .models import group
class groupAdmin(admin.ModelAdmin):
	list_display = ('groupName', 'groupArtist')
	list_filter = ['groupName', 'groupArtist']
	search_fields = ['groupName', 'groupArtist']
admin.site.register(group, groupAdmin)

