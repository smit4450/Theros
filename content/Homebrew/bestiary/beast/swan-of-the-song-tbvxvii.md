---
title: Swan of the Song
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxvii
- monster/cr/1-8
- monster/size/m
- monster/type/beast
statblock: inline
aliases: ["Swan of the Song"]
---
# Swan of the Song
*Source: Theros Bestiary TBVXVII*  

<blockquote><small>“The most enlightened mages create beauty from violence.”

—Medomai the Ageless</small></blockquote>
One way to counter a spell is to turn it into a bird.

![Swan of the Song](Homebrew/bestiary/beast/img/swan-of-the-song.webp#right)  

```statblock
"name": "Swan of the Song (TBVXVII)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"ac_class": "natural armor"
"hp": !!int "12"
"hit_dice": "2d8 + 4"
"modifier": !!int "1"
"stats":
  - !!int "14"
  - !!int "12"
  - !!int "14"
  - !!int "2"
  - !!int "10"
  - !!int "14"
"speed": "20 ft., fly 50 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+4"
  - "name": "[[skills#Performance|Performance]]"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": ""
"cr": "1/8"
"traits":
  - "desc": "The swan has [[advantage-xphb|Advantage]] on Wisdom (Perception) checks that rely on hearing."
    "name": "Keen Hearing"
  - "desc": "The swan has glowing patterns on its skin that take the shape of defensive runes, granting it [[advantage-xphb|Advantage]] on saving throws against spells and other magical effects."
    "name": "Bioluminescent Markings"
"actions":
  - "desc": "The swan makes two attacks: one with its bite and one with its wings."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) piercing damage."
    "name": "Bite"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 4 (1d4 + 2) bludgeoning damage."
    "name": "Wings"
"source":
  - "TBVXVII"
"image": "Homebrew/bestiary/beast/token/swan-of-the-song-tbvxvii.webp"
```
^statblock