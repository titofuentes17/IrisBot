#THIS IS A COMPLETELY OPEN SOURCED, INDEPENDENTLY DEVELOPED BOT THAT USES RIOT GAMES API, BUT IT WAS NOT DEVELOPED BY RIOT.

from random import choice, randint
import requests
import discord
from discord.ext import commands 
from discord.ext.commands import*
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)


champions = {266: 'Aatrox', 103: 'Ahri', 84: 'Akali', 166: 'Akshan', 12: 'Alistar', 32: 'Amumu', 34: 'Anivia', 1: 'Annie', 523: 'Aphelios', 22: 'Ashe', 136: 'Aurelion Sol', 268: 'Azir', 432: 'Bard', 200: "Bel'Veth", 53: 'Blitzcrank', 63: 'Brand', 201: 'Braum', 233: 'Briar', 51: 'Caitlyn', 164: 'Camille', 69: 'Cassiopeia', 31: "Cho'Gath", 42: 'Corki', 122: 'Darius', 131: 'Diana', 119: 'Draven', 36: 'Dr.Mundo', 245: 'Ekko', 60: 'Elise', 28: 'Evelynn', 81: 'Ezreal', 9: 'Fiddlesticks', 114: 'Fiora', 105: 'Fizz', 3: 'Galio', 41: 'Gangplank', 86: 'Garen', 150: 'Gnar', 79: 'Gragas', 104: 'Graves', 887: 'Gwen', 120: 'Hecarim', 74: 'Heimerdinger', 910: 'Hwei', 420: 'Illaoi', 39: 'Irelia', 427: 'Ivern', 40: 'Janna', 59: 'Jarvan', 24: 'Jax', 126: 'Jayce', 202: 'Jhin', 222: 'Jinx', 145: "Kai'Sa", 429: 'Kalista', 43: 'Karma', 30: 'Karthus', 38: 'Kassadin', 55: 'Katarina', 10: 'Kayle', 141: 'Kayn', 85: 'Kennen', 121: "Kha'Zix", 203: 'Kindred', 240: 'Kled', 96: "Kog'Maw", 897: "K'Sante", 7: 'LeBlanc', 64: 'Lee Sin', 89: 'Leona', 876: 'Lillia', 127: 'Lissandra', 236: 'Lucian', 117: 'Lulu', 99: 'Lux', 54: 'Malphite', 90: 'Malzahar', 57: 'Maokai', 11: 'Master Yi', 902: 'Milio', 21: 'Miss Fortune', 62: 'Wukong', 82: 'Mordekaiser', 25: 'Morgana', 950: 'Naafiri', 267: 'Nami', 75: 'Nasus', 111: 'Nautilus', 518: 'Neeko', 76: 'Nidalee', 895: 'Nilah', 56: 'Nocturne', 20: 'Nunu', 2: 'Olaf', 61: 'Orianna', 516: 'Ornn', 80: 'Pantheon', 78: 'Poppy', 555: 'Pyke', 246: 'Qiyana', 133: 'Quinn', 497: 'Rakan', 33: 'Rammus', 421: "Rek'Sai", 526: 'Rell', 888: 'Renata Glasc', 58: 'Renekton', 107: 'Rengar', 92: 'Riven', 68: 'Rumble', 13: 'Ryze', 360: 'Samira', 113: 'Sejuani', 235: 'Senna', 147: 'Seraphine', 875: 'Sett', 35: 'Shaco', 98: 'Shen', 102: 'Shyvana', 27: 'Singed', 14: 'Sion', 15: 'Sivir', 72: 'Skarner', 901: 'Smolder', 37: 'Sona', 16: 'Soraka', 50: 'Swain', 517: 'Sylas', 134: 'Syndra', 223: 'Tahm Kench', 163: 'Taliyah', 91: 'Talon', 44: 'Taric', 17: 'Teemo', 412: 'Thresh', 18: 'Tristana', 48: 'Trundle', 23: 'Tryndamere', 4: 'Twisted Fate', 29: 'Twitch', 77: 'Udyr', 6: 'Urgot', 110: 'Varus', 67: 'Vayne', 45: 'Veigar', 161: "Vel'Koz", 711: 'Vex', 254: 'Vi', 234: 'Viego', 112: 'Viktor', 8: 'Vladimir', 106: 'Volibear', 19: 'Warwick', 498: 'Xayah', 101: 'Xerath', 5: 'Xin Zhao', 157: 'Yasuo', 777: 'Yone', 83: 'Yorick', 350: 'Yuumi', 154: 'Zac', 238: 'Zed', 221: 'Zeri', 115: 'Ziggs', 26: 'Zilean', 142: 'Zoe', 143: 'Zyra'}

#load token
load_dotenv()
discord_token: Final[str] = os.getenv('DISCORD_TOKEN')
api_key: Final[str] = os.getenv('RIOT_API')
intents = discord.Intents.all()

#functions: 

def summoner_function(riot_id='titofuentes#euw',n = 20):
    print('inicio summoner', riot_id)
    win = 0
    kills = 0
    deaths = 0
    assists = 0
    firstBloodP = 0
    surrenderedGames = 0
    champions = {}
    pentas = 0
    dpm = 0
    kp = 0
    solokills = 0
    damagePercentage = 0
    riot_id = riot_id.replace(' ', '%20')
    riot_id = riot_id.replace('#', '/')
    rq = requests.get(f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}?api_key={api_key}').json()
    p_uid = rq['puuid']
    matches_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{p_uid}/ids?start=0&count={n}&api_key={api_key}'
    match_list = requests.get(matches_url).json()
    print('summoner matches', riot_id)
    
    for match in match_list:
        try:
            print(match)
            match_data =  requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}').json()
            i = match_data['metadata']['participants'].index(p_uid)
            gamestats = match_data['info']['participants'][i]
            #stats
            kills = kills +  gamestats['kills']    
            deaths = deaths +  gamestats['deaths']  
            assists = assists +  gamestats['assists']
            pentas = pentas + gamestats['pentaKills']
            champion = gamestats['championName']
            champions[champion] =  champions.get(champion, 0) + 1
            #challenges stats
            dpm = dpm +  gamestats['challenges']['damagePerMinute'] 
            kp = kp + gamestats['challenges']['killParticipation']
            solokills = solokills +  gamestats['challenges']['soloKills'] 
            damagePercentage = damagePercentage + gamestats['challenges']['teamDamagePercentage']
            
            #ifs
            if gamestats['firstBloodKill'] or gamestats['firstBloodAssist']:
                firstBloodP = firstBloodP +1
            if gamestats['gameEndedInEarlySurrender'] or gamestats['gameEndedInSurrender']:
                surrenderedGames = surrenderedGames +1
            if gamestats['win']:
                win = win +1
        except:
            print(f'error in match {match}')
            n = n-1
    print('fin summoner', riot_id)
    if n == 0:
            return f'error in all data for {rq["gameName"]}'
    if deaths == 0:
        return f' {rq["gameName"]} Stats for last {n} games: \nWR: {round((win/n)*100),2} % ({win} out of {n}).\nTotal kda in last {n} games: {(kills)}/{deaths}/{assists}. Av Kda last {n} games : {round(kills/n,2)}/{round(deaths/n,2)}/{round(assists/n,2)}. Last {n} games kda = {round((kills + assists)/1,2)}.\nFirst blood participation: {firstBloodP}/{n}, Pentakills: {pentas}, Surrenders: {surrenderedGames}, Average dpm: {round(dpm/n,2)}, average KP: {round(kp*100/n,2)}%, solokills: {solokills} ({solokills/n}/game),average damage%: {round(damagePercentage*100/n,2)}%\nChampions Played: {champions}'
    return f' {rq["gameName"]} Stats for last {n} games: \nWR: {round((win/n)*100),2} % ({win} out of {n}).\nTotal kda in last {n} games: {(kills)}/{deaths}/{assists}. Av Kda last {n} games : {round(kills/n,2)}/{round(deaths/n,2)}/{round(assists/n,2)}. Last {n} games kda = {round((kills + assists)/deaths,2)}.\nFirst blood participation: {firstBloodP}/{n}, Pentakills: {pentas}, Surrenders: {surrenderedGames}, Average dpm: {round(dpm/n,2)}, average KP: {round(kp*100/n,2)}%, solokills: {solokills} ({solokills/n}/game),average damage%: {round(damagePercentage*100/n,2)}%\nChampions Played: {champions}'
    
            
def wr_func(riot_id='titofuentes#euw',n = 40):
    print('inicio wr')
    win = 0
    riot_id = riot_id.replace(' ', '%20')
    riot_id = riot_id.replace('#', '/')
    rq = requests.get(f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}?api_key={api_key}').json()
    p_uid = rq['puuid']
    matches_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{p_uid}/ids?start=0&count=20&api_key={api_key}'
    match_list = requests.get(matches_url).json()
    for match in match_list:
        try:
            print(match)
            match_data =  requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}').json()
            i = match_data['metadata']['participants'].index(p_uid)
            if match_data['info']['participants'][i]['win']:
                win = win +1
        except:
            print(f'error in match {match}')
            n = n-1
    print('fin wr')
    return f' {rq["gameName"]} WR: {round((win/n)*100,2)} % ({win} out of {n})'


def pings_func(riot_id='titofuentes#euw',n = 20):
    print('inicio pings')
    pings = {'allInPings':0,'assistMePings':0,'basicPings':0,'commandPings':0,'dangerPings':0,'enemyMissingPings':0,'enemyVisionPings':0,
    'getBackPings':0,'holdPings':0,'needVisionPings':0,'onMyWayPings':0,'pushPings':0,'visionClearedPings':0}
    riot_id = riot_id.replace(' ', '%20')
    riot_id = riot_id.replace('#', '/')
    rq = requests.get(f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}?api_key={api_key}').json()
    p_uid = rq['puuid']
    matches_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{p_uid}/ids?start=0&count=20&api_key={api_key}'
    match_list = requests.get(matches_url).json()
    for match in match_list:
        match_data =  requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}').json()
        for element in match_data['info']['participants']:
            if element['puuid'] == p_uid:
                for ping_type in pings:
                    pings[ping_type] = pings[ping_type] + element[ping_type]
    total = sum(pings.values())
    print('fin kda')
    return(f'Total {rq["gameName"]} pings in last {n} games = {total}. (average = {total/n}) Specific pings = {pings}')


def kda_func(riot_id='titofuentes#euw',n = 20):
    print('inicio kda')
    kills = 0
    deaths = 0
    assists = 0
    riot_id = riot_id.replace(' ', '%20')
    riot_id = riot_id.replace('#', '/')
    rq = requests.get(f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}?api_key={api_key}').json()
    p_uid = rq['puuid']
    matches_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{p_uid}/ids?start=0&count=20&api_key={api_key}'
    match_list = requests.get(matches_url).json()
    for match in match_list:
        match_data =  requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}').json()
        for element in match_data['info']['participants']:
            if element['puuid'] == p_uid:
                kills = kills +  element['kills']    
                deaths = deaths +  element['deaths']  
                assists = assists +  element['assists']  
    print('fin kda')
    return f'{rq["gameName"]} total kda in last {n} games: {kills}/{deaths}/{assists}. Av Kda last {n} games : {kills/n}/{deaths/n}/{assists/n}. Last {n} games kda = {(kills + assists)/deaths}'


def ingame_rquest(p_uid, username, n = 10):
    print('-----------',username,'---------------------------------------------------------')
    win = 0
    kills = 0
    deaths = 0
    assists = 0
    firstBloodP = 0
    surrenderedGames = 0
    champions = {}
    pentas = 0
    dpm = 0
    kp = 0
    solokills = 0
    damagePercentage = 0
    matches_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{p_uid}/ids?start=0&count=20&api_key={api_key}'
    match_list = requests.get(matches_url).json()
    for match in match_list:
        try:
            print(f'try in match {match}')
            match_data =  requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}').json()
            i = match_data['metadata']['participants'].index(p_uid)
            gamestats = match_data['info']['participants'][i]
            #stats
            kills = kills +  gamestats['kills']    
            deaths = deaths +  gamestats['deaths']  
            assists = assists +  gamestats['assists']
            pentas = pentas + gamestats['pentaKills']
            champion = gamestats['championName']
            champions[champion] =  champions.get(champion, 0) + 1
            #challenges stats
            dpm = dpm +  gamestats['challenges']['damagePerMinute'] 
            kp = kp + gamestats['challenges']['killParticipation']
            solokills = solokills +  gamestats['challenges']['soloKills'] 
            damagePercentage = damagePercentage + gamestats['challenges']['teamDamagePercentage']
            
            #ifs
            if gamestats['firstBloodKill'] or gamestats['firstBloodAssist']:
                firstBloodP = firstBloodP +1
            if gamestats['gameEndedInEarlySurrender'] or gamestats['gameEndedInSurrender']:
                surrenderedGames = surrenderedGames +1
            if gamestats['win']:
                win = win +1
            print(f'successful in match {match}')
        except:
            print(f'error in match {match}')
            n = n-1
        if n == 0:
            return f'error in all data for summoner {username}'
        if deaths == 0:
            return f'{username} WR: {round((win/n)*100),2} % ({win} out of {n}).\nTotal kda in last {n} games: {(kills)}/{deaths}/{assists}. Av Kda last {n} games : {round(kills/n,2)}/{round(deaths/n,2)}/{round(assists/n,2)}. Last {n} games kda = {round((kills + assists)/1,2)}.\nFirst blood participation: {firstBloodP}/{n}, Pentakills: {pentas}, Surrenders: {surrenderedGames}, Average dpm: {round(dpm/n,2)}, average KP: {round(kp*100/n,2)}%, solokills: {solokills} ({solokills/n}/game),average damage%: {round(damagePercentage*100/n,2)}%\nChampions Played: {champions}'
    return f'{username} WR: {round((win/n)*100),2} % ({win} out of {n}).\nTotal kda in last {n} games: {(kills)}/{deaths}/{assists}. Av Kda last {n} games : {round(kills/n,2)}/{round(deaths/n,2)}/{round(assists/n,2)}. Last {n} games kda = {round((kills + assists)/deaths,2)}.\nFirst blood participation: {firstBloodP}/{n}, Pentakills: {pentas}, Surrenders: {surrenderedGames}, Average dpm: {round(dpm/n,2)}, average KP: {round(kp*100/n,2)}%, solokills: {solokills} ({solokills/n}/game),average damage%: {round(damagePercentage*100/n,2)}%\nChampions Played: {champions}'

def ingame_function(riot_id='titofuentes#euw'):
    team_100 = []
    team_200 = []
    #primero obtenemos el ingame
    print('inicio ingame')
    riot_id = riot_id.replace(' ', '%20')
    riot_id = riot_id.replace('#', '/')
    rq = requests.get(f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}?api_key={api_key}').json()
    p_uid = rq['puuid']
    rq = requests.get(f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{p_uid}?api_key={api_key}').json()
    summoner_id = rq['id']
    game_rq = requests.get(f'https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={api_key}').json()
    print(game_rq)
    #una vez tenemos los datos, procedemos a procesarlos:
    for participant in game_rq['participants']:
        if participant['puuid'] == p_uid:
            aliado = participant['teamId']
            
        elif participant['teamId'] == 100:
            team_100.append(ingame_rquest(participant['puuid'],participant['summonerName']))
        elif participant['teamId'] == 200:
            team_200.append(ingame_rquest(participant['puuid'],participant['summonerName']))
    if aliado == 100:
        return [f'Estadisticas equipo aliado: \n\n{team_100[0]}\n\n{team_100[1]}\n\n{team_100[2]}\n\n{team_100[3]}',f'Estadisticas equipo enemigo: \n\n{team_200[0]}\n\n{team_200[1]}\n\n{team_200[2]}\n\n{team_200[3]}\n\n{team_200[4]}']
    if aliado == 200:
        return [f'Estadisticas equipo aliado: \n\n{team_200[0]}\n\n{team_200[1]}\n\n{team_200[2]}\n\n{team_200[3]}',f'Estadisticas equipo enemigo: \n\n{team_100[0]}\n\n{team_100[1]}\n\n{team_100[2]}\n\n{team_100[3]}\n\n{team_200[4]}']
            
    
def mastery_func (riot_id='titofuentes#euw',n = 20):
    print('inicio mastery')
    riot_id = riot_id.replace(' ', '%20')
    riot_id = riot_id.replace('#', '/')
    rq = requests.get(f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}?api_key={api_key}').json()
    p_uid = rq['puuid']
    string = f'{n} champions with Highest mastery for {rq["gameName"]}:\n '
    masteries = requests.get(f'https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{p_uid}?api_key={api_key}').json()
    for mastery in masteries[:n]:
        string = string +  f' {champions[(mastery["championId"])]}: Level: {mastery["championLevel"]}, {mastery["championPoints"]} points\n'
    print('fin mastery')
    return string

@bot.event
async def on_ready():
    print(f'Conected as {bot.user.name}')
    
@bot.command()
async def kda(ctx,*riot_id:str):
    good_id = ''.join(riot_id)
    resultado = kda_func(good_id)
    await ctx.send(resultado)
    
@bot.command()
async def winrate(ctx,*riot_id:str):
    good_id = ''.join(riot_id)
    resultado = wr_func(good_id)
    await ctx.send(resultado)
    
@bot.command()
async def summoner(ctx,*riot_id:str):
    good_id = ''.join(riot_id)
    resultado = summoner_function(good_id)
    await ctx.send(resultado) 

@bot.command()
async def masteries(ctx,*riot_id:str):
    good_id = ''.join(riot_id)
    resultado = mastery_func(good_id)
    await ctx.send(resultado) 

@bot.command()
async def pings(ctx,*riot_id:str):
    good_id = ''.join(riot_id)
    resultado = pings_func(good_id)
    await ctx.send(resultado) 
     
    
@bot.command()
async def ingame(ctx,*riot_id:str):
    good_id = ''.join(riot_id)
    resultado = ingame_function(good_id)
    await ctx.send(resultado[0])
    await ctx.send ('-----------------------------------------------------------------------------------')
    await ctx.send(resultado[1])
    
    
    
#main
def main() -> None:
    bot.run(discord_token)
    
    
    
if __name__ == '__main__':
    main()

