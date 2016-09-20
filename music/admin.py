from django.contrib import admin

from .models import Artist, Album, Song, Composer


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "solo_vs_band", 
        "wiki_url"
    )



class AlbumAdmin (admin.ModelAdmin):
    list_display = (
        "name", 
        "year", 
        "audio_format",
        "genre",
        "collection",
        "artist_names",
        "owned",
    )

    def artist_names(self, obj):
        names = [artist.name for artist in obj.artists.all()]
        return ", ".join(names)

    artist_names.short_description = 'Artist'



class SongAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "track_number",
        "track_length",
        "album",
        )


class ComposerAdmin (admin.ModelAdmin):
    list_display = (
        "name",
        "song_names",
    )

    def song_names(self,obj):
        names = [song.name for song in obj.songs.all()]
        return ", ".join(names)




admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Composer, ComposerAdmin)
















