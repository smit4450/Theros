---
title: Chronicler of Heroes
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxv
- monster/cr/1-4
- monster/size/m
- monster/type/fey
statblock: inline
aliases: ["Chronicler of Heroes"]
---
# Chronicler of Heroes
*Source: Theros Bestiary TBVXV*  

<blockquote><small>She paints pictures with words, though not all pictures show the truth.</small></blockquote>

![Chronicler of Heroes](Homebrew/bestiary/fey/img/chronicler-of-heroes.webp#right)  

```statblock
"name": "Chronicler of Heroes (TBVXV)"
"size": "Medium"
"type": "fey"
"subtype": "centaur"
"alignment": "Lawful Neutral"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "0"
"stats":
  - !!int "12"
  - !!int "11"
  - !!int "16"
  - !!int "16"
  - !!int "11"
  - !!int "12"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+2"
  - "name": "[[skills#Performance|Performance]]"
    "desc": "+3"
  - "name": "[[skills#History|History]]"
    "desc": "+5"
  - "name": "[[skills#Nature|Nature]]"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": "Common, Sylvan, Any one language"
"cr": "1/4"
"traits":
  - "desc": "If the chronicler moves at least 30 feet straight toward a target and then hits it with a melee attack on the same turn, it can immediately follow that attack with a bonus action, making one attack against the target with its hooves."
    "name": "Charge"
  - "desc": "The chronicler counts as one size larger when determining its carrying capacity and the weight it can push or drag. In addition, any climb that requires hands and feet is especially difficult for it because of its equine legs. When it makes such a climb, each foot of movement costs it 4 extra feet instead of the normal 1 extra foot."
    "name": "Equine Build"
  - "desc": "The chronicler's innate spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: [[silent-image-xphb|Silent Image]], [[legend-lore-xphb|Legend Lore]] 2/day: [[charm-person-xphb|Charm Person]]"
    "name": "Innate Spellcasting"
"actions":
  - "desc": "Melee Weapon Attack: one target. +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage."
    "name": "Hooves"
  - "desc": "The chronicler moves up to its speed toward a creature with the Heroic reaction. It attempts to learn of the creature's heroic deeds through conversation with that creature or with nearby creatures."
    "name": "Chronicle the Deeds"
"source":
  - "TBVXV"
"image": "Homebrew/bestiary/fey/token/chronicler-of-heroes-tbvxv.webp"
```
^statblock