---
title: Aphemia
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Aphemia"]
---
# Aphemia
*Source: Mythic Odysseys of Theros p. 226*  

![](Compendium/bestiary/monstrosity/img/aphemia.webp#right|850)  
The notorious Nyxborn harpy Aphemia prowls the marshy wastes around the necropolis of Asphodel. Her shrill songs enthrall the necropolis's undead inhabitants, which she leads on raids to waylay unsuspecting travelers and settlements.

Cruel, corpse-eating creatures, harpies endlessly seek their next meal, careless of whether it comes from the living or the dead. With equal zeal, these vicious scavengers set upon travelers or claw open fresh graves, stripping bodies of riches and flesh. Then they carry back any treasures or appealing bones they find to reeking nests situated in cramped caves or rotten trees.
```statblock
"name": "Aphemia (MOT)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "52"
"hit_dice": "8d8 + 16"
"modifier": !!int "3"
"stats":
  - !!int "13"
  - !!int "16"
  - !!int "15"
  - !!int "13"
  - !!int "14"
  - !!int "16"
"speed": "20 ft., fly 50 ft."
"saves":
  - "dexterity": !!int "6"
  - "charisma": !!int "6"
"skillsaves":
  - "name": "[Arcana](Compendium/rules/skills.md#Arcana)"
    "desc": "+4"
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+6"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+5"
"damage_resistances": "necrotic"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened)"
"senses": "[darkvision](Compendium/rules/senses.md#Darkvision) 120 ft., passive Perception\
  \ 15"
"languages": "Common"
"cr": "5"
"traits":
  - "desc": "If Aphemia fails a saving throw, she can choose to succeed instead."
    "name": "Legendary Resistance (2/Day)"
  - "desc": "Aphemia has advantage on saving throws against spells and other magical\
      \ effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "Aphemia makes two attacks: one with her bite and one with her claws."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 8\
      \ (2d4 + 3) piercing damage plus 13 (3d8) necrotic damage."
    "name": "Bite"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 10\
      \ (2d6 + 3) slashing damage."
    "name": "Claws"
  - "desc": "Aphemia shrieks a cacophony of magical sounds. Each humanoid within 120\
      \ feet of her must succeed on a DC 14 Wisdom saving throw or be [frightened](Compendium/rules/conditions.md#Frightened)\
      \ of her until the song ends. A [frightened](Compendium/rules/conditions.md#Frightened)\
      \ creature takes 7 (2d6) psychic damage at the start of its turn while Aphemia\
      \ is singing. A [frightened](Compendium/rules/conditions.md#Frightened) creature\
      \ can repeat the saving throw at the end of each of its turns, ending the effect\
      \ on itself on a success. If a creature's saving throw is successful or the\
      \ effect ends for it, the creature is immune to Aphemia's Discordant Song for\
      \ the next 24 hours. Aphemia must take a bonus action on her subsequent turns\
      \ to continue singing. She can stop singing at any time. The song ends if Aphemia\
      \ is [incapacitated](Compendium/rules/conditions.md#Incapacitated) or dies."
    "name": "Discordant Song"
  - "desc": "Aphemia intones a low, growling magical melody. Every undead within 300\
      \ feet of her must succeed on a DC 14 Wisdom saving throw or fall under her\
      \ control until the song ends. Aphemia must take a bonus action on her subsequent\
      \ turns to continue singing, and she can mentally command the undead under her\
      \ control as part of the same bonus action. She can stop singing at any time.\
      \ The song ends if Aphemia is [incapacitated](Compendium/rules/conditions.md#Incapacitated)\
      \ or dies."
    "name": "Grave Calling Song"
"source":
  - "MOT"
"image": "Compendium/bestiary/monstrosity/token/aphemia-mot.webp"
```
^statblock