---
title: Master Thief
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["Master Thief"]
---
# Master Thief
*Source: Volo's Guide to Monsters p. 216, Mythic Odysseys of Theros*  

![](Compendium/bestiary/humanoid/img/master-thief.webp#right|850)  
Master thieves are known for perpetrating daring heists. They tend to develop a reputation and a cult of personality. A master thief might "retire" from hands-on work to run a thieves' guild, spearhead some covert enterprise, or enjoy a quiet life of luxury.
```statblock
"name": "Master Thief (VGM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "[[studded-leather-armor-xphb|studded leather]]"
"hp": !!int "83"
"hit_dice": "13d8 + 26"
"modifier": !!int "4"
"stats":
  - !!int "11"
  - !!int "18"
  - !!int "14"
  - !!int "11"
  - !!int "11"
  - !!int "12"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "7"
  - "intelligence": !!int "3"
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+7"
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+3"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
  - "name": "[[skills#Sleight%20of%20Hand|Sleight of Hand]]"
    "desc": "+7"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+7"
"senses": "passive Perception 13"
"languages": "any one language (usually Common) plus Thieves' cant"
"cr": "5"
"traits":
  - "desc": "On each of its turns, the thief can use a bonus action to take the Dash,\
      \ Disengage, or Hide action."
    "name": "Cunning Action"
  - "desc": "If the thief is subjected to an effect that allows it to make a Dexterity\
      \ saving throw to take only half damage, the thief instead takes no damage if\
      \ it succeeds on the saving throw, and only half damage if it fails."
    "name": "Evasion"
  - "desc": "The thief deals an extra 14 (4d6) damage when it hits a target with\
      \ a weapon attack and has advantage on the attack roll, or when the target is\
      \ within 5 feet of an ally of the thief that isn't [[conditions#Incapacitated|incapacitated]]\
      \ and the thief doesn't have disadvantage on the attack roll."
    "name": "Sneak Attack (1/Turn)"
"actions":
  - "desc": "The thief makes three attacks with its shortsword."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 7\
      \ (1d6 + 4) piercing damage."
    "name": "Shortsword"
  - "desc": "*Ranged Weapon Attack:* +7 to hit, range 80/320 ft., one target. *Hit:*\
      \ 8 (1d8 + 4) piercing damage."
    "name": "Light Crossbow"
"reactions":
  - "desc": "The thief halves the damage that it takes from an attack that hits it.\
      \ The thief must be able to see the attacker."
    "name": "Uncanny Dodge"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/master-thief-vgm.webp"
```
^statblock