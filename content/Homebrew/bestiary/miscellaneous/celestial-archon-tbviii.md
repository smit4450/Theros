---
title: Celestial Archon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbviii
- monster/cr/12
- monster/size/m
- monster/type/miscellaneous
statblock: inline
aliases: ["Celestial Archon"]
---
# Celestial Archon
*Source: Theros Bestiary TBVIII*  



![Celestial Archon](Homebrew/bestiary/miscellaneous/img/celestial-archon.webp#right)  

```statblock
"name": "Celestial Archon (TBVIII)"
"size": "Medium"
"type": "5th-level transmutation celestial"
"alignment": "Lawful Good"
"ac": !!int "18"
"ac_class": "plate"
"hp": !!int "128"
"hit_dice": "16d8 + 64"
"modifier": !!int "3"
"stats":
  - !!int "20"
  - !!int "17"
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
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]], [[conditions#Frightened|frightened]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception 10"
"languages": "All"
"cr": "12"
"traits":
  - "desc": "The archon's innate spellcasting ability is Wisdom (spell save DC 17, +9 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: [[command-xphb|Command]], [[guiding-bolt-xphb|Guiding Bolt]], [[spare-the-dying-xphb|Spare The Dying]] 1/day: _crusader's mantle_, [[spirit-guardians-xphb|Spirit Guardians]]"
    "name": "Innate Spellcasting"
  - "desc": "The archon's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "If the archon isn’t mounted, it can use a bonus action to magically teleport onto the creature serving as its mount, provided the archon and its mount are on the same plane of existence. When it teleports, the archon appears astride the mount, along with any equipment it is wearing or carrying. While mounted and not [[conditions#Incapacitated|incapacitated]], the archon can’t be surprised, and both it and its mount have [[advantage-xphb|Advantage]] on Dexterity saving throws. If the archon is reduced to 0 [[hit-points-xphb|Hit Points]] while riding its mount, the mount is reduced to 0 [[hit-points-xphb|Hit Points]] as well."
    "name": "Mount"
  - "desc": "In addition to being a creature, the archon is a 7th-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The archon glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "The archon makes two attacks with its radiant spear."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) piercing damage plus 10 (3d6) radiant damage."
    "name": "Radiant Spear"
"legendary_actions":
  - "desc": "The archon makes a radiant spear attack or casts guiding bolt."
    "name": "Attack"
  - "desc": "The archon makes a radiant spear attack, and then its mount can use its reaction to make a melee weapon attack."
    "name": "Coordinated Assault (Costs 2 Actions)"
"source":
  - "TBVIII"
"image": "Homebrew/bestiary/miscellaneous/token/celestial-archon-tbviii.webp"
```
^statblock