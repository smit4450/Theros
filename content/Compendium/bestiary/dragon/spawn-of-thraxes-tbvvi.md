---
title: Spawn of Thraxes
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/24
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Spawn of Thraxes"]
---
# Spawn of Thraxes
*Source: Theros Bestiary TBVVI*  

<small><blockquote>Sparks from Purphoros's forge fill the belly of every dragon.</blockquote></small><big><b>Lair Actions</b></big>
On initiative count 20 (losing initiative ties), the dragon takes a lair action to cause one of the following effects; the dragon can’t use the same effect two rounds in a row:

<li>Magma erupts from a point on the ground the dragon can see within 120 feet of it, creating a 20-foot-high, 5-foot-radius geyser. Each creature in the geyser’s area must make a DC 15 Dexterity saving throw, taking 21 (6d6) fire damage on a failed save, or half as much damage on a successful one.
<li>A tremor shakes the lair in a 60-foot radius around the dragon. Each creature other than the dragon on the ground in that area must succeed on a DC 15 Dexterity saving throw or be knocked prone.
<li>Volcanic gases form a cloud in a 20-foot-radius sphere centered on a point the dragon can see within 120 feet of it. The sphere spreads around corners, and its area is lightly obscured. It lasts until initiative count 20 on the next round. Each creature that starts its turn in the cloud must succeed on a DC 13 Constitution saving throw or be poisoned until the end of its turn. While poisoned in this way, a creature is incapacitated.

<big><b>Regional Effects</b></big>
The region containing a legendary red dragon’s lair is warped by the dragon’s magic, which creates one or more of the following effects:

<li>Small earthquakes are common within 6 miles of the dragon’s lair.
<li>Water sources within 1 mile of the lair are supernaturally warm and tainted by sulfur.
<li>Rocky fissures within 1 mile of the dragon’s lair form portals to the Elemental Plane of Fire, allowing creatures of elemental fire into the world to dwell nearby.

If the dragon dies, these effects fade over the course of 1d10 days.

![Spawn of Thraxes](Compendium/bestiary/dragon/img/spawn-of-thraxes.webp#right)  

```statblock
"name": "Spawn of Thraxes (TBVVI)"
"size": "Gargantuan"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "22"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "0"
"stats":
  - !!int "21"
  - !!int "10"
  - !!int "20"
  - !!int "15"
  - !!int "15"
  - !!int "23"
"speed": "40 ft., fly 80 ft., climb 40 ft."
"saves":
  - "dexterity": !!int "7"
  - "constitution": !!int "12"
  - "wisdom": !!int "9"
  - "charisma": !!int "13"
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+16"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+7"
"damage_immunities": "fire"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 10"
"languages": "Draconic, Common (barely)"
"cr": "24"
"traits":
  - "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
"actions":
  - "desc": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 15 (2d10 + 5) piercing damage plus 14 (4d6) fire damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) slashing damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 20 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage."
    "name": "Tail"
  - "desc": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 21 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."
    "name": "Frightful Presence"
  - "desc": "The dragon exhales fire in a 90-foot cone. Each creature in that area must make a DC 24 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one."
    "name": "Fire Breath (Recharge 5-6)"
"legendary_actions":
  - "desc": "The dragon makes a Wisdom (Perception) check."
    "name": "Detect"
  - "desc": "The dragon makes a tail attack."
    "name": "Tail Attack"
  - "desc": "The dragon beats its wings. Each creature within 15 ft. of the dragon must succeed on a DC 25 Dexterity saving throw or take 12 (2d6 + 5) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
    "name": "Wing Attack (Costs 2 Actions)"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/dragon/token/spawn-of-thraxes-tbvvi.webp"
```
^statblock