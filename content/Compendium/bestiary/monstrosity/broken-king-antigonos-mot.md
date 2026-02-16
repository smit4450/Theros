---
title: Broken King Antigonos
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Broken King Antigonos"]
---
# Broken King Antigonos
*Source: Mythic Odysseys of Theros p. 189*  

He is old and decrepit, garbed in ancient finery worn to tatters. A dented crown rests on his brow, and one of his horns ends in a jagged stump. He drags a rusty greataxe in the dirt, and tied to his back is a 30-pound, clay amphora painted with images of warring hoplites—all of whom have had horns crudely painted on them to make them look like minotaurs. The broad-mouthed amphora is large enough to hold roughly 55 gallons of wine.

He claims that he was a great king who was cursed by Mogis after he defied his war advisors by making his sickly but beloved child his heir. He was cast out and has since become tragically obsessed with finding a worthy heir.
```statblock
"name": "Broken King Antigonos (MOT)"
"size": "Large"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "38"
"hit_dice": "9d10 + 27"
"modifier": !!int "0"
"stats":
  - !!int "18"
  - !!int "11"
  - !!int "16"
  - !!int "6"
  - !!int "16"
  - !!int "9"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+7"
"senses": "[[senses#Darkvision|darkvision]] 60 ft., passive Perception\
  \ 17"
"languages": "Abyssal"
"cr": "3"
"traits":
  - "desc": "If Antigonos moves at least 10 feet straight toward a target and then\
      \ hits it with a gore attack on the same turn, the target takes an extra 9 (2d8)\
      \ piercing damage. If the target is a creature, it must succeed on a DC 14 Strength\
      \ saving throw or be pushed up to 10 feet away and knocked [[conditions#Prone|prone]]."
    "name": "Charge"
  - "desc": "Antigonos can perfectly recall any path he has traveled."
    "name": "Labyrinthine Recall"
  - "desc": "At the start of his turn, Antigonos can gain advantage on all melee weapon\
      \ attack rolls he makes during that turn, but attack rolls against him have\
      \ advantage until the start of his next turn."
    "name": "Reckless"
  - "desc": "Antigonos has disadvantage on his attack rolls."
    "name": "Decrepit State"
"actions":
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 17\
      \ (2d12 + 4) slashing damage."
    "name": "Greataxe"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 13\
      \ (2d8 + 4) piercing damage."
    "name": "Gore"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one Medium or smaller\
      \ creature. *Hit:* 8 (1d8 + 4) bludgeoning damage. If there is not already\
      \ a creature inside the amphora, the target is [[conditions#Restrained|restrained]]\
      \ inside. As an action, the [[conditions#Restrained|restrained]]\
      \ creature can make a DC 14 Dexterity ([[skills#Acrobatics|Acrobatics]])\
      \ check, escaping from the amphora on a success. The effect also ends if the\
      \ amphora is destroyed. The amphora has AC 8, 20 hit points, and immunity to\
      \ poison and psychic damage."
    "name": "Amphora"
"source":
  - "MOT"
"image": "Compendium/bestiary/monstrosity/token/broken-king-antigonos-mot.webp"
```
^statblock