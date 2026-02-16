---
title: Silver Dragon Wyrmling
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/dragon/metallic
statblock: inline
aliases: ["Silver Dragon Wyrmling"]
---
# Silver Dragon Wyrmling
*Source: Monster Manual (2024) p. 278. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/silver-dragon-wyrmling.webp#right|850)  
Silver dragon wyrmlings typically live with one or more parents or mentors, learning much about the world and its past before living on their own.

## Silver Dragons

*Dragons of Courage and Fairness*

- **Habitat.** Mountain, Urban  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Silver dragons work to preserve peace and encourage greatness. They try to live as examples of decency while remaining watchful against evil.

Silver dragons typically dwell amid snow-capped mountains, though aspirations and congeniality drive some to instead live among cosmopolitan societies. Disguised as humanoids, they ally with artists, historians, knights, and humble leaders who learn from the past to create better futures.

Silver dragons take inspiration from legendary heroes and have grand ambitions. Many collect treasures that reflect these interests, such as histories, ancient art, and the gear of famous champions.

### Silver Dragon Lairs

Silver dragons typically lair in picturesque mountain retreats or on sculpted cloud "islands."
## Statblock

```statblock
"name": "Silver Dragon Wyrmling (XMM)"
"size": "Medium"
"type": "dragon"
"subtype": "metallic"
"alignment": "Lawful Good"
"ac": !!int "17"
"hp": !!int "45"
"hit_dice": "6d8 + 18"
"modifier": !!int "2"
"stats":
  - !!int "19"
  - !!int "10"
  - !!int "17"
  - !!int "12"
  - !!int "11"
  - !!int "15"
"speed": "30 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "2"
  - "wisdom": !!int "2"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+2"
"damage_immunities": "cold"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., [[senses#Darkvision|Darkvision]]\
  \ 60 ft., passive Perception 14"
"languages": "Draconic"
"cr": "2"
"actions":
  - "desc": "The dragon makes two Rend attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 9 (1d10 + 4) Piercing\
      \ damage."
    "name": "Rend"
  - "desc": "*Constitution Saving Throw:* DC 13, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 18 (4d8) Cold damage. *Success:* Half damage."
    "name": "Cold Breath (Recharge 5-6)"
  - "desc": "*Constitution Saving Throw:* DC 13, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *1St Failure:* The target has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition until the end of its next turn, when it repeats the save. *2Nd Failure:*\
      \ The target has the [[conditions#Paralyzed|Paralyzed]] condition,\
      \ and it repeats the save at the end of each of its turns, ending the effect\
      \ on itself on a success. After 1 minute, it succeeds automatically."
    "name": "Paralyzing Breath"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/silver-dragon-wyrmling-xmm.webp"
```
^statblock