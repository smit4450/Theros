---
title: Hag Tongue
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvv
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/size/t
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Hag Tongue"]
---
# Hag Tongue
*Source: Theros Bestiary TBVV*  

A hag coven can craft a magic item called a Hag Tongue, which is made from a real tongue. When placed in a hag's mouth, it begins to speak. It generally is cooperative as long as it's inside a mouth. Once taken out, it helplessly squirms around like a fish out of water. Its amorphous nature makes it very difficult to hold onto.

```statblock
"name": "Hag Tongue (TBVV)"
"size": "Tiny"
"type": "construct"
"subtype": "homunculus"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "1"
"hit_dice": "1d4 + -1"
"modifier": !!int "2"
"stats":
  - !!int "8"
  - !!int "15"
  - !!int "8"
  - !!int "1"
  - !!int "1"
  - !!int "1"
"speed": "5 ft."
"senses": "blindsight 0 ft., passive Perception 10"
"languages": "Common, Giant, Primordial"
"cr": "0"
"traits":
  - "desc": "The tongue can't speak if it's not inside a hag's mouth."
    "name": "Hag Tongue"
  - "desc": "The tongue has advantage on ability checks and saving throws made to escape a grapple."
    "name": "Slippery"
  - "desc": "The tongue can move through a space as narrow as 1 inch wide without squeezing."
    "name": "Amorphous"
"actions":
  - "desc": "If the tongue is inside a hag's mouth, it may speak."
    "name": "Speak"
"source":
  - "TBVV"
"image": "Compendium/bestiary/construct/token/hag-tongue-tbvv.webp"
```
^statblock