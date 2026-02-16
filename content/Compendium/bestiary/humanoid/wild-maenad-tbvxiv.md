---
title: Wild Maenad
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxiv
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Wild Maenad"]
---
# Wild Maenad
*Source: Theros Bestiary TBVXIV*  

The maenads of Theros are men and women possessed by Xenagos.

![Wild Maenad](https://img.scryfall.com/cards/art_crop/front/7/b/7b8ec95a-e728-446b-8c4a-a3571e6aa458.jpg?1562639876#right)  

```statblock
"name": "Wild Maenad (TBVXIV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"hp": !!int "6"
"hit_dice": "1d8 + 2"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "15"
  - !!int "14"
  - !!int "7"
  - !!int "7"
  - !!int "15"
"speed": "35 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+4"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+0"
  - "name": "[[skills#Performance|Performance]]"
    "desc": "+4"
"damage_vulnerabilities": "psychic"
"damage_resistances": "cold, fire, poison"
"senses": "passive Perception 10"
"languages": "Common, any language"
"cr": "3"
"traits":
  - "desc": "If Xenagos becomes [[conditions#Incapacitated|incapacitated]], or if the maenad isn't on one of Theros's three realms, the maenad becomes a **human commoner**."
    "name": "Charmed by Xenagos"
  - "desc": "If the maenad performs for at least 1 minute, it chooses up to four humanoids within 60 feet of it who watched or listened to the entire performance. Each target must succeed on a DC 13 Wisdom saving throw or be [[conditions#Charmed|charmed]]. While [[conditions#Charmed|charmed]] in this way, the target idolizes the maenad and will take part in the maenad's revels. The [[conditions#Charmed|charmed]] condition ends for the creature after 1 hour, if it takes any damage, if the maenad attacks the target, or if the target witnesses the maenad attacking or damaging any of the target’s allies."
    "name": "Enthralling Performance"
  - "desc": "The maenad has proficiency with improvised weapons."
    "name": "Improvised Weapon Proficiency"
  - "desc": "Magic can’t put the maenad to sleep."
    "name": "Sleepless Reveler"
  - "desc": "While the maenad is in any of Theros's three realms, it can magically convey what it senses to Xenagos."
    "name": "Telepathic Bond"
"actions":
  - "desc": "The maenad makes two attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4+3) bludgeoning damage."
    "name": "Unarmed Strike"
"source":
  - "TBVXIV"
"image": "Compendium/bestiary/humanoid/token/wild-maenad-tbvxiv.webp"
```
^statblock