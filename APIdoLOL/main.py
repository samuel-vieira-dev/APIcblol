import requests
import json
#CHAVE DA API ###############################
#RGAPI-2f0393a5-8071-466a-8066-872a119a3ff8
#SUMMONERNAME
#4OO Bad Request
#ID = mkY9YR1rpEy9kxNHjs93qwfakRPDUg8VeTCvPJhcA86lo9w
#accountId = TCoa8qmwnnyZd8aokZleiA7UAJsLT3wtBrNsBi02PlIBp88
#puuid = d1OWkTKXBmsYNqJSf5qGyc94OZ25-GOxwIAomRz3hVMA1rhtZQB6Exxl2tJBipS5SnqeziRDntan6A

#url = requests.get("https://br1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/mkY9YR1rpEy9kxNHjs93qwfakRPDUg8VeTCvPJhcA86lo9w", headers={"X-Riot-Token":"RGAPI-fda5bbb0-0312-4da1-b7ee-471dc08d1120","encryptionSummonerId":"mkY9YR1rpEy9kxNHjs93qwfakRPDUg8VeTCvPJhcA86lo9w"})
#resposta = json.loads(url.content)
#print(resposta)

url = requests.get("https://feed.lolesports.com/livestats/v1/window/105658534675811034?hl=pt-BR&startingTime=2021-03-13T22:10:20.000Z")
resposta = json.loads(url.content)
print("Blue Team")
print("Ouro do Time:", resposta["frames"][0]["blueTeam"]["totalGold"] ,"//", "Torres:", resposta["frames"][0]["blueTeam"]["towers"] ,"//", "Kills:", resposta["frames"][0]["blueTeam"]["totalKills"])
print(resposta["gameMetadata"]["blueTeamMetadata"]["participantMetadata"][0]["summonerName"],"//","Ouro:", resposta["frames"][0]["blueTeam"]["participants"][0]["totalGold"],"//","Level:", resposta["frames"][0]["blueTeam"]["participants"][0]["level"],"//","Eliminações:", resposta["frames"][0]["blueTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][0]["blueTeam"]["participants"][0]["deaths"],"//","Assistências:", resposta["frames"][0]["blueTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][0]["blueTeam"]["participants"][0]["currentHealth"])
print(resposta["gameMetadata"]["blueTeamMetadata"]["participantMetadata"][1]["summonerName"],"//","Ouro:", resposta["frames"][1]["blueTeam"]["participants"][1]["totalGold"],"//","Level:", resposta["frames"][1]["blueTeam"]["participants"][1]["level"],"//","Eliminações:", resposta["frames"][1]["blueTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][1]["blueTeam"]["participants"][1]["deaths"],"//","Assistências:", resposta["frames"][1]["blueTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][1]["blueTeam"]["participants"][1]["currentHealth"])
print(resposta["gameMetadata"]["blueTeamMetadata"]["participantMetadata"][2]["summonerName"],"//","Ouro:", resposta["frames"][2]["blueTeam"]["participants"][2]["totalGold"],"//","Level:", resposta["frames"][2]["blueTeam"]["participants"][2]["level"],"//","Eliminações:", resposta["frames"][2]["blueTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][2]["blueTeam"]["participants"][2]["deaths"],"//","Assistências:", resposta["frames"][2]["blueTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][2]["blueTeam"]["participants"][2]["currentHealth"])
print(resposta["gameMetadata"]["blueTeamMetadata"]["participantMetadata"][3]["summonerName"],"//","Ouro:", resposta["frames"][3]["blueTeam"]["participants"][3]["totalGold"],"//","Level:", resposta["frames"][3]["blueTeam"]["participants"][3]["level"],"//","Eliminações:", resposta["frames"][3]["blueTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][3]["blueTeam"]["participants"][3]["deaths"],"//","Assistências:", resposta["frames"][3]["blueTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][3]["blueTeam"]["participants"][3]["currentHealth"])
print(resposta["gameMetadata"]["blueTeamMetadata"]["participantMetadata"][4]["summonerName"],"//","Ouro:", resposta["frames"][4]["blueTeam"]["participants"][4]["totalGold"],"//","Level:", resposta["frames"][4]["blueTeam"]["participants"][4]["level"],"//","Eliminações:", resposta["frames"][4]["blueTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][4]["blueTeam"]["participants"][4]["deaths"],"//","Assistências:", resposta["frames"][4]["blueTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][4]["blueTeam"]["participants"][4]["currentHealth"])
print('---------------------------------------------------------------------------------------------------------------------')
print("Red Team")
print("Ouro do Time:", resposta["frames"][0]["redTeam"]["totalGold"] ,"//", "Torres:", resposta["frames"][0]["redTeam"]["towers"] ,"//", "Kills:", resposta["frames"][0]["redTeam"]["totalKills"])
print(resposta["gameMetadata"]["redTeamMetadata"]["participantMetadata"][0]["summonerName"],"//","Ouro:", resposta["frames"][0]["redTeam"]["participants"][0]["totalGold"],"//","Level:", resposta["frames"][0]["redTeam"]["participants"][0]["level"],"//","Eliminações:", resposta["frames"][0]["redTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][0]["redTeam"]["participants"][0]["deaths"],"//","Assistências:", resposta["frames"][0]["redTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][0]["redTeam"]["participants"][0]["currentHealth"])
print(resposta["gameMetadata"]["redTeamMetadata"]["participantMetadata"][1]["summonerName"],"//","Ouro:", resposta["frames"][1]["redTeam"]["participants"][1]["totalGold"],"//","Level:", resposta["frames"][1]["redTeam"]["participants"][1]["level"],"//","Eliminações:", resposta["frames"][1]["redTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][1]["redTeam"]["participants"][1]["deaths"],"//","Assistências:", resposta["frames"][1]["redTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][1]["redTeam"]["participants"][1]["currentHealth"])
print(resposta["gameMetadata"]["redTeamMetadata"]["participantMetadata"][2]["summonerName"],"//","Ouro:", resposta["frames"][2]["redTeam"]["participants"][2]["totalGold"],"//","Level:", resposta["frames"][2]["redTeam"]["participants"][2]["level"],"//","Eliminações:", resposta["frames"][2]["redTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][2]["redTeam"]["participants"][2]["deaths"],"//","Assistências:", resposta["frames"][2]["redTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][2]["redTeam"]["participants"][2]["currentHealth"])
print(resposta["gameMetadata"]["redTeamMetadata"]["participantMetadata"][3]["summonerName"],"//","Ouro:", resposta["frames"][3]["redTeam"]["participants"][3]["totalGold"],"//","Level:", resposta["frames"][3]["redTeam"]["participants"][3]["level"],"//","Eliminações:", resposta["frames"][3]["redTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][3]["redTeam"]["participants"][3]["deaths"],"//","Assistências:", resposta["frames"][3]["redTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][3]["redTeam"]["participants"][3]["currentHealth"])
print(resposta["gameMetadata"]["redTeamMetadata"]["participantMetadata"][4]["summonerName"],"//","Ouro:", resposta["frames"][4]["redTeam"]["participants"][4]["totalGold"],"//","Level:", resposta["frames"][4]["redTeam"]["participants"][4]["level"],"//","Eliminações:", resposta["frames"][4]["redTeam"]["participants"][0]["kills"],"//","Mortes:", resposta["frames"][4]["redTeam"]["participants"][4]["deaths"],"//","Assistências:", resposta["frames"][4]["redTeam"]["participants"][0]["assists"],"//","Vida:", resposta["frames"][4]["redTeam"]["participants"][4]["currentHealth"])
print('---------------------------------------------------------------------------------------------------------------------')