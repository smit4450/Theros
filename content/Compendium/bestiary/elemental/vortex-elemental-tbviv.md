---
title: Vortex Elemental
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/14
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Vortex Elemental"]
---
# Vortex Elemental
*Source: Theros Bestiary TBVIV*  

<blockquote><small>The sea is always hungry.</small></blockquote>

![Vortex Elemental](https://img.scryfall.com/cards/art_crop/front/5/c/5cb7ca2b-c5de-4c8a-91cb-8dd8ab5387d8.jpg?1578451880#right)  

```statblock
"name": "Vortex Elemental (TBVIV)"
"size": "Gargantuan"
"type": "elemental"
"subtype": "titan"
"alignment": "Lawful Evil"
"ac": !!int "17"
"hp": !!int "450"
"hit_dice": "30d20 + 150"
"modifier": !!int "-1"
"stats":
  - !!int "20"
  - !!int "8"
  - !!int "20"
  - !!int "1"
  - !!int "1"
  - !!int "8"
"speed": "0 ft."
"damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks, cold"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](Compendium/rules/conditions.md#Exhaustion), [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed), [petrified](Compendium/rules/conditions.md#Petrified), [poisoned](Compendium/rules/conditions.md#Poisoned), [prone](Compendium/rules/conditions.md#Prone), [restrained](Compendium/rules/conditions.md#Restrained), [unconscious](Compendium/rules/conditions.md#Unconscious)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": ""
"cr": "14"
"traits":
  - "desc": "As long as the elemental doesn't have a whirlpool, it is indistinguishable from normal submarine rocks."
    "name": "False Appearance"
  - "desc": "The elemental's eyes and mouth remain closed and undetectable except when it is awake. An orange glow penetrates the water where its eyes and mouth are when they are opened."
    "name": "Glowing Eyes and Mouth"
  - "desc": "The mouth of the elemental is solid rock, 20 feet thick. It opens only during a Whirlpool or a Regurgitate action, then closes promptly when that event is complete."
    "name": "Mouth"
  - "desc": "The stomach of the elemental is an undersea cavern that glows bright orange at the bottom. During a Regurgitate, the floor of the cavern rises to meet the elemental's mouth, causing everything inside it to be expelled. Conversely, the cavern's floor sinks 100 feet from the mouth during a Whirlpool. At all times, the stomach is completely filled with water, regardless of its size."
    "name": "Stomach"
"actions":
  - "desc": "The elemental opens its mouth, creating a vortex that is 50 feet wide at the base, up to 500 feet wide at the top, and 250 feet tall. Any creature or object in the water and within 250 feet of the vortex is pulled 50 (1d4 * 25) feet toward the center. A creature can swim away from the vortex by making a DC 9 Strength (Athletics) check. When a creature enters the vortex for the first time on a turn or starts its turn there, it must make a Strength saving throw. On a failed save, the creature takes 2d8 bludgeoning damage and is caught in the vortex until the spell ends. On a successful save, the creature takes half damage, and isn't caught in the vortex. A creature caught in the vortex can use its action to try to swim away from the vortex as described above, but has [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md) on the Strength (Athletics) check to do so. The first time each turn that an object enters the vortex, the object takes 2d8 bludgeoning damage; this damage occurs each round it remains in the vortex. An object or creature that is 50 feet or less from the mouth of the elemental becomes swallowed. The whirlpool lasts 10 rounds, and the elemental may not take a Regurgitate action until after the whirlpool is complete."
    "name": "Whirlpool (3/day; Recharges after a Regurgitate)"
  - "desc": "_Melee Weapon Attack:_ +10 to hit, reach 5 ft., one target that is in the elemental's whirlpool. _Hit:_ 22 (2d8 + 5) bludgeoning damage."
    "name": "Smash"
  - "desc": "The elemental opens its mouth and belches, creating a 20-foot tall wave that travels from its mouth for 100 feet and then crashes down. Any Huge or smaller vehicles in the wave's path are carried with it to the other side. Any Huge or smaller vehicles struck by the wave have a 25 percent chance of capsizing. Anything the elemental has swallowed is expelled with this water."
    "name": "Regurgitate (3/day; Recharges after a Whirlpool is completed)"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/elemental/token/vortex-elemental-tbviv.webp"
```
^statblock