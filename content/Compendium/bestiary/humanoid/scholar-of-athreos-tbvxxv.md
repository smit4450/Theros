---
title: Scholar of Athreos
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxv
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Scholar of Athreos"]
---
# Scholar of Athreos
*Source: Theros Bestiary TBVXXV*  

<small><blockquote>She asks pointed questions of the dead who wait for Athreos, learning of life from those who are about to leave it.</blockquote></small>
The scholar of Athreos is a religious acolyte. She oversees the tithes for the temple of Athreos. Using her necromantic powers, she speaks with those who died without a gold coin, who will exchange any information in return for the coin they desperately need to gain passage into the realm of the dead.

![Scholar of Athreos](https://img.scryfall.com/cards/art_crop/front/9/5/95a36e06-39f3-47d0-b6a9-43728afceb4a.jpg?1562821652#right)  

```statblock
"name": "Scholar of Athreos (TBVXXV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Lawful Evil"
"ac": !!int "10"
"hp": !!int "8"
"hit_dice": "2d8 + 0"
"modifier": !!int "0"
"stats":
  - !!int "11"
  - !!int "11"
  - !!int "11"
  - !!int "11"
  - !!int "15"
  - !!int "12"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Medicine|Medicine]]"
    "desc": "+4"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Any one language"
"cr": "1/2"
"traits":
  - "desc": "The scholar of athreos's innate spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: [[speak-with-dead-xphb|Speak With Dead]], [[light-xphb|Light]], [[sacred-flame-xphb|Sacred Flame]] 3/day: [[bless-xphb|Bless]], [[cure-wounds-xphb|Cure Wounds]], [[sanctuary-xphb|Sanctuary]]"
    "name": "Innate Spellcasting"
  - "desc": "When speaking with the dead, the scholar presents a gold coin (worth 1 gp). If the scholar is generally satisfied with the corpse's responses, the scholar pays the corpse that amount."
    "name": "Bribery"
"actions":
  - "desc": "_Melee or Ranged Weapon Attack:_ +6 to hit, reach 5 ft. or range 20/60 ft., one target. _Hit:_ 4 (1d4 + 2) piercing damage."
    "name": "Dagger"
  - "desc": "The scholar demands a tithe from all living humanoid creatures it within 30 ft. of it, except those wearing the temple's official garb. The tithe is 1 gp. On the scholar's next turn, as a bonus action, it deals 5 (1d10) necrotic damage to each creature that failed to pay."
    "name": "Collect Tithes (1/Day)"
"source":
  - "TBVXXV"
"image": "Compendium/bestiary/humanoid/token/scholar-of-athreos-tbvxxv.webp"
```
^statblock