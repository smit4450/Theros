---
title: Flame-Wreathed Phoenix
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/size/t
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Flame-Wreathed Phoenix"]
---
# Flame-Wreathed Phoenix
*Source: Theros Bestiary TBVIV*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more phoenix cultists might be nearby who will pay tribute to the phoenix.
<li>A valuable (but flammable) object might be positioned near the phoenix.
<li>A quest goal might involve securing a phoenix egg.
<li>A quest goal might involve vanquishing a phoenix that reincarnates itself every time it is killed.

![Flame-Wreathed Phoenix](Compendium/bestiary/elemental/img/flame-wreathed-phoenix.webp#right|850)  

```statblock
"name": "Flame-Wreathed Phoenix (TBVIV)"
"size": "Tiny"
"type": "elemental"
"alignment": "Neutral"
"ac": !!int "18"
"hp": !!int "15"
"hit_dice": "3d4 + 9"
"modifier": !!int "4"
"stats":
  - !!int "17"
  - !!int "18"
  - !!int "17"
  - !!int "2"
  - !!int "15"
  - !!int "14"
"speed": "5 ft., fly 60 ft."
"saves":
  - "wisdom": !!int "5"
  - "charisma": !!int "5"
"damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks, cold"
"damage_immunities": "fire"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": ""
"cr": "8"
"traits":
  - "desc": "Immediately after initiative rolls in which the phoenix participates, it expects tribute from a creature within 60 feet that it can see, but does not reveal which one or indicate it expects the tribute. Tribute may be paid by bowing, genuflecting, saluting, or a similar gesture. If by the beginning of the phoenix's first turn in combat the creature it selected has paid it tribute, the phoenix's flames grow larger, brighter, and louder. Until the end of combat, the phoenix gains a +2 bonus to damage rolls and Strength and Dexterity checks, gains 5 (2d4) temporary [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md), and loses its Rebirth trait."
    "name": "Expect Tribute"
  - "desc": "When the phoenix dies, it explodes. Each creature within 10 feet of it must make a DC 20 Dexterity saving throw, taking 5 (1d10) fire damage on a failed save, or half as much damage on a successful one. The fire ignites flammable objects in the area that aren't worn or carried."
    "name": "Fiery Death"
  - "desc": "The phoenix doesn't provoke opportunity attacks when it flies out of an enemy's reach."
    "name": "Flyby"
  - "desc": "The phoenix sheds bright light in a 30-foot radius and dim light for an additional 15 feet."
    "name": "Illumination"
  - "desc": "The explosion from the Fiery Death trait destroys the phoenix's body and leaves behind an egg-shaped cinder that weighs 2 ounces. The cinder is blazing hot, dealing 21 (6d6) fire damage to any creature that touches it, though no more than once per round. The cinder is immune to all damage, and after 1d6 hours, it hatches a new phoenix."
    "name": "Rebirth"
  - "desc": ""
    "name": ""
"actions":
  - "desc": "The phoenix makes two attacks: one with its beak and one with its fiery talons."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage and 10 (2d6 + 3) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 5 (1d10) fire damage at the start of each of its turns."
    "name": "Beak"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage and 12 (2d8 + 3) fire damage."
    "name": "Fiery Talons"
"legendary_actions":
  - "desc": "The phoenix makes one beak attack."
    "name": "Peck"
  - "desc": "The phoenix moves up to its speed."
    "name": "Move"
  - "desc": "The phoenix moves up to its speed and attacks with its fiery talons."
    "name": "Swoop (Costs 2 Actions)"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/elemental/token/flame-wreathed-phoenix-tbviv.webp"
```
^statblock