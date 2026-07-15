---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxiv
- monster/cr/1-8
- monster/size/medium
- monster/type/humanoid/human
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Cutthroat"
---
# Cutthroat
*Source: Theros Bestiary, Vol. XIV*
![](/Compendium/bestiary/humanoid/img/cutthroat.webp#right)

"Our ambition drives us forward. Together we will claim what is ours, no matter who holds it."

```statblock
"name": "Cutthroat"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "10"
"hit_dice": "2d8 + 2"
"modifier": !!int "1"
"stats":
  - !!int "12"
  - !!int "13"
  - !!int "13"
  - !!int "11"
  - !!int "11"
  - !!int "11"
"speed": "30 ft."
"senses": "passive Perception 10"
"languages": "Common, any one language"
"cr": "1/8"
"traits":
  - "desc": "Whenever the cutthroat deals damage to a creature, that creature makes\
      \ a DC 13 Dexterity saving throw. On a fail, the cutthroat steals 1 gp worth\
      \ of currency for every point of damage it dealt. If the defending creature\
      \ doesn't have enough currency, the cutthroat instead takes all the creature's\
      \ currency."
    "name": "Purse Slasher"
"actions":
  - "desc": "_Ranged Weapon Attack:_ +3 to hit, range 10 ft., one target. _Hit:_ 3\
      \ (1d4 + 1) slashing damage."
    "name": "Whip"
  - "desc": "_Melee or Ranged Weapon Attack:_ +3 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. _Hit:_ 3 (1d4 + 1) piercing damage in melee, or 3 (1d4 +\
      \ 1) piercing damage at range."
    "name": "Dagger"
  - "desc": "Until the beginning of the cutthroat's next turn, the next time an allied\
      \ creature would attack a creature the cutthroat could attack, the cutthroat\
      \ uses a bonus action to make one weapon attack against the defending creature.\
      \ The cutthroat and its ally each deal an extra 1 damage of the same type dealt.\
      \ Both attacks are simultaneous, and all the damage is dealt at once. The cutthroat\
      \ and the ally both gain 4 (1d8) temporary Hit Points until the beginning of\
      \ the cutthroat's next turn."
    "name": "Cutthroat Maneuver"
"source":
  - "TBVXIV"
```
^statblock