---
title: Pharika's Mender
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Pharika's Mender"]
---
# Pharika's Mender
*Source: Theros Bestiary TBVVI*  

<small><blockquote>“The direst venom becomes a panacea under Pharika’s guidance. I bring it to the worthy, clinging at the edge of the abyss.”</blockquote></small>

![Pharika's Mender](Compendium/bestiary/monstrosity/img/pharikas-mender.webp#right|850)  

```statblock
"name": "Pharika's Mender (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"subtype": "medusa, gorgon"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "plate"
"hp": !!int "77"
"hit_dice": "11d8 + 33"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "15"
  - !!int "17"
  - !!int "12"
  - !!int "13"
  - !!int "18"
"speed": "30 ft."
"skillsaves":
  - "name": "[Deception](Compendium/rules/skills.md#Deception)"
    "desc": "+7"
  - "name": "[Insight](Compendium/rules/skills.md#Insight)"
    "desc": "+4"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
  - "name": "[Medicine](Compendium/rules/skills.md#Medicine)"
    "desc": "+4"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": "Common"
"cr": "3"
"traits":
  - "desc": "The gorgon is an expert in extending its own life to immortality, and it enjoys a high-stake deal. If a creature successfully restrains the gorgon, it will share one of its medicinal secrets in exchange for its freedom."
    "name": "Gorgon's Trial"
  - "desc": "The gorgon doesn't require food, drink, or sleep."
    "name": "Immortal Nature"
  - "desc": "The mender's innate spellcasting ability is Charisma (spell save DC 15, +7 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: [Spare The Dying](Compendium/spells/spare-the-dying-xphb.md) 3/day: [Cure Wounds](Compendium/spells/cure-wounds-xphb.md), [Lesser Restoration](Compendium/spells/lesser-restoration-xphb.md), [Protection From Poison](Compendium/spells/protection-from-poison-xphb.md) 1/day: [Revivify](Compendium/spells/revivify-xphb.md)"
    "name": "Innate Spellcasting"
  - "desc": "As soon as a creature within 30 feet of the gorgon sees the gorgon's face, it may make a DC 14 Constitution saving throw. On a success, that creature may use a reaction to shield its eyes or avert them. If the saving throw fails by 5 or more, or if the creature is unable to react, the creature is instantly [petrified](Compendium/rules/conditions.md#Petrified). Otherwise, a creature that fails the save begins to turn to stone and is [restrained](Compendium/rules/conditions.md#Restrained). The [restrained](Compendium/rules/conditions.md#Restrained) creature must repeat the saving throw at the end of its next turn, becoming [petrified](Compendium/rules/conditions.md#Petrified) on a failure or ending the effect on a success. The petrification lasts until the creature is unpetrified by a god.If the gorgon sees its own face reflected on a polished surface within 30 ft. of it and in an area of bright light, the gorgon is, due to its curse, affected by its own visage.This trait has no effect if the gorgon's face is not its normal flesh state. The trait remains active even if the gorgon is [incapacitated](Compendium/rules/conditions.md#Incapacitated), killed, and even beheaded."
    "name": "Petrifying Visage"
  - "desc": "The mender wears a visored helmet to prevent accidental petrification. While her visor is down, other creatures can't see her eyes."
    "name": "Visor"
"actions":
  - "desc": "The gorgon makes two attacks: one to constrict, and one with its shortsword."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 10 ft., one target. Hit: 7 (2d6) bludgeoning damage, and the target is [grappled](Compendium/rules/conditions.md#Grappled) (escape DC 10) if it is a Large or smaller creature. Until this grapple ends, the target is [restrained](Compendium/rules/conditions.md#Restrained), and the gorgon can’t constrict another target."
    "name": "Constrict"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) piercing damage."
    "name": "Shortsword"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/monstrosity/token/pharikas-mender-tbvvi.webp"
```
^statblock