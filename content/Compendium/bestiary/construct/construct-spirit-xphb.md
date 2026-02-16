---
title: Construct Spirit
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xphb
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Construct Spirit"]
---
# Construct Spirit
*Source: Player's Handbook (2024) p. 324*  

![](Compendium/bestiary/construct/img/construct-spirit.webp#center)  
```statblock
"name": "Construct Spirit (XPHB)"
"size": "Medium"
"type": "construct"
"alignment": "Neutral"
"ac_class": "13 + the spell's level"
"modifier": !!int "0"
"stats":
  - !!int "18"
  - !!int "10"
  - !!int "18"
  - !!int "14"
  - !!int "11"
  - !!int "5"
"speed": "30 ft."
"damage_resistances": "poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]], [[conditions#Paralyzed|paralyzed]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 10"
"languages": "Understands the languages you know"
"traits":
  - "desc": "A creature that hits the spirit with a melee attack or that starts its\
      \ turn in a grapple with the spirit takes 1d10 Fire damage."
    "name": "Heated Body (Metal Only)"
  - "desc": "When a creature starts its turn within 10 feet of the spirit, the spirit\
      \ can target it with magical energy if the spirit can see it. *Wisdom Saving\
      \ Throw:* DC equals your spell save DC, the target. *Failure:* Until the start\
      \ of its next turn, the target can't make [[actions#Opportunity%20Attack|Opportunity Attacks]],\
      \ and its Speed is halved."
    "name": "Stony Lethargy (Stone Only)"
"actions":
  - "desc": "The spirit makes a number of Slam attacks equal to half this spell's\
      \ level (round down)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d8 + 4 + the spell's level Bludgeoning damage."
    "name": "Slam"
"reactions":
  - "desc": "Trigger: The spirit takes damage from a creature. _Response:_ The spirit\
      \ makes a Slam attack against that creature if possible, or the spirit moves\
      \ up to half its Speed toward that creature without provoking [[actions#Opportunity%20Attack|Opportunity Attacks]]."
    "name": "Berserk Lashing (Clay Only)"
"source":
  - "XPHB"
"image": "Compendium/bestiary/construct/token/construct-spirit-xphb.webp"
```
^statblock