---
title: Venomous Basilisk
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Venomous Basilisk"]
---
# Venomous Basilisk
*Source: Theros Bestiary TBVIV*  

<small><blockquote>"Anyone who sees the eyes of a basilisk serpent (<i>Basilisci serpentis</i>) dies immediately... Its touch and even its breath scorch grass, kill bushes and burst rocks. Its poison is so deadly that once when a man on a horse speared a basilisk, the venom travelled up the spear and killed not only the man, but also the horse. A weasel can kill a basilisk; the serpent is thrown into a hole where a weasel lives, and the stench of the weasel kills the basilisk at the same time as the basilisk kills the weasel."

- Pliny the Elder</blockquote></small>
The basilisk's lair should be easy to identify; all nearby vegetation is blighted, scorched, and withered. The basilisk is immune to its own venom, so a mirror will do no good in this fight. One's only hope is tossing a weasel at it.

Any part of a basilisk might be profitable to sell. Basilisk blood is a pricey commodity due to the obvious challenges in obtaining it. Pharika claims that it can be used to make antidotes, but few have even been able to obtain it to experiment with.

![Venomous Basilisk](https://img.scryfall.com/cards/art_crop/front/7/9/799d08a6-d978-4731-98ad-38acd57f3196.jpg?1562820228#right)  

```statblock
"name": "Venomous Basilisk (TBVIV)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "48"
"hit_dice": "8d8 + 16"
"modifier": !!int "-1"
"stats":
  - !!int "16"
  - !!int "8"
  - !!int "15"
  - !!int "2"
  - !!int "8"
  - !!int "7"
"speed": "20 ft."
"damage_immunities": "poison, acid"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "If a non-basilisk creature starts its turn within 30 ft. of the basilisk and the two of them can see each other, the basilisk can force the creature to make a DC 12 Constitution saving throw if the basilisk isn't [incapacitated](Compendium/rules/conditions.md#Incapacitated). On a failed save, the creature becomes infected with the basilisk's venom. Until cured, the venom deals 36 (8d8) poison damage to the creature at the end of its turn. A creature that isn't surprised can avert its eyes to avoid the saving throw at the start of its turn. If it does so, it can't see the basilisk until the start of its next turn, when it can avert its eyes again. If it looks at the basilisk in the meantime, it must immediately make the save."
    "name": "Venomous Gaze"
  - "desc": "Any creature that starts its turn within 10 feet of the basilisk must succeed on a DC 14 Constitution saving throw or be [poisoned](Compendium/rules/conditions.md#Poisoned) until the start of its next turn."
    "name": "Stench"
  - "desc": "The odor of a living or dead weasel is toxic to the basilisk, although the weasel has no immunity to the basilisk's venom, so both die."
    "name": "Weakness to Weasels"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage plus 7 (2d6) poison damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) poison damage plus 7 (2d6) acid damage."
    "name": "Acidic Touch"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/monstrosity/token/venomous-basilisk-tbviv.webp"
```
^statblock