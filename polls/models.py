# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appearances(models.Model):
    year_id = models.SmallIntegerField(db_column='year_id', primary_key=True)
    team_id = models.CharField(db_column='team_id', max_length=3)
    league_id = models.CharField(db_column='league_id', max_length=2, blank=True, null=True)
    player_id = models.CharField(db_column='player_id', max_length=9)
    g_total = models.SmallIntegerField(db_column='G_total', blank=True, null=True)  # Field name made lowercase.
    gs = models.SmallIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.SmallIntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    g_defense = models.SmallIntegerField(db_column='G_defense', blank=True, null=True)  # Field name made lowercase.
    g_p = models.SmallIntegerField(db_column='G_p', blank=True, null=True)  # Field name made lowercase.
    g_c = models.SmallIntegerField(db_column='G_c', blank=True, null=True)  # Field name made lowercase.
    g_1b = models.SmallIntegerField(db_column='G_1b', blank=True, null=True)  # Field name made lowercase.
    g_2b = models.SmallIntegerField(db_column='G_2b', blank=True, null=True)  # Field name made lowercase.
    g_3b = models.SmallIntegerField(db_column='G_3b', blank=True, null=True)  # Field name made lowercase.
    g_ss = models.SmallIntegerField(db_column='G_ss', blank=True, null=True)  # Field name made lowercase.
    g_lf = models.SmallIntegerField(db_column='G_lf', blank=True, null=True)  # Field name made lowercase.
    g_cf = models.SmallIntegerField(db_column='G_cf', blank=True, null=True)  # Field name made lowercase.
    g_rf = models.SmallIntegerField(db_column='G_rf', blank=True, null=True)  # Field name made lowercase.
    g_of = models.SmallIntegerField(db_column='G_of', blank=True, null=True)  # Field name made lowercase.
    g_dh = models.SmallIntegerField(db_column='G_dh', blank=True, null=True)  # Field name made lowercase.
    g_ph = models.SmallIntegerField(db_column='G_ph', blank=True, null=True)  # Field name made lowercase.
    g_pr = models.SmallIntegerField(db_column='G_pr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appearances'
        unique_together = (('year_id', 'team_id', 'player_id'),)


class Batting(models.Model):
    player_id = models.CharField(db_column='player_id', max_length=9, blank=True, null=True)
    year_id = models.SmallIntegerField(db_column='year_id', blank=True, null=True)
    stint = models.SmallIntegerField(db_column='stint', blank=True, null=True)
    team_id = models.CharField(db_column='team_id', max_length=3, blank=True, null=True)
    league_id = models.CharField(db_column='league_id', max_length=2, blank=True, null=True)
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    at_bats = models.SmallIntegerField(db_column='at_bats', blank=True, null=True)
    runs = models.SmallIntegerField(db_column='runs', blank=True, null=True)
    hits = models.SmallIntegerField(db_column='hits', blank=True, null=True)
    number_2b = models.SmallIntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.SmallIntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.SmallIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.SmallIntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.SmallIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.SmallIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.SmallIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.SmallIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.SmallIntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.SmallIntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.SmallIntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.SmallIntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.SmallIntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'batting'
        unique_together = (('player_id', 'year_id', 'stint'),)


class People(models.Model):
    player_id = models.CharField(db_column='player_id', primary_key=True, max_length=255)
    birth_country = models.CharField(db_column='birth_country', max_length=255, blank=True, null=True)
    birth_state = models.CharField(db_column='birth_state', max_length=255, blank=True, null=True)
    birth_city = models.CharField(db_column='birth_city', max_length=255, blank=True, null=True)
    name_first = models.CharField(db_column='name_first', max_length=255, blank=True, null=True)
    name_last = models.CharField(db_column='name_last', max_length=255, blank=True, null=True)
    weight = models.IntegerField(db_column='weight', blank=True, null=True)
    height = models.IntegerField(db_column='height', blank=True, null=True)
    bats = models.CharField(db_column='bats', max_length=255, blank=True, null=True)
    throws = models.CharField(db_column='throws', max_length=255, blank=True, null=True)
    debut = models.CharField(db_column='debut', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people'


class Pitching(models.Model):
    player_id = models.CharField(db_column='player_id', max_length=9, blank=True, null=True)
    year_id = models.SmallIntegerField(db_column='year_id', blank=True, null=True)
    stint = models.SmallIntegerField(db_column='stint', blank=True, null=True)
    team_id = models.CharField(db_column='team_id', max_length=3, blank=True, null=True)
    league_id = models.CharField(db_column='league_id', max_length=2, blank=True, null=True)
    w = models.SmallIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.SmallIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.SmallIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    shutouts = models.SmallIntegerField(db_column='shutouts', blank=True, null=True)
    saves = models.SmallIntegerField(db_column='saves', blank=True, null=True)
    outs_pitched = models.IntegerField(db_column='outs_pitched', blank=True, null=True)
    h = models.SmallIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.SmallIntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.SmallIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.SmallIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    strikeouts = models.SmallIntegerField(db_column='strikeouts', blank=True, null=True)
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.SmallIntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.SmallIntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.SmallIntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    r = models.SmallIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pitching'
        unique_together = (('player_id', 'year_id', 'stint'),)


class Teams(models.Model):
    year_id = models.SmallIntegerField(db_column='year_id', primary_key=True)
    league_id = models.CharField(db_column='league_id', max_length=2, blank=True, null=True)
    team_id = models.CharField(db_column='team_id', max_length=3)
    franchise_id = models.CharField(db_column='franchise_id', max_length=3, blank=True, null=True)
    rank = models.SmallIntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    home_games = models.SmallIntegerField(db_column='home_games', blank=True, null=True)
    w = models.SmallIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.SmallIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    r = models.SmallIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    at_bats = models.SmallIntegerField(db_column='at_bats', blank=True, null=True)
    h = models.SmallIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.SmallIntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.SmallIntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.SmallIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.SmallIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.SmallIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    sb = models.SmallIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.SmallIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    ra = models.SmallIntegerField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=50, blank=True, null=True)
    park = models.CharField(db_column='park', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'
        unique_together = (('year_id', 'team_id'),)
