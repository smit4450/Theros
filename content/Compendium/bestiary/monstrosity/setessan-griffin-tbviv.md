---
title: Setessan Griffin
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Setessan Griffin"]
---
# Setessan Griffin
*Source: Theros Bestiary TBVIV*  

<small><blockquote>Most griffins must be caught and broken into the service of the polis. Not so in Setessa, where they volunteer.</blockquote></small>

![Setessan Griffin](https://img.scryfall.com/cards/art_crop/front/3/5/35d2ae77-b16c-4a01-84ce-5c78be5a54d8.jpg?1562816585#right)  

```statblock
"name": "Setessan Griffin (TBVIV)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "56"
"hit_dice": "7d10 + 21"
"modifier": !!int "2"
"stats":
  - !!int "20"
  - !!int "15"
  - !!int "16"
  - !!int "2"
  - !!int "13"
  - !!int "8"
"speed": "30 ft., fly 80 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The griffin has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Wisdom (Perception) checks that rely on sight."
    "name": "Keen Sight"
  - "desc": "At the beginning of every creature's turn that the griffin can see a Setessan creature, it gains 20 temporary [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) for the duration of that turn and its attacks deal 50% more damage, rounded up."
    "name": "Eager Servitor"
"actions":
  - "desc": "The griffin makes two attacks: one with its beak and one with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) piercing damage."
    "name": "Beak"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage."
    "name": "Claws"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/monstrosity/token/setessan-griffin-tbviv.webp"
```
^statblock