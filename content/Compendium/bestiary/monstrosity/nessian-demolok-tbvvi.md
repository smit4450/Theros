---
title: Nessian Demolok
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/22
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Nessian Demolok"]
---
# Nessian Demolok
*Source: Theros Bestiary TBVVI*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more demolok cultists might be nearby with children, ready to pay tribute.
<li>A quest goal might involve protecting or destroying a structure that is near the demolok.
<li>A quest goal might involve protecting or vanquishing a demolok.
<li>A quest goal might involve protecting a child that is about to be sacrificed to the demolok.

![Nessian Demolok](Compendium/bestiary/monstrosity/img/nessian-demolok.webp#right|850)  

```statblock
"name": "Nessian Demolok (TBVVI)"
"size": "Gargantuan"
"type": "monstrosity"
"alignment": "Lawful Evil"
"ac": !!int "18"
"hp": !!int "420"
"hit_dice": "30d20 + 120"
"modifier": !!int "0"
"stats":
  - !!int "20"
  - !!int "10"
  - !!int "18"
  - !!int "7"
  - !!int "9"
  - !!int "9"
"speed": "160 ft."
"skillsaves":
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+3"
"damage_resistances": "fire"
"senses": "passive Perception 10"
"languages": "Common, Minotaur"
"cr": "22"
"traits":
  - "desc": "Immediately after the demolok uses the Dash action on its turn and moves at least 50 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The demolok deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "If the demolok moves at least 50 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 20 Strength saving throw or be knocked prone. If the target is prone, the demolok can make one stomp attack against it as a bonus action."
    "name": "Trampling Charge"
"actions":
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 30 (10d4 + 5) slashing damage."
    "name": "Claw"
  - "desc": "_Melee Weapon Attack:_ +12 to hit, reach 10 ft., one target. _Hit:_ 40 (10d6 + 5) piercing damage, and the demolok can use a bonus action to attempt to shove that target with its horns. The target must be within 10 feet of the demolok. Unless the target succeeds on a DC 20 Strength saving throw, the demolok pushes it up to 20 feet away from the demolok."
    "name": "Horns"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 30 (10d4 + 5) bludgeoning damage."
    "name": "Ram"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 5 ft., one prone creature. Hit: 60 (10d10 + 5) bludgeoning damage."
    "name": "Stomp"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 20 ft., one target. Hit: 40 (10d6 + 5) bludgeoning damage."
    "name": "Tail"
"reactions":
  - "desc": "Immediately after initiative rolls in which the demolok participates, it demands tribute from a creature it can see. That creature may take a bonus action to present a child to the demolok. If tribute is paid: The demolok takes a bonus action to devour the child. The demolok gains a permanent +3 bonus to damage rolls and Strength and Dexterity checks, and its hit points and maximum hit points are increased by 315 (30d20). If tribute isn't paid, the demolok takes a bonus action to move up to its speed and attack an object or structure."
    "name": "Demand Tribute"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/monstrosity/token/nessian-demolok-tbvvi.webp"
```
^statblock