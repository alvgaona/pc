# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:28:27 2022

@author: Tiziano Levi Martin Bernal
"""

def match_duration (hours, minutes, seconds):
    """
    Parameters
    ----------
    hours : horas jugadas en el partido de tenis
    minutes : minutos jugados
    seconds : segundos jugados
    
    Returns
    -------
    Suma de las variables hours_secs y mins_secs y el parámetro seconds
    De este modo se calcula la duración del partido medida en segundos.
    """
    hours_secs = 3600*hours
    mins_secs = 60*minutes
    return hours_secs + mins_secs + seconds

print("la duración del partido fue de", match_duration (11,6,23), "segundos")
