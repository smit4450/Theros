---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvix
- monster/cr/23
- monster/size/gargantuan
- monster/type/giant/cyclops
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Thunder Brute"
---
# Thunder Brute
*Source: Theros Bestiary, Vol. IX*
![](/Compendium/bestiary/giant/img/thunder-brute.webp#center)

```statblock
"name": "Thunder Brute"
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
"condition_immunities": "[deafened](/Compendium/rules/conditions.md#Deafened)"
"senses": "passive Perception 10"
"languages": "Giant"
"cr": "23"
"traits":
  - "desc": "At the start of each of the cyclops's turns, each grounded creature within\
      \ 5 feet of it takes 10 (3d6) lightning damage, and flammable objects in the\
      \ aura that aren't being worn or carried ignite. A creature that touches the\
      \ cyclops or hits it with a melee attack while within 5 feet of it takes 10\
      \ (3d6) lightning damage."
    "name": "Lightning Aura"
  - "desc": "The cyclops has Disadvantage on any attack roll against a target more\
      \ than 30 feet away."
    "name": "Poor Depth Perception"
  - "desc": "The cyclops can move in and out of a Huge or smaller creature's space.\
      \ If it would, it uses a bonus action to attack that creature with its unarmed\
      \ strike. That creature must succeed on a DC 15 Strength saving throw or be\
      \ knocked prone. If the creature succeeds, the cyclops can't enter that space\
      \ and must end its turn immediately. If the cyclops stops on top of that creature,\
      \ that creature becomes restrained until the cyclops moves off it (escape DC\
      \ 15)."
    "name": "Trample"
"actions":
  - "desc": "The cyclops makes two unarmed strikes."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 30 (10d4\
      \ + 5) bludgeoning damage."
    "name": "Unarmed Strike"
  - "desc": "The cyclops hurls a magical lightning bolt at a point it can see within\
      \ 500 feet of it. Each creature within 10 feet of that point must make a DC\
      \ 17 Dexterity saving throw, taking 54 (12d8) lightning damage on a failed save,\
      \ or half as much damage on a successful one."
    "name": "Lightning Strike (Recharge 5-6)"
  - "desc": "The cyclops claps its hands together. Each creature within a 20-foot\
      \ radius from the cyclops takes 10 (1d10+5) thunder damage."
    "name": "Thunderclap (Recharge 4-5)"
"reactions":
  - "desc": "Immediately after initiative rolls in which the cyclops participates,\
      \ it demands tribute from a creature it can see. That creature may bow, genuflect,\
      \ salute, or perform a similar gesture as a bonus action. If tribute is paid:\
      \ Until the end of combat, the cyclops gains a permanent +3 bonus to damage\
      \ rolls and Strength and Dexterity checks, and 315 (30d20) temporary Hit Points.\
      \ If tribute isn't paid: The cyclops pounds the earth, dealing 30 (10d4+5) thunder\
      \ damage to every creature and object on the ground (including walls) within\
      \ a 15-foot radius."
    "name": "Demand Tribute"
"source":
  - "TBVIX"
```
^statblock