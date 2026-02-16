---
title: Prognostic Sphinx
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Prognostic Sphinx"]
---
# Prognostic Sphinx
*Source: Theros Bestiary TBVVI*  

The prognostic sphinx is an expert in predicting the likelihood of recovery from disease and ailments.

![Prognostic Sphinx](https://img.scryfall.com/cards/art_crop/front/9/f/9f0a27a6-54b8-4615-89b3-591a4e3ef626.jpg?1562822709#right)  

```statblock
"name": "Prognostic Sphinx (TBVVI)"
"size": "Large"
"type": "monstrosity"
"alignment": "Lawful Neutral"
"ac": !!int "17"
"hp": !!int "120"
"hit_dice": "12d10 + 60"
"modifier": !!int "0"
"stats":
  - !!int "17"
  - !!int "10"
  - !!int "20"
  - !!int "16"
  - !!int "18"
  - !!int "23"
"speed": "40 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "6"
  - "constitution": !!int "11"
  - "intelligence": !!int "9"
  - "wisdom": !!int "10"
"skillsaves":
  - "name": "[Arcana](Compendium/rules/skills.md#Arcana)"
    "desc": "+9"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+10"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+15"
  - "name": "[Medicine](Compendium/rules/skills.md#Medicine)"
    "desc": "+10"
"damage_immunities": "psychic, bludgeoning, piercing, and slashing from nonmagical attacks"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened)"
"senses": "[Truesight](Compendium/rules/senses.md#Truesight) 120 ft., passive Perception 10"
"languages": "Common, Sphinx"
"cr": "9"
"traits":
  - "desc": "The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intentions or sincerity have [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md)."
    "name": "Inscrutable"
  - "desc": "The sphinx's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The prognostic sphinx's innate spellcasting ability is Wisdom (spell save DC 18, +10 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: [Identify](Compendium/spells/identify-xphb.md), [True Strike](Compendium/spells/true-strike-xphb.md) 3/day: [Augury](Compendium/spells/augury-xphb.md), [Detect Poison Or Disease](Compendium/spells/detect-poison-or-disease-xphb.md), [Locate Animals Or Plants](Compendium/spells/locate-animals-or-plants-xphb.md) 2/day: [Divination](Compendium/spells/divination-xphb.md) 1/day: [Legend Lore](Compendium/spells/legend-lore-xphb.md), [Scrying](Compendium/spells/scrying-xphb.md)"
    "name": "Innate Spellcasting"
  - "desc": "The sphinx can't be affected or detected by spells of 6th level or lower unless it wishes to be. It has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against all other spells and magical effects."
    "name": "Limited Magic Immunity"
"actions":
  - "desc": "The sphinx makes two claw attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 24 (2d10 + 3) slashing damage."
    "name": "Claw"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/monstrosity/token/prognostic-sphinx-tbvvi.webp"
```
^statblock