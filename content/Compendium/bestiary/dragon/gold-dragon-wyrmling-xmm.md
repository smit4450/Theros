---
title: Gold Dragon Wyrmling
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/3
- monster/environment/forest
- monster/environment/grassland
- monster/size/medium
- monster/type/dragon/metallic
statblock: inline
aliases: ["Gold Dragon Wyrmling"]
---
# Gold Dragon Wyrmling
*Source: Monster Manual (2024) p. 144. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/gold-dragon-wyrmling.webp#right|850)  
Gold dragon wyrmlings learn much from their elders, then head off to save the world. Idealistic and curious, these wyrmlings seek to right obvious wrongs and make friends among those they aid.

## Gold Dragons

*Dragons of Hope and Majesty*

- **Habitat.** Forest, Grassland  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Gold dragons work to make the world a better place. The most powerful of the metallic dragons, these awe-inspiring dragons strive to protect that which is good and bend fate toward a brighter future. Their kind dispositions don't prevent gold dragons from engaging in combat when necessary, though, and they exhale brilliant flames and weakening magic to rout their foes.

Gold dragons favor grasslands and pristine forests, frequently dwelling near awe-inspiring natural wonders or guarding monuments from ancient civilizations. In their lairs, gold dragons hoard coins and gems, but they frequently put their treasure to use in pursuit of greater goals. They often use their riches to buy rare lore books, pay informants, or patronize idealistic adventurers.

### Gold Dragon Lairs

Gold dragons make their homes in places of natural and magical wonder.
## Statblock

```statblock
"name": "Gold Dragon Wyrmling (XMM)"
"size": "Medium"
"type": "dragon"
"subtype": "metallic"
"alignment": "Lawful Good"
"ac": !!int "17"
"hp": !!int "60"
"hit_dice": "8d8 + 24"
"modifier": !!int "4"
"stats":
  - !!int "19"
  - !!int "14"
  - !!int "17"
  - !!int "14"
  - !!int "11"
  - !!int "16"
"speed": "30 ft., fly 60 ft., swim 30 ft."
"saves":
  - "dexterity": !!int "4"
  - "wisdom": !!int "2"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
"damage_immunities": "fire"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., [[senses#Darkvision|Darkvision]]\
  \ 60 ft., passive Perception 14"
"languages": "Draconic"
"cr": "3"
"traits":
  - "desc": "The dragon can breathe air and water."
    "name": "Amphibious"
"actions":
  - "desc": "The dragon makes two Rend attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 9 (1d10 + 4) Slashing\
      \ damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 13, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 22 (4d10) Fire damage. *Success:* Half damage."
    "name": "Fire Breath (Recharge 5-6)"
  - "desc": "*Strength Saving Throw:* DC 13, each creature that isn't currently affected\
      \ by this breath in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* The target has [[disadvantage-xphb|Disadvantage]]\
      \ on Strength-based [[d20-test-xphb|D20 Tests]]\
      \ and subtracts 2 (1d4) from its damage rolls. It repeats the save at the\
      \ end of each of its turns, ending the effect on itself on a success. After\
      \ 1 minute, it succeeds automatically."
    "name": "Weakening Breath"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/gold-dragon-wyrmling-xmm.webp"
```
^statblock