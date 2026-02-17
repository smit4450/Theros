---
title: Priest
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/any
- monster/size/small-or-medium
- monster/type/humanoid/cleric
statblock: inline
aliases: ["Priest"]
---
# Priest
*Source: Monster Manual (2024) p. 248, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/humanoid/img/priests.webp#right|850)  
Priests draw on their beliefs to heal the needful and smite their foes. They can channel their faith as spells and empower their weapons with divine might.

## Priests

*Arbiters of the Mortal and the Divine*

- **Habitat.** Any  
- **Treasure.** Individual, [[random-magic-items-relics|Relics]]  

Priests harness the power of faith to work miracles. These religious adherents are as diverse as the faiths they follow. Some obey gods and their servants, while others live by age-old creeds. Belief guides priests' actions and their magic, which they use to shape the world in line with their ideologies.

Roll on or choose a result from the Priest Roles table to inspire different sorts of priests.

**Priest Roles**

| dice: 1d10 | The Priest Is... |
|------------|------------------|
| 1 | An ascetic who keeps wicked spirits at bay. |
| 2 | An elder who speaks for the dead. |
| 3 | An exorcist who hunts wicked spirits. |
| 4 | A follower of a god no one has heard of. |
| 5 | A mediator and teacher of traditional ways. |
| 6 | A philosopher devoted to a concept, multiversal view, or plane of existence. |
| 7 | The reincarnation of an ancient faith leader. |
| 8 | A ritualist who uses tinctures and performances to access the divine. |
| 9 | A shaman whose medicines ease many ills. |
| 10 | A zealot who wages war for a divine cause. |
^priest-roles

> [!quote]  
> 
> Shining One, light my hours. Enkindle my soul, and inspire my deeds. Chase the shadows from my path, and let me walk in your brilliance.

## Statblock

```statblock
"name": "Priest (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"subtype": "cleric"
"alignment": "Neutral"
"ac": !!int "13"
"hp": !!int "38"
"hit_dice": "7d8 + 7"
"modifier": !!int "0"
"stats":
  - !!int "16"
  - !!int "10"
  - !!int "12"
  - !!int "13"
  - !!int "16"
  - !!int "13"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Medicine|Medicine]]"
    "desc": "+7"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+5"
"senses": "passive Perception 15"
"languages": "Common plus one other language"
"cr": "2"
"actions":
  - "desc": "The priest makes two attacks, using Mace or Radiant Flame in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 6 (1d6 + 3) Bludgeoning\
      \ damage plus 5 (2d4) Radiant damage."
    "name": "Mace"
  - "desc": "*Ranged Attack Roll:* +5, range 60 ft. *Hit:* 11 (2d10) Radiant damage."
    "name": "Radiant Flame"
  - "desc": "The priest casts one of the following spells, using Wisdom as the spellcasting\
      \ ability:\n\n**At will:** [[light-xphb|Light]], [[thaumaturgy-xphb|Thaumaturgy]]\n\
      \n**1/day:** [[spirit-guardians-xphb|Spirit Guardians]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The priest casts [[bless-xphb|Bless]], [[dispel-magic-xphb|Dispel Magic]],\
      \ [[healing-word-xphb|Healing Word]], or [[lesser-restoration-xphb|Lesser Restoration]],\
      \ using the same spellcasting ability as Spellcasting.\n"
    "name": "Divine Aid (3/Day)"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/humanoid/token/priest-xmm.webp"
```
^statblock