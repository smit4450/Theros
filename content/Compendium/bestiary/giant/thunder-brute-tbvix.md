---
title: Thunder Brute
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvix
- monster/cr/23
- monster/size/g
- monster/type/giant
statblock: inline
aliases: ["Thunder Brute"]
---
# Thunder Brute
*Source: Theros Bestiary TBVIX*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more cyclops cultists might be nearby who will pay tribute.
<li>A valuable (but flammable) object might be positioned near the cyclops.
<li>A quest goal might involve protecting or destroying a structure that is near the cyclops.
<li>A quest goal might involve protecting or vanquishing the cyclops.
<li>A quest goal might involve protecting a creature that is near the cyclops.

![Thunder Brute](https://img.scryfall.com/cards/art_crop/front/c/2/c28fa4f8-4b87-41dc-802d-dfd160ccf1a8.jpg?1593092387#right)  

```statblock
"name": "Thunder Brute (TBVIX)"
"size": "Gargantuan"
"type": "giant"
"subtype": "cyclops"
"alignment": "Chaotic Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "0"
"stats":
  - !!int "20"
  - !!int "11"
  - !!int "20"
  - !!int "8"
  - !!int "6"
  - !!int "10"
"speed": "120 ft."
"damage_resistances": "cold"
"damage_immunities": "lightning, thunder"
"condition_immunities": "[[conditions#Deafened|deafened]]"
"senses": "passive Perception 10"
"languages": "Giant"
"cr": "23"
"traits":
  - "desc": "At the start of each of the cyclops's turns, each grounded creature within 5 feet of it takes 10 (3d6) lightning damage, and flammable objects in the aura that aren't being worn or carried ignite. A creature that touches the cyclops or hits it with a melee attack while within 5 feet of it takes 10 (3d6) lightning damage."
    "name": "Lightning Aura"
  - "desc": "The cyclops has [[disadvantage-xphb|Disadvantage]] on any attack roll against a target more than 30 feet away."
    "name": "Poor Depth Perception"
  - "desc": "The cyclops can move in and out of a Huge or smaller creature's space. If it would, it uses a bonus action to attack that creature with its unarmed strike. That creature must succeed on a DC 15 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the creature succeeds, the cyclops can't enter that space and must end its turn immediately. If the cyclops stops on top of that creature, that creature becomes [[conditions#Restrained|restrained]] until the cyclops moves off it (escape DC 15)."
    "name": "Trample"
"actions":
  - "desc": "The cyclops makes two unarmed strikes."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 30 (10d4 + 5) bludgeoning damage."
    "name": "Unarmed Strike"
  - "desc": "The cyclops hurls a magical lightning bolt at a point it can see within 500 feet of it. Each creature within 10 feet of that point must make a DC 17 Dexterity saving throw, taking 54 (12d8) lightning damage on a failed save, or half as much damage on a successful one."
    "name": "Lightning Strike (Recharge 5-6)"
  - "desc": "The cyclops claps its hands together. Each creature within a 20-foot radius from the cyclops takes 10 (1d10+5) thunder damage."
    "name": "Thunderclap (Recharge 4-5)"
"reactions":
  - "desc": "Immediately after initiative rolls in which the cyclops participates, it demands tribute from a creature it can see. That creature may bow, genuflect, salute, or perform a similar gesture as a bonus action. If tribute is paid: Until the end of combat, the cyclops gains a permanent +3 bonus to damage rolls and Strength and Dexterity checks, and 315 (30d20) temporary [[hit-points-xphb|Hit Points]]. If tribute isn't paid: The cyclops pounds the earth, dealing 30 (10d4+5) thunder damage to every creature and object on the ground (including walls) within a 15-foot radius."
    "name": "Demand Tribute"
"source":
  - "TBVIX"
"image": "Compendium/bestiary/giant/token/thunder-brute-tbvix.webp"
```
^statblock