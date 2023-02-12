# -*- coding: utf-8 -*-
from codecs import latin_1_decode
import logging
import math
from sensecam_control import vapix_control
##############################################################################
# Import the packages necessary for finding coordinates and making
# coordinate transformations

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_body


LAT = 
LON = 
UTC_OFFSET = 4
AXIS_IP = "192.168.1.74"
AXIS_USER = "ADMIN"
AXIS_PASSWORD = "PASSWORD"

#vega = SkyCoord.from_name('altair')
#vega = SkyCoord.from_name('deneb')
vega = SkyCoord.from_name('vega')

##############################################################################
# Use `astropy.coordinates.EarthLocation` to provide the location of Bear
# Mountain and set the time to 11pm EDT on 2012 July 12:

homebase = EarthLocation(lat= LAT*u.deg, lon=LON*u.deg, height=23*u.m)
utcoffset = UTC_OFFSET*u.hour  # Eastern Daylight Time
time = Time.now()

##############################################################################
# `astropy.coordinates.EarthLocation.get_site_names` and
# `~astropy.coordinates.EarthLocation.get_site_names` can be used to get
# locations of major observatories.
#
# Use `astropy.coordinates` to find the Alt, Az coordinates of vega at as
# observed from Bear Mountain at 11pm on 2012 July 12.

vega_altaz = vega.transform_to(AltAz(obstime=time,location=homebase))
print(f"Vega's Altitude = {float(vega_altaz.alt.value)} Azimuth = {float(vega_altaz.az.value)}")


camera = vapix_control.CameraControl(AXIS_IP, AXIS_USER, AXIS_PASSWORD)
camera.absolute_move(float(vega_altaz.az.value), float(vega_altaz.alt.value))

#frame_now = AltAz(obstime=time, location=homebase)
#saturn = get_body("jupiter", time)
#saturn_here_now = saturn.transform_to(frame_now)
#print(f"Jupiter's Altitude = {saturn_here_now.alt} Azimuth = {saturn_here_now.az}")