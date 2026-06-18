---
title: Galaia
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvi
- monster/cr/5
- monster/size/l
- monster/type/construct
statblock: inline
aliases: ["Galaia"]
---
# Galaia
*Source: Theros Bestiary TBVI*  

Galaia, the horizon chimera, was forged by Purphoros as a gift to Thassa. It was given sight by Thassa. Purphoros commanded it to run until it found his lost sword. It could run faster than Nylea's arrows could fly.

It has the form of an ibis-headed stag with an ibis's wings.

<blockquote>"Do not try to make sense of the chimera.. Impossibility is its habitat." - Kydele, prophet of Kruphix</blockquote>

<b><big>Anvilwroughts</big></b>
The first anvilwroughts were created by the god of the forge, Purphoros. He gave the secret of breathing life into these metal creatures to his most devoted followers so they could mimic his works and invent new forms at their own forges.

Some anvilwroughts are vigilant guardians at holy shrines, others serve as familiars and messengers, and a few were created to emulate beauty found among the animals of the mortal world. Each exhibits abilities suited to its role, with some behaving like companionable creatures or stoic guardians.

A few extremely rare and valuable anvilwroughts were crafted by the hand of Purphoros himself. A number of these magnificent creations are now heirlooms of monarchs; others are lost to the sands of time or are guarded by ancient monsters.

<b><i>Constructed Nature</i></b>. An anvilwrought doesn’t require air, food, drink, or sleep.

![Galaia](Homebrew/bestiary/construct/img/galaia.webp#right)  

```statblock
"name": "Galaia (TBVI)"
"size": "Large"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "40"
"hit_dice": "5d12 + 10"
"modifier": !!int "3"
"stats":
  - !!int "19"
  - !!int "16"
  - !!int "14"
  - !!int "3"
  - !!int "14"
  - !!int "1"
"speed": "325 ft., fly 60 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
"damage_immunities": "fire, poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]], [[conditions#Paralyzed|paralyzed]], [[conditions#Petrified|petrified]], [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception 10"
"languages": "Understands Celestial but can't speak"
"cr": "5"
"traits":
  - "desc": "If Galaia moves at least 20 feet straight toward a target and then hits it with a hooves attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Charge"
  - "desc": "Galaia can take the Disengage or Dash action as a bonus action on each of her turns. Galaia ignores difficult terrain, and magical effects can't reduce her speed or cause her to be [[conditions#Restrained|restrained]]. She can spend 5 feet of movement to escape from nonmagical restraints or being [[conditions#Grappled|grappled]]. When Galaia is [[conditions#Prone|prone]], standing up only uses 5 feet of her movement."
    "name": "Faster than Nylea's Arrow"
  - "desc": "Galaia must move on each of its turns. If it discovers the location of the Godsend, it must spend its turns trying to move within 15 feet of Purphoros, whereupon she tells him this information. After that, Galaia may act freely as if she did not have this ability."
    "name": "Purphoros's Charge"
  - "desc": "Galaia has [[advantage-xphb|Advantage]] on Wisdom (perception) checks that rely on sight."
    "name": "Keen Sight"
  - "desc": "Galaia can move in and out of a Medium or smaller creature's space. If it would, it uses a bonus action to attack that creature with its hooves. That creature must succeed on a DC 14 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the creature succeeds, Galaia can't enter that space and must end its turn immediately. If Galaia stops on top of that creature, that creature becomes [[conditions#Restrained|restrained]] until Galaia moves off it (escape DC 14)."
    "name": "Trample"
"actions":
  - "desc": "Galaia makes two attacks: one with her hooves and one with her beak."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one [[conditions#Prone|prone]] creature. Hit: 22 (4d8 + 4) bludgeoning damage."
    "name": "Hooves"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) piercing damage."
    "name": "Beak"
"source":
  - "TBVI"
"image": "Homebrew/bestiary/construct/token/galaia-tbvi.webp"
```
^statblock