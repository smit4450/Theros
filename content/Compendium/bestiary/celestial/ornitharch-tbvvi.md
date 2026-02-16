---
title: Ornitharch
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Ornitharch"]
---
# Ornitharch
*Source: Theros Bestiary TBVVI*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more archon cultists might be nearby who will pay tribute.
<li>One or more aerie worshipers might be nearby who will worship the ornitharch's summoned doves.
<li>A quest goal might involve securing a dove.
<li>A quest goal might involve vanquishing the archon.
<li>The archon might be helpful in vanquishing a nearby foe.

![Ornitharch](https://img.scryfall.com/cards/art_crop/front/f/9/f95a0bf4-10c7-4afa-8cf6-e31196cc2bd5.jpg?1578451659#right)  

```statblock
"name": "Ornitharch (TBVVI)"
"size": "Medium"
"type": "celestial"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "plate"
"hp": !!int "112"
"hit_dice": "16d8 + 48"
"modifier": !!int "3"
"stats":
  - !!int "17"
  - !!int "17"
  - !!int "17"
  - !!int "15"
  - !!int "21"
  - !!int "17"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "8"
  - "charisma": !!int "6"
  - "strength": !!int "6"
  - "constitution": !!int "6"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+8"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+8"
  - "name": "[[skills#History|History]]"
    "desc": "+5"
  - "name": "[[skills#Animal Handling|Animal Handling]]"
    "desc": "+8"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]], [[conditions#Frightened|frightened]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception 10"
"languages": "all"
"cr": "5"
"traits":
  - "desc": "The ornitharch's innate spellcasting ability is Charisma (spell save DC 13, +6 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: [[true-strike-xphb|True Strike]] 3/day: _animal messenger_, [[conjure-animals-xphb|Conjure Animals]] (doves), [[speak-with-animals-xphb|Speak With Animals]]"
    "name": "Innate Spellcasting"
  - "desc": "If the ornitharch isn’t controlling a vehicle, it can use a bonus action to magically teleport into its vehicle, provided the ornitharch and its vehicle are on the same plane of existence. When it teleports, the ornitharch appears in the vehicle, along with any equipment it is wearing or carrying. While controlling the vehicle and not [[conditions#Incapacitated|incapacitated]], the ornitharch can’t be surprised, and both it and its vehicle have [[advantage-xphb|Advantage]] on Dexterity saving throws. If the ornitharch is reduced to 0 [[hit-points-xphb|Hit Points]] while controlling its vehicle, the vehicle is reduced to 0 [[hit-points-xphb|Hit Points]] as well."
    "name": "Pilot"
  - "desc": "The ornitharch has proficiency with flying vehicles."
    "name": "Vehicle Proficiency"
"actions":
  - "desc": "_Melee or Ranged Weapon Attack:_ +6 to hit, reach 5 ft. or range 20/60 ft., one target. _Hit:_ 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing damage if used with two hands to make a melee attack."
    "name": "Spear"
"reactions":
  - "desc": "Immediately after initiative rolls in which the ornitharch participates, it demands tribute from a creature it can see. That creature may bow, genuflect, salute, or perform a similar gesture as a bonus action. If tribute is paid: Until the end of combat, the ornitharch gains a +2 bonus to damage rolls and Strength and Dexterity checks, and 9 (2d8) temporary [[hit-points-xphb|Hit Points]]. If tribute isn't paid: The ornitharch summons 9 (2d8) **doves** that appear in unoccupied spaces that the ornitharch can see within 120 feet of itself. The summoned doves act as allies to their summoner and its allies."
    "name": "Demand Tribute"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/celestial/token/ornitharch-tbvvi.webp"
```
^statblock