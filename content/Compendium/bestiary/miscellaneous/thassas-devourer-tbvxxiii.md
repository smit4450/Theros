---
title: Thassa's Devourer
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxiii
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Thassa's Devourer"]
---
# Thassa's Devourer
*Source: Theros Bestiary TBVXXIII*  

<blockquote><small>When mortals claim there are places Thassa cannot reach, the sea god laughs.</small></blockquote>

![Thassa's Devourer](https://img.scryfall.com/cards/art_crop/front/d/4/d4ebd8c0-bb03-434d-b669-d9b35d07b2c6.jpg?1593095570#right)  

```statblock
"name": "Thassa's Devourer (TBVXXIII)"
"size": "Large"
"type": "5th-level transmutation elemental"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"hp": !!int "132"
"hit_dice": "12d10 + 72"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "14"
  - !!int "22"
  - !!int "5"
  - !!int "10"
  - !!int "12"
"speed": "60 ft., climb 60 ft., swim 90 ft."
"damage_resistances": "acid, bludgeoning, piercing, and slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](Compendium/rules/conditions.md#Exhaustion), [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed), [petrified](Compendium/rules/conditions.md#Petrified), [poisoned](Compendium/rules/conditions.md#Poisoned), [prone](Compendium/rules/conditions.md#Prone), [restrained](Compendium/rules/conditions.md#Restrained), [unconscious](Compendium/rules/conditions.md#Unconscious)"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 60 ft. (can't see beyond this radius), passive Perception 10"
"languages": "Primordial"
"cr": "4"
"traits":
  - "desc": "If the elemental takes cold damage, it partially freezes; its speed is reduced by 20 ft. until the end of its next turn."
    "name": "Freeze"
  - "desc": "The devourer's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "In addition to being a creature, the elemental is a 5th-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The elemental glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
  - "desc": "While the elemental is in any of Theros's three realms, it can magically convey what it senses to Thassa."
    "name": "Telepathic Bond"
  - "desc": "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."
    "name": "Water Form"
"actions":
  - "desc": "The elemental makes two slam attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 11 (2d8 + 2) bludgeoning damage."
    "name": "Slam"
  - "desc": "Each creature in the elemental's space must make a DC 12 Strength saving throw. On a failure, a target takes 11 (2d8 + 2) bludgeoning damage. If it is Large or smaller, it is also [grappled](Compendium/rules/conditions.md#Grappled) (escape DC 12). Until this grapple ends, the target is [restrained](Compendium/rules/conditions.md#Restrained) and unable to breathe unless it can breathe water. If the saving throw is successful, the target is pushed out of the elemental's space. The elemental can grapple one Large creature or up to two Medium or smaller creatures at one time. At the start of each of the elemental's turns, each target [grappled](Compendium/rules/conditions.md#Grappled) by it takes 11 (2d8 + 2) bludgeoning damage. A creature within 5 feet of the elemental can pull a creature or object out of it by taking an action to make a DC 12 Strength check and succeeding."
    "name": "Whelm (Recharge 4-6)"
"source":
  - "TBVXXIII"
"image": "Compendium/bestiary/miscellaneous/token/thassas-devourer-tbvxxiii.webp"
```
^statblock