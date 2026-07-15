---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvvi
- monster/cr/5
- monster/size/medium
- monster/type/celestial
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Ornitharch"
---
# Ornitharch
*Source: Theros Bestiary, Vol. VI*
![](/Compendium/bestiary/celestial/img/ornitharch.webp#center)

```statblock
"name": "Ornitharch"
"size": "Medium"
"type": "celestial"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "plate"
"hp": !!int "112"
"hit_dice": "16d8 + 48"
"modifier": !!int "3"
"stats":
  - !!int "17"
  - !!int "17"
  - !!int "17"
  - !!int "15"
  - !!int "21"
  - !!int "17"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "8"
  - "charisma": !!int "6"
  - "strength": !!int "6"
  - "constitution": !!int "6"
"skillsaves":
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+8"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+8"
  - "name": "[History](/Compendium/rules/skills.md#History)"
    "desc": "+5"
  - "name": "[Animal Handling](/Compendium/rules/skills.md#Animal%20Handling)"
    "desc": "+8"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](/Compendium/rules/conditions.md#Frightened)"
"senses": "[truesight](/Compendium/rules/senses.md#Truesight) 120 ft., passive Perception\
  \ 10"
"languages": "all"
"cr": "5"
"traits":
  - "desc": "The ornitharch's innate spellcasting ability is Charisma (spell save\
      \ DC 13, +6 to hit with spell attacks). It can innately cast the following spells,\
      \ requiring no material components: At will: True Strike 3/day: _animal messenger_,\
      \ Conjure Animals (doves), Speak With Animals"
    "name": "Innate Spellcasting"
  - "desc": "If the ornitharch isn’t controlling a vehicle, it can use a bonus action\
      \ to magically teleport into its vehicle, provided the ornitharch and its vehicle\
      \ are on the same plane of existence. When it teleports, the ornitharch appears\
      \ in the vehicle, along with any equipment it is wearing or carrying. While\
      \ controlling the vehicle and not incapacitated, the ornitharch can’t be surprised,\
      \ and both it and its vehicle have Advantage on Dexterity saving throws. If\
      \ the ornitharch is reduced to 0 Hit Points while controlling its vehicle, the\
      \ vehicle is reduced to 0 Hit Points as well."
    "name": "Pilot"
  - "desc": "The ornitharch has proficiency with flying vehicles."
    "name": "Vehicle Proficiency"
"actions":
  - "desc": "_Melee or Ranged Weapon Attack:_ +6 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. _Hit:_ 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing\
      \ damage if used with two hands to make a melee attack."
    "name": "Spear"
"reactions":
  - "desc": "Immediately after initiative rolls in which the ornitharch participates,\
      \ it demands tribute from a creature it can see. That creature may bow, genuflect,\
      \ salute, or perform a similar gesture as a bonus action. If tribute is paid:\
      \ Until the end of combat, the ornitharch gains a +2 bonus to damage rolls and\
      \ Strength and Dexterity checks, and 9 (2d8) temporary Hit Points. If tribute\
      \ isn't paid: The ornitharch summons 9 (2d8) **doves** that appear in unoccupied\
      \ spaces that the ornitharch can see within 120 feet of itself. The summoned\
      \ doves act as allies to their summoner and its allies."
    "name": "Demand Tribute"
"source":
  - "TBVVI"
```
^statblock