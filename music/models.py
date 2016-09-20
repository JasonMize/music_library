from django.db import models
from django.core.urlresolvers import reverse



class Artist (models.Model):
    #artist name
    name = models.CharField(max_length = 40)
    
    #link to artist wiki
    wiki_url = models.URLField(max_length=200, blank=True)
    
    #is artist solo or with a group
    SOLO = "Solo Artist"
    BAND = "Band"
    
    SOLO_VS_BAND_CHOICES = (
        (SOLO, "Solo Artist"),
        (BAND, "Band"),
    )
    solo_vs_band = models.CharField(max_length = 40, 
        choices = SOLO_VS_BAND_CHOICES, 
        default = SOLO,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ("artists:detail", kwargs={"id":self.pk})


class Album (models.Model):
    #album name
    name = models.CharField(max_length = 100)

    #what format is the album?
    VINYL = "Vinyl"
    CD = "Compact Disc"
    DIGITAL = "Digital"
    PHONOGRAPH = "Phonograph Cylinder"
    CASSETTE = "Compact Cassette"
    
    AUDIO_FORMAT = (
    (VINYL, "Vinyl"),
    (CD, "Compact Disc"),
    (DIGITAL, "Digital"),
    (PHONOGRAPH, "Phonograph Cylinder"),        
    )
    audio_format = models.CharField(max_length = 40,
        choices = AUDIO_FORMAT,
        default = DIGITAL,
    )

    #what year was the album released
    year = models.IntegerField ()

    #what genre
    ROCK = "Rock 'n Roll"
    PUNK = "Punk"

    GENRE = (
        (ROCK, "Rock 'n Roll"),
        (PUNK, "Punk"),
    )
    genre = models.CharField (max_length = 40, 
        choices = GENRE,
        default = ROCK)

    #is the album a collection?
    collection = models.BooleanField (default = False)

    #album art
    # cover_art = models.ImageField ()

    #link between Album and Artist models/classes
    artists = models.ManyToManyField("Artist")

    #do I own this album?
    owned = models.BooleanField(default = False)

    def __str__(self):
        return self.name



class Song (models.Model):
    #song name
    name = models.CharField(max_length = 100)

    #track number
    track_number = models.IntegerField()

    #track length
    track_length = models.CharField(max_length = 20)

    #link from Song to Album models/classes
    album = models.ForeignKey("Album")

    def __str__(self):
        return self.name



class Composer (models.Model):
    #track composer
    name = models.CharField(max_length = 40)

    #link between Composer and Song models/classes
    songs = models.ManyToManyField("Song")

    def __str__(self):
        return self.name







