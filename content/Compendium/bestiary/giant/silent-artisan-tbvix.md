---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvix
- monster/cr/18
- monster/size/gargantuan
- monster/type/giant
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Silent Artisan"
---
# Silent Artisan
*Source: Theros Bestiary, Vol. IX*
![](/Compendium/bestiary/giant/img/silent-artisan.webp#right)

On the fourth day they passed through a forest of immense stacked stones. Althemone, youngest of the companions, called these pillars the work of a god, but the Champion knew better. She quickened her pace. - The Theriad

```statblock
"name": "Silent Artisan"
"size": "Gargantuan"
"type": "giant"
"alignment": "Unaligned"
"ac": !!int "17"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "15"
  - !!int "20"
  - !!int "10"
  - !!int "12"
  - !!int "9"
"speed": "120 ft."
"saves":
  - "dexterity": !!int "8"
  - "constitution": !!int "11"
  - "wisdom": !!int "7"
"skillsaves":
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+9"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+7"
"damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Giant"
"cr": "18"
"traits":
  - "desc": "The giant has Advantage on Dexterity (Stealth) checks made to hide in\
      \ mountainous rocky terrain."
    "name": "Stone Camouflage"
  - "desc": "The artisan deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "Unless provoked, the giant ignores all nonflying things that are Huge\
      \ or smaller and all flying things that are Large or smaller."
    "name": "Titanic Nature"
"actions":
  - "desc": "Ranged Weapon Attack: +9 to hit, range 120/480 ft., one target. Hit:\
      \ 30 (6d8 + 3) bludgeoning damage. If the target is a creature, it must succeed\
      \ on a DC 17 Strength saving throw or be knocked prone."
    "name": "Boulder"
"reactions":
  - "desc": "If a rock or similar object is hurled at the giant, the giant can, with\
      \ a successful DC 16 Dexterity saving throw, catch the missile and take no bludgeoning\
      \ damage from it."
    "name": "Rock Catching"
"source":
  - "TBVIX"
```
^statblock