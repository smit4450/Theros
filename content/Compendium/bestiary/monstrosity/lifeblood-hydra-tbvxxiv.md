---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxxiv
- monster/cr/5
- monster/size/huge
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Lifeblood Hydra"
---
# Lifeblood Hydra
*Source: Theros Bestiary, Vol. XXIV*
![](/Compendium/bestiary/monstrosity/img/lifeblood-hydra.webp#center)

```statblock
"name": "Lifeblood Hydra"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "55"
"hit_dice": "5d12 + 25"
"modifier": !!int "1"
"stats":
  - !!int "21"
  - !!int "12"
  - !!int "21"
  - !!int "2"
  - !!int "10"
  - !!int "7"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+6"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "5"
"traits":
  - "desc": "When the hydra takes piercing or slashing damage, each creature within\
      \ 5 feet of it regains 9 (2d8) Hit Points."
    "name": "Healing Blood"
  - "desc": "The hydra can hold its breath for 1 hour."
    "name": "Hold Breath"
  - "desc": "The hydra has five heads. While it has more than one head, the hydra\
      \ has Advantage on saving throws against being blinded, charmed, deafened, frightened,\
      \ stunned, and knocked unconscious. Whenever the hydra takes 11 or more damage\
      \ in a single turn, one of its heads dies. If all its heads die, the hydra dies.\
      \ At the end of its turn, it grows two heads for each of its heads that died\
      \ since its last turn, unless it has taken fire damage since its last turn.\
      \ The hydra regains 11 Hit Points for each head regrown in this way."
    "name": "Multiple Heads"
  - "desc": "For each head the hydra has beyond one, it gets an extra reaction that\
      \ can be used only for opportunity attacks."
    "name": "Reactive Heads"
  - "desc": "The hydra can move in and out of a Medium or smaller creature's space.\
      \ If it would, it uses a bonus action to attack that creature with its stomp\
      \ attack. That creature must succeed on a DC 16 Strength saving throw or be\
      \ knocked prone. If the creature succeeds, the hydra can't enter that space\
      \ and must end its turn immediately. If the hydra stops on top of that creature,\
      \ that creature becomes restrained until the hydra moves off it (escape DC 16)."
    "name": "Trample"
  - "desc": "While the hydra sleeps, at least one of its heads is awake."
    "name": "Wakeful"
"actions":
  - "desc": "The hydra makes as many bite attacks as it has heads."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 10 (1d10\
      \ + 5) piercing damage."
    "name": "Bite"
  - "desc": "_Melee Weapon Attack:_ +8 to hit, reach 5 ft., one target. _Hit:_ 7 (1d4\
      \ + 5) bludgeoning damage."
    "name": "Stomp"
"source":
  - "TBVXXIV"
```
^statblock