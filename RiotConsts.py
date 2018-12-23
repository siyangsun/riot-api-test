# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 23:05:33 2018

@author: Siyang
"""

URL = {
    'base' : 'https://{proxy}.api.riotgames.com/lol/{url}',
    'summoner_by_name' : 'summoner/v{version}/summoners/by-name/{names}',
    'champion_mastery_by_summoner' : 'champion-mastery/v{version}/champion-masteries/by-summoner/{ids}'
}

API_VERSION = {
    'summoner' : '4',
    'champion_mastery' : '4'
}

REGIONS = {
    'north_america' : 'na1'
}