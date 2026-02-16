---
title: Opaline Unicorn
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvii
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Opaline Unicorn"]
---
# Opaline Unicorn
*Source: Theros Bestiary TBVII*  

<blockquote><small>Purphoros once loved Nylea, the god of the hunt. His passion inspired his most astounding works of art.</small></blockquote>

![Opaline Unicorn](https://img.scryfall.com/cards/art_crop/front/c/f/cfba304c-9cb8-4d5c-b70d-b7f61a365977.jpg?1562831841#right)  

```statblock
"name": "Opaline Unicorn (TBVII)"
"size": "Large"
"type": "celestial"
"alignment": "Lawful Good"
"ac": !!int "12"
"hp": !!int "63"
"hit_dice": "9d10 + 18"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "14"
  - !!int "15"
  - !!int "11"
  - !!int "17"
  - !!int "16"
"speed": "50 ft."
"damage_immunities": "poison"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [paralyzed](Compendium/rules/conditions.md#Paralyzed), [poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": "Understands Celestial but can't speak"
"cr": "5"
"traits":
  - "desc": "If the unicorn moves at least 20 ft. straight toward a target and then hits it with a horn attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it must succeed on a DC 15 Strength saving throw or be knocked [prone](Compendium/rules/conditions.md#Prone)."
    "name": "Charge"
  - "desc": "The unicorn has doesn't need to eat, drink or breathe. It is immune to disease. It doesn't need to sleep, and magic can't put it to sleep."
    "name": "Constructed Resilience"
  - "desc": "When the unicorn takes a long rest, it must spend at least six hours in an active, motionless state, rather than sleeping. In this state, the unicorn appears inert, but the rest doesn't render it [unconscious](Compendium/rules/conditions.md#Unconscious), and it can see and hear as normal."
    "name": "Sentry's Rest"
"actions":
  - "desc": "The unicorn makes two attacks: one with its hooves and one with its horn."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft ., one target. Hit: 11 (2d6 + 4) bludgeoning damage."
    "name": "Hooves"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft ., one target. Hit: 8 (1d8 + 4) piercing damage."
    "name": "Horn"
  - "desc": "The unicorn touches a creature with its horn and restores one of that creature's level 1 spell slots."
    "name": "Restore Spell Slot"
"source":
  - "TBVII"
"image": "Compendium/bestiary/celestial/token/opaline-unicorn-tbvii.webp"
```
^statblock