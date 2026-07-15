---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxxi
- monster/cr/15
- monster/size/gargantuan
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Floodtide Serpent"
---
# Floodtide Serpent
*Source: Theros Bestiary, Vol. XXI*
![](/Compendium/bestiary/monstrosity/img/floodtide-serpent.webp#center)

```statblock
"name": "Floodtide Serpent"
"size": "Gargantuan"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "560"
"hit_dice": "40d20 + 160"
"modifier": !!int "-2"
"stats":
  - !!int "18"
  - !!int "7"
  - !!int "18"
  - !!int "1"
  - !!int "8"
  - !!int "4"
"speed": "swim 120 ft."
"saves":
  - "constitution": !!int "9"
  - "wisdom": !!int "4"
"senses": "passive Perception 10"
"languages": ""
"cr": "15"
"traits":
  - "desc": "If the serpent is underwater, it stays submerged except when breaching.\
      \ After breaching, if it lands on water, it submerges once again."
    "name": "Submarine Nature"
  - "desc": "When a Large or smaller creature is bitten by the serpent, or when it\
      \ is in the serpent's path as it breaches (but before it falls), it must succeed\
      \ on a DC 11 Dexterity saving throw or be swallowed by the serpent. A swallowed\
      \ creature is blinded and restrained, it has total cover against attacks and\
      \ other effects outside the serpent, and it takes 21 (6d6) acid damage at the\
      \ start of each of the serpent's turns. If the serpent takes 30 damage or more\
      \ on a single turn from a creature inside it, the serpent must succeed on a\
      \ DC 17 Constitution saving throw at the end of that turn or regurgitate all\
      \ swallowed creatures, which fall prone in a space within 10 feet of the serpent.\
      \ If the serpent dies, a swallowed creature is no longer restrained by it and\
      \ can escape from the corpse by using 20 feet of movement, exiting prone."
    "name": "Swallow"
  - "desc": "The serpent can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 40 (8d8\
      \ + 4) piercing damage. (See the Swallow trait.)"
    "name": "Bite"
  - "desc": "The serpent breaches at a 45 degree angle to the surface, its head reaching\
      \ an apex height of 110 ft. It does this with its mouth open. It attempts to\
      \ swallow Large or smaller creatures that it intercepts this way, and bites\
      \ Huge or larger creatures. (See the Swallow trait.) It then closes its mouth\
      \ and falls back into the water, striking the surface as it does so. (See the\
      \ Splash reaction.)"
    "name": "Breach (Recharge 5-6)"
"reactions":
  - "desc": "Whenever the serpent strikes the surface of the water after a breach,\
      \ it creates a massive splash, causing the water level of all standing water\
      \ in a 100-foot cube area around it to rise by as much as 20 feet. If the area\
      \ includes a shore, the flooding water spills over onto dry land. If the serpent\
      \ isn't near land, it instead creates a 20-foot tall wave that travels from\
      \ one side of the area to the other and then crashes down. Any Huge or smaller\
      \ vehicles in the wave’s path are carried with it to the other side. Any Huge\
      \ or smaller vehicles struck by the wave have a 25 percent chance of capsizing.\
      \ Water that doesn't run off the land back into the sea gradually disappears\
      \ over the course of 2 weeks."
    "name": "Splash"
"source":
  - "TBVXXI"
```
^statblock