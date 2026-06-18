---
title: Vulpine Goliath
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbviv
- monster/cr/3
- monster/size/h
- monster/type/beast
statblock: inline
aliases: ["Vulpine Goliath"]
---
# Vulpine Goliath
*Source: Theros Bestiary TBVIV*  

<small><blockquote>“With a diet of hydras, giants, and massive serpents, anything would get that big.” —Corisande, Setessan hunter</blockquote></small>
The vulpine goliath is a gigantic fox that can never be caught. It feeds on whatever it wants to.

![Vulpine Goliath](Homebrew/bestiary/beast/img/vulpine-goliath.webp#right|850)  

```statblock
"name": "Vulpine Goliath (TBVIV)"
"size": "Huge"
"type": "beast"
"subtype": "fox"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "55"
"hit_dice": "5d12 + 25"
"modifier": !!int "1"
"stats":
  - !!int "22"
  - !!int "12"
  - !!int "21"
  - !!int "4"
  - !!int "14"
  - !!int "7"
"speed": "50 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+2"
"condition_immunities": "[[conditions#Grappled|grappled]], [[conditions#Restrained|restrained]], [[conditions#Paralyzed|paralyzed]], [[conditions#Incapacitated|incapacitated]], [[conditions#Exhaustion|exhaustion]], [[conditions#Charmed|charmed]], [[conditions#Prone|prone]], [[conditions#Stunned|stunned]], [[conditions#Unconscious|unconscious]]"
"senses": "[[senses#Darkvision|Darkvision]] 30 ft., passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "The fox has [[advantage-xphb|Advantage]] on Wisdom (Perception) checks that rely on sight, hearing or smell."
    "name": "Keen Senses"
  - "desc": "If any creature tries to catch the fox, it fails. If a paradox is formed in this way because that creature cannot fail, both that creature and the fox become [[conditions#Petrified|petrified]]."
    "name": "Teumessian"
  - "desc": "The fox can move in and out of a Large or smaller creature's space. If it would, it uses a bonus action to attack that creature with its paw. That creature must succeed on a DC 16 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the creature succeeds, the fox can't enter that space and must end its turn immediately. If the fox stops on top of that creature, that creature becomes [[conditions#Restrained|restrained]] until the fox moves off it (escape DC 16)."
    "name": "Trample"
"actions":
  - "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., 1 target. Hit: 33 (6d8 + 6) piercing damage."
    "name": "Bite"
  - "desc": "_Melee Weapon Attack:_ +8 to hit, reach 5 ft., one target. _Hit:_ 21 (6d4 + 6) bludgeoning damage."
    "name": "Paw"
"source":
  - "TBVIV"
"image": "Homebrew/bestiary/beast/token/vulpine-goliath-tbviv.webp"
```
^statblock