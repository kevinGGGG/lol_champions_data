#coding=utf-8
import requests
from bs4 import BeautifulSoup
import sys
class Chaimpions:
	def __init__(self,name,health,health_per_level,health_regenation,health_regenation_per_level,mana,mana_per_level,mana_regenation,mana_regenation_per_level,
		ranged,attack_damage,attack_damage_per_level,attack_speed
		,attack_speed_per_level,armor,armor_per_level,magic,magic_per_level,move_speed):
		self.name = name
		self.health = health
		self.health_per_level = health_per_level
		self.health_regenation = health_regenation
		self.health_regenation_per_level = health_regenation_per_level
		self.mana = mana
		self.mana_per_level = mana_per_level
		self.mana_regenation = mana_regenation
		self.mana_regenation_per_level = mana_regenation_per_level
		self.ranged = ranged
		self.attack_damage = attack_damage
		self.attack_damage_per_level = attack_damage_per_level
		self.attack_speed = attack_speed
		self.attack_speed_per_level = attack_speed_per_level
		self.armor = armor
		self.armor_per_level = armor_per_level
		self.magic = magic
		self.magic_per_level = magic_per_level
		self.move_speed = move_speed
champions_names = []
champ_name_res = requests.get("http://www.lol123.com/ziyuan/mingzi")
soup_name = BeautifulSoup(champ_name_res.text,'html.parser')
for ele in soup_name.find_all("td"):
	if ele.string.encode('utf-8').isalpha():
		champions_names.append(ele.string)
for single_champion in champions_names:
	res = requests.get(("http://leagueoflegends.wikia.com/wiki/%s"%single_champion))
	soup = BeautifulSoup(res.text,'html.parser')
	name = soup.find("span",class_="name").string
	health = float(soup.find("span",class_="Health").string)
	health_per_level = float(soup.find("span",class_="Health_lvl").string)
	health_regenation = float(soup.find("span",class_="HealthRegen").string)
	health_regenation_per_level =  float(soup.find("span",class_="HealthRegen_lvl").string) 
	if soup.find("span",class_="ResourceBar") is not None:
		mana = float(soup.find("span",class_="ResourceBar").string)
		mana_per_level = float(soup.find("span",class_="ResourceBar").string)
		if soup.find("span",class_="ResourceRegen") is not None:
			mana_regenation = float(soup.find("span",class_="ResourceRegen").string)
			mana_regenation_per_level = float(soup.find("span",class_="ResourceRegen_lvl").string)
		else:
			mana_regenation = 0
			mana_regenation_per_level = 0
	ranged = int(soup.find("span",class_="Range").string)
	attack_damage = float(soup.find("span",class_="AttackDamage").string)
	attack_damage_per_level = float(soup.find("span",class_="AttackDamage_lvl").string)
	attack_speed = float(soup.find("span",class_="AttackSpeed").string)
	attack_speed_per_level = float(soup.find("span",class_="AttackSpeedBonus_lvl").string)
	armor = float(soup.find("span",class_="Armor").string)
	armor_per_level = float(soup.find("span",class_="Armor_lvl").string)
	magic = float(soup.find("span",class_="MagicResist").string)
	magic_per_level = float(soup.find("span",class_="MagicResist_lvl").string)
	move_speed = int(soup.find("span",class_="MovementSpeed").string)

	champion = Chaimpions(name,health,health_per_level,health_regenation,health_regenation_per_level,mana,mana_per_level,mana_regenation,mana_regenation_per_level,
		ranged,attack_damage,attack_damage_per_level,attack_speed,attack_speed_per_level,armor,armor_per_level,magic,magic_per_level,move_speed)
	file = open("%s.txt"%(champion.name),'w')
	file.write(champion.name+"\n")
	file.write("Health:%.2f (+%d)\n" %(champion.health,champion.health_per_level))
	file.write("Health Regenation:%.1f(+%.2f)\n"%(champion.health_regenation,champion.health_regenation_per_level))
	file.write("Mana:%.2f (+%.2f)\n"%(champion.mana,champion.mana_per_level))
	file.write("Mana Regenation:%.1f (+%.1f)\n"%(champion.mana_regenation,champion.mana_regenation_per_level))
	file.write("Ranged:%d\n"%(champion.ranged))
	file.write("AttackDamage:%.3f (+%.2f)\n"%(champion.attack_damage,champion.attack_damage_per_level))
	file.write("AttackSpeed:%.3f (+%.3f)\n"%(champion.attack_speed,champion.attack_speed_per_level))
	file.write("Armor:%.2f (+%.2f)\n"%(champion.armor,champion.armor_per_level))
	file.write("Magic:%.2f (+%.2f)\n"%(champion.magic,champion.magic_per_level))
	file.write("Move Speed:%d\n"%(champion.move_speed))
	file.close()


