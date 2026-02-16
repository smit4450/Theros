---
title: Stormbreath Dragon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/23
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Stormbreath Dragon"]
---
# Stormbreath Dragon
*Source: Theros Bestiary TBVVI*  



![Stormbreath Dragon](Compendium/bestiary/dragon/img/stormbreath-dragon.webp#right|850)  

```statblock
"name": "Stormbreath Dragon (TBVVI)"
"size": "Gargantuan"
"type": "dragon"
"alignment": "Unaligned"
"ac": !!int "22"
"hp": !!int "468"
"hit_dice": "26d20 + 208"
"modifier": !!int "0"
"stats":
  - !!int "29"
  - !!int "10"
  - !!int "27"
  - !!int "18"
  - !!int "17"
  - !!int "21"
"speed": "40 ft., fly 80 ft., burrow 40 ft."
"saves":
  - "dexterity": !!int "7"
  - "constitution": !!int "15"
  - "wisdom": !!int "10"
  - "charisma": !!int "12"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+17"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+7"
"damage_immunities": "lightning, radiant"
"senses": "[[senses#Blindsight|Blindsight]] 60 ft., [[senses#Darkvision|Darkvision]] 120 ft., passive Perception 10"
"languages": "Draconic, Common (barely)"
"cr": "23"
"traits":
  - "desc": "The dragon has [[advantage-xphb|Advantage]] on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "When the dragon is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, the damage creates tears in its hide, revealing its hearts. The dragon has three hearts in its chest. A heart has an AC of 22 and 120 [[hit-points-xphb|Hit Points]]. It is immune to lightning and radiant damage and to all conditions. If it is forced to make a saving throw, treat its ability scores as 10 (+0). The dragon dies when all the hearts are destroyed."
    "name": "Hearts of the Dragon (Mythic Trait; Recharges after a Short or Long Rest)"
"actions":
  - "desc": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 20 (2d10 + 9) piercing damage plus 11 (2d10) lightning damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 16 (2d6 + 9) slashing damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +16 to hit, reach 20 ft., one target. Hit: 18 (2d8 + 9) bludgeoning damage."
    "name": "Tail"
  - "desc": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 20 Wisdom saving throw or become [[conditions#Frightened|frightened]] for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."
    "name": "Frightful Presence"
  - "desc": "The dragon exhales lightning in a 120-foot line that is 10 feet wide. Each creature in that line must make a DC 23 Dexterity saving throw, taking 88 (16d10) lightning damage on a failed save, or half as much damage on a successful one."
    "name": "Lightning Breath (Recharge 5-6)"
"legendary_actions":
  - "desc": "The dragon makes a Wisdom (Perception) check."
    "name": "Detect"
  - "desc": "The dragon makes a tail attack."
    "name": "Tail Attack"
  - "desc": "The dragon beats its wings. Each creature within 15 ft. of the dragon must succeed on a DC 24 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked [[conditions#Prone|prone]]. The dragon can then fly up to half its flying speed."
    "name": "Wing Attack (Costs 2 Actions)"
  - "desc": "**Mythic Actions**If the dragon's mythic trait is active, it can use the options below as legendary actions for 1 hour after using Hearts of the Dragon. **_Breathe Lightning._** The dragon makes a lightning breath attack."
    "name": ""
"source":
  - "TBVVI"
"image": "Compendium/bestiary/dragon/token/stormbreath-dragon-tbvvi.webp"
```
^statblock