#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.contrib.gis.db import models

class Line(models.Model):
  osm_id = models.IntegerField(primary_key=True)
  #access text,
  #"addr:housename" text,
  #"addr:housenumber" text,
  #"addr:interpolation" text,
  admin_level = models.TextField(null=True)
  #aerialway text,
  #aeroway text,
  #amenity text,
  #area text,
  #barrier text,
  bicycle = models.TextField(null=True)
  #brand text,
  bridge = models.TextField(null=True)
  boundary = models.TextField(null=True)
  #building text,
  #construction text,
  #covered text,
  #culvert text,
  #cutting text,
  #denomination text,
  #disused text,
  #embankment text,
  foot = models.TextField(null=True)
  #"generator:source" text,
  #harbour text,
  highway = models.TextField(null=True)
  #historic text,
  #horse text,
  #intermittent text,
  #junction text,
  #landuse text,
  #layer text,
  #leisure text,
  #lock text,
  #man_made text,
  #military text,
  #motorcar text,
  name = models.TextField(null=True, db_index=True)
  #"natural" text,
  #oneway text,
  #operator text,
  #population text,
  #power text,
  #power_source text,
  #place text,
  railway = models.TextField(null=True, db_index=True)
  ref = models.TextField(null=True, db_index=True)
  #religion text,
  route = models.TextField(null=True, db_index=True)
  #service text,
  #shop text,
  #sport text,
  surface = models.TextField(null=True)
  #toll text,
  #tourism text,
  #"tower:type" text,
  tracktype = models.TextField(null=True)
  #tunnel text,
  #water text,
  #waterway text,
  #wetland text,
  #width text,
  #wood text,
  z_order = models.IntegerField(null=True)
  #way_area real,
  way  = models.LineStringField(null=True, srid=900913)

  class Meta:
    db_table = "planet_osm_line"
    managed = False

  objects = models.GeoManager()


class Point(models.Model):
  osm_id = models.IntegerField(primary_key=True)
  name = models.TextField(null=True, db_index=True)
  railway = models.TextField(null=True, db_index=True)
  place = models.TextField(null=True, db_index=True)
  way  = models.PointField(null=True, srid=900913)

  class Meta:
    db_table = "planet_osm_point"
    managed = False

  objects = models.GeoManager()


class Polygon(models.Model):
  osm_id = models.IntegerField(primary_key=True)
  name = models.TextField(null=True, db_index=True)
  admin_level = models.TextField(null=True, db_index=True)
  boundary = models.TextField(null=True, db_index=True)
  way  = models.PolygonField(null=True, srid=900913)

  class Meta:
    db_table = "planet_osm_polygon"
    managed = False

  objects = models.GeoManager()
