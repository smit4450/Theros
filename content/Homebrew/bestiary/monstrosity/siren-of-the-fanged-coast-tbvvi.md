---
title: Siren of the Fanged Coast
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvvi
- monster/cr/2
- monster/size/m
- monster/type/monstrosity
statblock: inline
aliases: ["Siren of the Fanged Coast"]
---
# Siren of the Fanged Coast
*Source: Theros Bestiary TBVVI*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more siren cultists might be nearby who will pay tribute.
<li>The siren could prove helpful or detrimental in vanquishing a larger beast.
<li>A quest goal might involve saving a creature that is near the siren.
<li>A quest goal might involve vanquishing the siren.

![Siren of the Fanged Coast](Homebrew/bestiary/monstrosity/img/siren-of-the-fanged-coast.webp#right)  

```statblock
"name": "Siren of the Fanged Coast (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "11"
"hp": !!int "35"
"hit_dice": "7d8 + 7"
"modifier": !!int "1"
"stats":
  - !!int "12"
  - !!int "13"
  - !!int "12"
  - !!int "7"
  - !!int "10"
  - !!int "13"
"speed": "20 ft., fly 40 ft."
"condition_immunities": "[[conditions#Charmed|charmed]]"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "2"
"actions":
  - "desc": "The siren makes two attacks: one with its claws and one with its club."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage."
    "name": "Claws"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage."
    "name": "Club"
  - "desc": "The siren sings a magical melody. Every humanoid and giant within 300 ft. of the siren that can hear the song must succeed on a DC 11 Wisdom saving throw or be [[conditions#Charmed|charmed]] until the song ends. The siren must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the siren is [[conditions#Incapacitated|incapacitated]]. While [[conditions#Charmed|charmed]] by the siren, a target is [[conditions#Incapacitated|incapacitated]] and ignores the songs of other sirens. If the [[conditions#Charmed|charmed]] target is more than 5 ft. away from the siren, the must move on its turn toward the siren by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the siren, a target can repeat the saving throw. A creature can also repeat the saving throw at the end of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this siren's song for the next 24 hours."
    "name": "Luring Song"
"reactions":
  - "desc": "Immediately after initiative rolls in which the siren participates, it demands tribute from a creature it can see. That creature may bow, genuflect, salute, or perform a similar gesture as a bonus action. If tribute is paid: Until the end of combat, the siren gains a +3 bonus to damage rolls and Strength and Dexterity checks, and 17 (3d8) temporary [[hit-points-xphb|Hit Points]]. If tribute isn't paid: The creature must succeed on a DC 11 Wisdom saving throw or be [[conditions#Charmed|charmed]] by the siren for 1 round."
    "name": "Demand Tribute"
"source":
  - "TBVVI"
"image": "Homebrew/bestiary/monstrosity/token/siren-of-the-fanged-coast-tbvvi.webp"
```
^statblock