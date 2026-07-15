---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxxiv
- monster/cr/22
- monster/size/gargantuan
- monster/type/monstrosity/hydra
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Heroes' Bane"
---
# Heroes' Bane
*Source: Theros Bestiary, Vol. XXIV*
![](/Compendium/bestiary/monstrosity/img/heroes-bane.webp#center)

```statblock
"name": "Heroes' Bane"
"size": "Gargantuan"
"type": "monstrosity"
"subtype": "hydra"
"alignment": "Unaligned"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "560"
"hit_dice": "40d20 + 160"
"modifier": !!int "0"
"stats":
  - !!int "19"
  - !!int "10"
  - !!int "19"
  - !!int "2"
  - !!int "10"
  - !!int "7"
"speed": "40 ft., swim 40 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+7"
"damage_immunities": "acid"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "22"
"traits":
  - "desc": "When the hydra takes piercing or slashing damage, each creature within\
      \ 5 feet of the hydra takes 9 (2d8) acid damage."
    "name": "Acidic Blood"
  - "desc": "The hydra can hold its breath for 1 hour."
    "name": "Hold Breath"
  - "desc": "The hydra has four heads. While it has more than one head, the hydra\
      \ has Advantage on saving throws against being blinded, charmed, deafened, frightened,\
      \ stunned, or knocked unconscious. Whenever the hydra takes 150 or more damage\
      \ in a single turn, one of its heads dies. If all its heads die, the hydra dies.\
      \ At the end of its turn, it grows two heads for each of its heads that died\
      \ since its last turn, unless it has taken fire damage since its last turn.\
      \ The hydra regains 50 Hit Points for each head regrown in this way."
    "name": "Multiple Heads"
  - "desc": "For each head the hydra has beyond one, it gets an extra reaction that\
      \ can be used only for opportunity attacks."
    "name": "Reactive Heads"
  - "desc": "While the hydra sleeps, at least one of its heads is awake."
    "name": "Wakeful"
"actions":
  - "desc": "The hydra makes as many bite attacks as it has heads."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 48 (8d10\
      \ + 6) piercing damage."
    "name": "Bite"
"source":
  - "TBVXXIV"
```
^statblock