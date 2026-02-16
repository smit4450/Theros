---
title: Silent Sentinel
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Silent Sentinel"]
---
# Silent Sentinel
*Source: Theros Bestiary TBVVI*  

<blockquote><small>It serves a justice higher than the whims of the gods.</small></blockquote>

![Silent Sentinel](Compendium/bestiary/celestial/img/silent-sentinel.webp#right|850)  

```statblock
"name": "Silent Sentinel (TBVVI)"
"size": "Medium"
"type": "celestial"
"subtype": "archon"
"alignment": "Lawful Good"
"ac": !!int "18"
"ac_class": "plate"
"hp": !!int "170"
"hit_dice": "17d8 + 102"
"modifier": !!int "4"
"stats":
  - !!int "19"
  - !!int "18"
  - !!int "22"
  - !!int "15"
  - !!int "19"
  - !!int "18"
"speed": "30 ft."
"saves":
  - "strength": !!int "9"
  - "constitution": !!int "11"
  - "wisdom": !!int "9"
  - "charisma": !!int "9"
"skillsaves":
  - "name": "[[skills#History|History]]"
    "desc": "+7"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+9"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+9"
"damage_immunities": "thunder"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]], [[conditions#Frightened|frightened]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception 10"
"languages": "All, but chooses to remain silent"
"cr": "8"
"traits":
  - "desc": "If the sentinel isn’t mounted, it can use a bonus action to magically teleport onto the creature serving as its mount, provided the sentinel and its mount are on the same plane of existence. When it teleports, the sentinel appears astride the mount, along with any equipment it is wearing or carrying. While mounted and not [[conditions#Incapacitated|incapacitated]], the sentinel can’t be surprised, and both it and its mount have [[advantage-xphb|Advantage]] on Dexterity saving throws. If the sentinel is reduced to 0 [[hit-points-xphb|Hit Points]] while riding its mount, the mount is reduced to 0 [[hit-points-xphb|Hit Points]] as well."
    "name": "Mount"
"actions":
  - "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) slashing damage plus 13 (2d12) radiant damage."
    "name": "Ashen Blade"
  - "desc": "Ranged Spell Attack: +9 to hit, range 120 ft., one creature. Hit: 22 (4d10) necrotic damage, and the target can’t regain [[hit-points-xphb|Hit Points]] until the start of the sentinel’s next turn."
    "name": "Bolt of Ash"
"reactions":
  - "desc": "Immediately after the sentinel attacks, roll a d100. The number rolled determine the effect: 1-48: No effect. 50-85: The sentinel summons a **hopeful eidolon**. 86-98: The sentinel summons a **ghostblade eidolon**. 99: The sentinel summons a **spirit of the labyrinth**. 100: The sentinel summons an **eidolon of countless battles**. If a creature is summoned this way, the creature acts as an ally to its summoner and to other creatures its summoner summons."
    "name": "Justice for the Fallen"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/celestial/token/silent-sentinel-tbvvi.webp"
```
^statblock