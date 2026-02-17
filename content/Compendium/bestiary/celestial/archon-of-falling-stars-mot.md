---
title: Archon of Falling Stars
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/12
- monster/size/medium
- monster/type/celestial
statblock: inline
aliases: ["Archon of Falling Stars"]
---
# Archon of Falling Stars
*Source: Mythic Odysseys of Theros p. 212*  

![](Compendium/bestiary/celestial/img/archon-of-falling-stars.webp#right|850)  
The epic accounting of the world's earliest histories called *The Cosmogony* recounts the battle between a group of the gods' champions and a mighty archon, which took place at the mysterious eastern edge of the world. Defeated, the falling archon is said to have met the rising sun. But Heliod showed mercy to the penitent archon, who swore to uphold justice and righteousness in the world's wildest places. As a sign of his mercy, Heliod gave the archon a spear that rivaled his own in its brilliance. This was the first archon of falling stars.

The mysterious conquerors known as archons once ruled vast empires. These armored warlords saw themselves as champions of merciless justice, and they ruled with iron fists. But their dominance ultimately came to an end. As the archon overlords toppled, they scattered to the fringes of the world, and their holdings developed into the poleis of today.

Even though the age of archons is long past, many wonder if the few surviving archons might someday attempt to reestablish their empire or if they are truly resigned to their lesser role in the world.
```statblock
"name": "Archon of Falling Stars (MOT)"
"size": "Medium"
"type": "celestial"
"alignment": "Lawful Good"
"ac": !!int "18"
"ac_class": "[[plate-armor-xphb|plate]]"
"hp": !!int "144"
"hit_dice": "17d8 + 68"
"modifier": !!int "2"
"stats":
  - !!int "20"
  - !!int "15"
  - !!int "19"
  - !!int "15"
  - !!int "21"
  - !!int "19"
"speed": "30 ft."
"saves":
  - "strength": !!int "9"
  - "constitution": !!int "8"
  - "wisdom": !!int "9"
  - "charisma": !!int "8"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+6"
  - "name": "[[skills#History|History]]"
    "desc": "+6"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+9"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+9"
"damage_immunities": "radiant"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]]"
"senses": "[[senses#Truesight|truesight]] 120 ft., passive Perception\
  \ 19"
"languages": "all"
"cr": "12"
"traits":
  - "desc": "The archon's spellcasting ability is Wisdom (spell save DC 17, +9 to\
      \ hit with spell attacks). The archon can innately cast the following spells,\
      \ requiring no material components:\n\n**At will:** [[command-xphb|command]],\
      \ [[guiding-bolt-xphb|guiding bolt]], [[spare-the-dying-xphb|spare the dying]]\n\
      \n**1/day each:** [[crusaders-mantle-xphb|crusader's mantle]],\
      \ [[spirit-guardians-xphb|spirit guardians]]"
    "name": "Innate Spellcasting"
  - "desc": "The archon has advantage on saving throws against spells and other magical\
      \ effects."
    "name": "Magic Resistance"
  - "desc": "If the archon isn't mounted, it can use a bonus action to magically teleport\
      \ onto the creature serving as its mount, provided the archon and its mount\
      \ are on the same plane of existence. When it teleports, the archon appears\
      \ astride the mount, along with any equipment it is wearing or carrying. While\
      \ mounted and not [[conditions#Incapacitated|incapacitated]],\
      \ the archon can't be [[conditions#Surprised|surprised]],\
      \ and both it and its mount have advantage on Dexterity saving throws. If the\
      \ archon is reduced to 0 hit points while riding its mount, the mount is reduced\
      \ to 0 hit points as well."
    "name": "Mount"
  - "desc": "If the archon is reduced to 0 hit points, it regains 30 hit points and\
      \ springs back to its feet with a burst of radiance. Each creature of the archon's\
      \ choice within 30 feet of it must succeed on a DC 16 Constitution saving throw,\
      \ or the creature takes 13 (3d8) radiant damage and is [[conditions#Blinded|blinded]]\
      \ until the start of the archon's turn."
    "name": "Radiant Rebirth (Recharges after a Long Rest)"
"actions":
  - "desc": "The archon makes two attacks with its radiant spear."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +9 to hit, reach 10 ft., one target. *Hit:*\
      \ 12 (2d6 + 5) piercing damage plus 10 (3d6) radiant damage."
    "name": "Radiant Spear"
"legendary_description": "Legendary Action Uses: 3. Immediately after another creature's\
  \ turn, the archon of falling stars can expend a use to take one of the following\
  \ actions. The archon of falling stars regains all expended uses at the start of\
  \ each of its turns."
"legendary_actions":
  - "desc": "The archon makes a radiant spear attack or casts [[guiding-bolt-xphb|guiding bolt]]."
    "name": "Attack"
  - "desc": "The archon makes a radiant spear attack, and then its mount can use its\
      \ reaction to make a melee weapon attack."
    "name": "Coordinated Assault (Costs 2 Actions)"
  - "desc": "The archon causes a corpse it can see within 30 feet of it to burst into\
      \ a shower of radiant stars leaving no trace of it behind. Everything it is\
      \ wearing or carrying remains. Each creature within 10 feet of the corpse when\
      \ it bursts must succeed on a DC 16 Dexterity saving throw or take 22 (4d10)\
      \ radiant damage."
    "name": "Return to Nyx (Costs 3 Actions)"
"source":
  - "MOT"
"image": "Compendium/bestiary/celestial/token/archon-of-falling-stars-mot.webp"
```
^statblock