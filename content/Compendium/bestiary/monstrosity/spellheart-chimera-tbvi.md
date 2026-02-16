---
title: Spellheart Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvi
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Spellheart Chimera"]
---
# Spellheart Chimera
*Source: Theros Bestiary TBVI*  

<blockquote>Thaumaturges remain silent around chimeras, lest their words conjure even stranger beasts.</blockquote>

The spellheart chimera has the front half of a ram and the hindquarters of a lion, with an eagle's wings and rear claws. It devours the essence of spells when they are cast.

![Spellheart Chimera](https://img.scryfall.com/cards/art_crop/front/8/7/8782a7b7-79ca-4e5c-845b-d662222574c0.jpg?1562857033#right)  

```statblock
"name": "Spellheart Chimera (TBVI)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "11"
"ac_class": "natural armor"
"hp": !!int "24"
"hit_dice": "4d10 + 4"
"modifier": !!int "0"
"stats":
  - !!int "17"
  - !!int "11"
  - !!int "12"
  - !!int "3"
  - !!int "12"
  - !!int "6"
"speed": "40 ft., fly 60 ft."
"senses": "passive Perception 10"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "The chimera can move in and out of a large or smaller creature's space. If it would, it uses a bonus action to attack that creature with its hooves. That creature must succeed on a DC 13 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the creature succeeds, the chimera can't enter that space and must end its turn immediately. If the chimera stops on top of that creature, that creature becomes [[conditions#Restrained|restrained]] until the chimera moves off it (escape DC 13)."
    "name": "Trample"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) bludgeoning damage."
    "name": "Ram"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 5 (1d4 + 3) bludgeoning damage."
    "name": "Hooves"
"reactions":
  - "desc": "Whenever any spell is cast that targets only the chimera (not an area), the chimera's Strength increases by 1."
    "name": "Spellheart"
"source":
  - "TBVI"
"image": "Compendium/bestiary/monstrosity/token/spellheart-chimera-tbvi.webp"
```
^statblock