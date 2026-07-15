---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxvii
- monster/cr/0
- monster/size/tiny
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Charging Badger"
---
# Charging Badger
*Source: Theros Bestiary, Vol. XVII*
![](/Compendium/bestiary/beast/img/charging-badger.webp#right)

“If the hierarchies of nature were determined by ferocity alone, the badger would be lord of the beasts.” —Anthousa of Setessa

```statblock
"name": "Charging Badger"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "3"
"hit_dice": "1d4 + 1"
"modifier": !!int "1"
"stats":
  - !!int "4"
  - !!int "12"
  - !!int "12"
  - !!int "2"
  - !!int "12"
  - !!int "5"
"speed": "20 ft., burrow 5 ft., swim 15 ft."
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 30 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The badger has Advantage on Wisdom (Perception) checks that rely on smell."
    "name": "Keen Smell"
  - "desc": "If the badger moves at least 10 feet straight toward a creature and then\
      \ hits it with a claw attack on the same turn, that target must succeed on a\
      \ DC 7 Strength saving throw or be knocked prone. If the target is prone, the\
      \ badger can make one claw attack against it as a bonus action."
    "name": "Charge"
  - "desc": "The badger can move in and out of a Medium or smaller creature's space.\
      \ If it would, it uses a bonus action to attack that creature with its claw.\
      \ That creature must succeed on a DC 11 Strength saving throw or be knocked\
      \ prone. If the creature succeeds, the badger can't enter that space and must\
      \ end its turn immediately. If the badger stops on top of that creature, that\
      \ creature becomes restrained until the badger moves off it (escape DC 7)."
    "name": "Trample"
"actions":
  - "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing\
      \ damage."
    "name": "Bite"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 5 ft., one target. _Hit:_ 13\
      \ (4d4 + 3) slashing damage."
    "name": "Claw"
"source":
  - "TBVXVII"
```
^statblock