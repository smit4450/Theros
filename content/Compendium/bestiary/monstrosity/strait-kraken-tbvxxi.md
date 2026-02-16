---
title: Strait Kraken
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxi
- ttrpg-cli/monster/cr/14
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Strait Kraken"]
---
# Strait Kraken
*Source: Theros Bestiary TBVXXI*  

<small><blockquote>Thassa felt no need to punish the sailors for their folly in crossing the straits. The kraken would do it for her.</blockquote></small>

![Strait Kraken](https://img.scryfall.com/cards/art_crop/front/1/2/12ae69b3-afa5-4763-a0c8-c3d9d96f6ddc.jpg?1578451786#right)  

```statblock
"name": "Strait Kraken (TBVXXI)"
"size": "Gargantuan"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "384"
"hit_dice": "24d20 + 144"
"modifier": !!int "2"
"stats":
  - !!int "23"
  - !!int "15"
  - !!int "22"
  - !!int "6"
  - !!int "14"
  - !!int "7"
"speed": "0 ft., swim 120 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
"condition_immunities": "[[conditions#Paralyzed|paralyzed]], [[conditions#Stunned|stunned]]"
"senses": "passive Perception 10"
"languages": ""
"cr": "14"
"traits":
  - "desc": "The kraken can hold its breath for 90 minutes. The kraken won't lose its held breath as a result of damage."
    "name": "Massive Lungs"
  - "desc": "The kraken can survive for 3 hours on land. Every turn thereafter, the kraken takes 1 bludgeoning damage for every turn it remains on land. This damage comes from its weight crushing it, so being magically lifted, being given a flying speed, or other means of the DM's discretion can prevent it. Additionally, the kraken takes double the normal damage from falling, but if it falls onto a creature, that creature takes an equal amount of bludgeoning damage."
    "name": "Extremely Heavy"
  - "desc": "If the kraken makes an attack action that fails against a target not fully underwater while the kraken has at least one tentacle above the surface, the kraken takes a bonus action to slap the surface of the water with that tentacle, dealing 4 (1d8) bludgeoning damage to the target. If the tentacle was grappling anything, it isn't anymore."
    "name": "Splash"
"actions":
  - "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 9 (3d6 + 6) bludgeoning plus 7 (2d6) piercing damage and the target is [[conditions#Grappled|grappled]] (escape DC 20 Strength). It can release a [[conditions#Grappled|grappled]] creature as a free action. If the kraken takes 100 or more damage to one tentacle in a single round, that tentacle falls off."
    "name": "Tentacles"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 37 (7d8 + 6) bludgeoning damage."
    "name": "Bite"
"source":
  - "TBVXXI"
"image": "Compendium/bestiary/monstrosity/token/strait-kraken-tbvxxi.webp"
```
^statblock