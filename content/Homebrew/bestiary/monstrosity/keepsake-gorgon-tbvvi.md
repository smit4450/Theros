---
title: Keepsake Gorgon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvvi
- monster/cr/5
- monster/size/m
- monster/type/monstrosity
statblock: inline
aliases: ["Keepsake Gorgon"]
---
# Keepsake Gorgon
*Source: Theros Bestiary TBVVI*  

Some gorgons are collectors, making "sculpture" gardens of their victims.

![Keepsake Gorgon](Homebrew/bestiary/monstrosity/img/keepsake-gorgon.webp#right)  

```statblock
"name": "Keepsake Gorgon (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"subtype": "medusa"
"alignment": "Lawful Evil"
"ac": !!int "15"
"hp": !!int "99"
"hit_dice": "11d8 + 55"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "15"
  - !!int "20"
  - !!int "12"
  - !!int "13"
  - !!int "15"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+4"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+3"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
  - "name": "[[skills#Medicine|Medicine]]"
    "desc": "+3"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Common"
"cr": "5"
"traits":
  - "desc": "The gorgon is an expert in extending its own life to immortality, and it enjoys a high-stake deal. If a creature successfully restrains the gorgon, it will share one of its medicinal secrets in exchange for its freedom."
    "name": "Gorgon's Trial"
  - "desc": "The gorgon doesn't require food, drink, or sleep."
    "name": "Immortal Nature"
  - "desc": "As soon as a creature within 30 feet of the gorgon sees the gorgon's face, it may make a DC 14 Constitution saving throw. On a success, that creature may use a reaction to shield its eyes or avert them. If the saving throw fails by 5 or more, or if the creature is unable to react, the creature is instantly [[conditions#Petrified|petrified]]. Otherwise, a creature that fails the save begins to turn to stone and is [[conditions#Restrained|restrained]]. The [[conditions#Restrained|restrained]] creature must repeat the saving throw at the end of its next turn, becoming [[conditions#Petrified|petrified]] on a failure or ending the effect on a success. The petrification lasts until the creature is unpetrified by a god.If the gorgon sees its own face reflected on a polished surface within 30 ft. of it and in an area of bright light, the gorgon is, due to its curse, affected by its own visage.This trait has no effect if the gorgon's face is not its normal flesh state. The trait remains active even if the gorgon is [[conditions#Incapacitated|incapacitated]], killed, and even beheaded."
    "name": "Petrifying Visage"
  - "desc": "If the gorgon is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, it sheds its skin, regains 15 (1d20+5) [[hit-points-xphb|Hit Points]], and moves up to its speed without provoking opportunity attacks."
    "name": "Shed Skin (Mythic Trait; Recharges after a Short or Long Rest)"
"actions":
  - "desc": "The gorgon makes either three melee attacks—one with its snake hair, one to constrict, and one with its shortsword—or two ranged attacks with its longbow."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +2 to hit, reach 10 ft., one target. Hit: 7 (2d6) bludgeoning damage, and the target is [[conditions#Grappled|grappled]] (escape DC 10) if it is a Large or smaller creature. Until this grapple ends, the target is [[conditions#Restrained|restrained]], and the gorgon can’t constrict another target."
    "name": "Constrict"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage plus 14 (4d6) poison damage."
    "name": "Snake Hair"
  - "desc": "Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage plus 7 (2d6) poison damage."
    "name": "Longbow"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) piercing damage."
    "name": "Shortsword"
"legendary_actions":
  - "desc": "**Mythic Actions**If the gorgon's mythic trait is active, it can use the options below as legendary actions for 1 hour after using Shed Skin. **Look at Me (Costs 3 Actions).** The gorgon can force a sighted creature it has [[conditions#Grappled|grappled]] to see its face and be affected by its visage."
    "name": ""
"source":
  - "TBVVI"
"image": "Homebrew/bestiary/monstrosity/token/keepsake-gorgon-tbvvi.webp"
```
^statblock