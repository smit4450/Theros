---
title: Shoal Serpent
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxi
- monster/cr/18
- monster/size/g
- monster/type/monstrosity
statblock: inline
aliases: ["Shoal Serpent"]
---
# Shoal Serpent
*Source: Theros Bestiary TBVXXI*  

<small><blockquote>“It’s like a reef that runs aground on ships.”

—Jaby, Silundi Sea nomad</blockquote></small>Introduced to Theros from Zendikar.

![Shoal Serpent](https://img.scryfall.com/cards/art_crop/front/a/4/a4a98047-8e6d-416c-b11d-cc4c2a56b624.jpg?1562615139#right)  

```statblock
"name": "Shoal Serpent (TBVXXI)"
"size": "Gargantuan"
"type": "monstrosity"
"subtype": "serpent"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "12"
  - !!int "20"
  - !!int "2"
  - !!int "7"
  - !!int "12"
"speed": "swim 120 ft."
"saves":
  - "constitution": !!int "10"
  - "wisdom": !!int "3"
"skillsaves":
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+6"
"senses": "passive Perception 10"
"languages": ""
"cr": "18"
"traits":
  - "desc": "When a Huge or smaller creature is bitten by the serpent, or when it is in the serpent's path as it breaches (but before it falls), it must succeed on a DC 13 Dexterity saving throw or be swallowed by the serpent. A swallowed creature is [[conditions#Blinded|blinded]] and [[conditions#Restrained|restrained]], it has total cover against attacks and other effects outside the serpent, and it takes 21 (6d6) acid damage at the start of each of the serpent's turns. If the serpent takes 30 damage or more on a single turn from a creature inside it, the serpent must succeed on a DC 19 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall [[conditions#Prone|prone]] in a space within 10 feet of the serpent. If the serpent dies, a swallowed creature is no longer [[conditions#Restrained|restrained]] by it and can escape from the corpse by using 20 feet of movement, exiting [[conditions#Prone|prone]]."
    "name": "Swallow"
  - "desc": "The serpent can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 50 (10d8 + 5) piercing damage. (See the Swallow trait.)"
    "name": "Bite"
  - "desc": "The serpent breaches at any angle, its head reaching an apex height of 50 ft, arcing back toward the surface. It breaches with its mouth open. It attempts to swallow Huge or smaller creatures that it intercepts this way, and bites Gargantuan creatures. (See the Swallow trait.) It then closes its mouth and falls back into the water."
    "name": "Breach (Recharge 5-6)"
"source":
  - "TBVXXI"
"image": "Compendium/bestiary/monstrosity/token/shoal-serpent-tbvxxi.webp"
```
^statblock