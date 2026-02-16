---
title: Returned Centaur
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxii
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Returned Centaur"]
---
# Returned Centaur
*Source: Theros Bestiary TBVXXII*  

<blockquote><small>Driven away by his living kin, he wanders mourning through the wilderness, seeking the dead city of Asphodel.</small></blockquote>

![Returned Centaur](Compendium/bestiary/undead/img/returned-centaur.webp#right|850)  

```statblock
"name": "Returned Centaur (TBVXXII)"
"size": "Medium"
"type": "undead"
"subtype": "returned, centaur"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "32"
"hit_dice": "4d8 + 16"
"modifier": !!int "2"
"stats":
  - !!int "13"
  - !!int "15"
  - !!int "18"
  - !!int "11"
  - !!int "13"
  - !!int "10"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+4"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "passive Perception 10"
"languages": "Common, Sylvan"
"cr": "1"
"traits":
  - "desc": "As a bonus action, the centaur can add 1d10 to its next attack or damage roll with a longbow or shortbow."
    "name": "Archer's Eye (3/Day)"
  - "desc": "If the centaur moves at least 30 feet straight toward a target and then hits it with a melee attack on the same turn, it can immediately follow that attack with a bonus action, making one attack against the target with its hooves."
    "name": "Charge"
  - "desc": "The centaur counts as one size larger when determining its carrying capacity and the weight it can push or drag. In addition, any climb that requires hands and feet is especially difficult for it because of its equine legs. When it makes such a climb, each foot of movement costs it 4 extra feet instead of the normal 1 extra foot."
    "name": "Equine Build"
  - "desc": "The centaur has proficiency in one of the following skills: Animal Handling, Medicine, Nature, or Survival."
    "name": "Survivor"
  - "desc": "The centaur needs water and air but not food or sleep. It thinks and speaks and even feels emotions based on its new experiences, but given its circumstances, those emotions tend to be muted."
    "name": "Returned Nature"
  - "desc": "The centaur has [[advantage-xphb|Advantage]] on saving throws against any effect that turns undead."
    "name": "Turn Resistance"
  - "desc": "The centaur is immune to any effect that would sense its emotions or read its thoughts. Wisdom (Insight) checks to ascertain the centaur's intentions or sincerity are made with [[disadvantage-xphb|Disadvantage]]."
    "name": "Unreadable Face"
"actions":
  - "desc": "The centaur makes two attacks with its longbow."
    "name": "Multiattack"
  - "desc": "_Ranged Weapon Attack:_ +4 to hit, range 150/600 ft., one target. _Hit:_ 6 (1d8 + 2) piercing damage."
    "name": "Longbow"
  - "desc": "Melee Weapon Attack: one target. Hit: 3 (1d4 + 1) bludgeoning damage."
    "name": "Hooves"
"source":
  - "TBVXXII"
"image": "Compendium/bestiary/undead/token/returned-centaur-tbvxxii.webp"
```
^statblock