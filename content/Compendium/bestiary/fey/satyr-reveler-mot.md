---
title: Satyr Reveler
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/1
- monster/size/medium
- monster/type/fey
statblock: inline
aliases: ["Satyr Reveler"]
---
# Satyr Reveler
*Source: Mythic Odysseys of Theros p. 242*  

![](Compendium/bestiary/fey/img/satyr-reveler.webp#right|850)  
Pursuing lives of endless reverie, satyr revelers eagerly participate in celebrations wherever they find them. Their boisterous natures go far toward tempting others to eat, drink, and carouse with them. Faced with stodgier individuals or outright rivals, satyr revelers don't balk at using the magic of their music, dance, or other performances to charm opponents into joining their festivities. In the aftermath, these satyrs' foes are more likely to suffer embarrassment and groggy mornings than any lasting harm.

While most satyrs are known for their high spirits, love of revels, and gregarious personalities, these outgoing people are neither naive nor defenseless. Some satyrs delightedly torment stuffy individuals or pull pranks on the unwary, pastimes that can predictably lead to scuffles. If a satyr can't talk their way out of a conflict—or diffuse it with a good-natured distraction—they readily defend themselves, their friends, and their homes in the Skola Vale. With diversions aside, satyrs bend their cleverness toward tactics and methods of ending conflicts as swiftly as possible. This often means turning the same skills that make them famed celebrants toward battle, be it captivating performances or the aim developed through endless games of skill. Once a threat is overcome, though, satyrs are quick to engage in their favorite part of battle: the victory celebration.
```statblock
"name": "Satyr Reveler (MOT)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "13"
"hp": !!int "33"
"hit_dice": "6d8 + 6"
"modifier": !!int "3"
"stats":
  - !!int "12"
  - !!int "16"
  - !!int "13"
  - !!int "12"
  - !!int "10"
  - !!int "16"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+5"
  - "name": "[[skills#Performance|Performance]]"
    "desc": "+7"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": "Common, Sylvan"
"cr": "1"
"traits":
  - "desc": "If the satyr performs for at least 1 minute, it chooses up to four humanoids\
      \ within 60 feet of it who watched or listened to the entire performance. Each\
      \ target must succeed on a DC 13 Wisdom saving throw or be [[conditions#Charmed|charmed]].\
      \ While [[conditions#Charmed|charmed]] in this way, the target\
      \ idolizes the satyr and will take part in the satyr's revels. The [[conditions#Charmed|charmed]]\
      \ condition ends for the creature after 1 hour, if it takes any damage, if the\
      \ satyr attacks the target, or if the target witnesses the satyr attacking or\
      \ damaging any of the target's allies."
    "name": "Enthralling Performance"
  - "desc": "The satyr has advantage on saving throws against spells and other magical\
      \ effects."
    "name": "Magic Resistance"
  - "desc": "Magic can't put the satyr to sleep."
    "name": "Sleepless Reveler"
"actions":
  - "desc": "The satyr makes two ram attacks or two shortbow attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 6\
      \ (2d4 + 1) bludgeoning damage."
    "name": "Ram"
  - "desc": "*Ranged Weapon Attack:* +5 to hit, range 80/320 ft., one target. *Hit:*\
      \ 6 (1d6 + 3) piercing damage."
    "name": "Shortbow"
"source":
  - "MOT"
"image": "Compendium/bestiary/fey/token/satyr-reveler-mot.webp"
```
^statblock