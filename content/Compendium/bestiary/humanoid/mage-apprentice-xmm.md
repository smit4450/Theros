---
title: Mage Apprentice
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/any
- monster/size/small-or-medium
- monster/type/humanoid/wizard
statblock: inline
aliases: ["Mage Apprentice"]
---
# Mage Apprentice
*Source: Monster Manual (2024) p. 198*  

![](Compendium/bestiary/humanoid/img/mage-apprentice.webp#right|850)  
Mage apprentices are spellcasters of humble skill. Some are students of accomplished mages, while others have innate powers.

## Mages

*Magical Scholars and Spellcasters*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-arcana|Arcana]], Individual  

Mages are magical wonder-workers, ranging from spellcasting overlords to reclusive witches. They study mystical secrets and possess insight into monsters, legends, omens, and other lore. Mages often gather allies or hire assistants to aid them in their research or to attain magical might.

Roll on or choose a result from the Mage Roles table to inspire different sorts of mages.

**Mage Roles**

| dice: 1d10 | The Mage Is... |
|------------|----------------|
| 1 | An astronomer who draws magic from stars. |
| 2 | An author who writes about the occult. |
| 3 | A magical engineer who creates wonders. |
| 4 | An oracle who interprets omens. |
| 5 | A prodigy with a remarkable magical heritage. |
| 6 | A psion whose powers manifest as spells. |
| 7 | A scholar investigating ancient lore. |
| 8 | A soothsayer who advises rulers. |
| 9 | A war mage who aids soldiers in battle. |
| 10 | A witch who shares secret wisdom. |
^mage-roles

> [!quote] A quote from Nathor, Thayan Refugee  
> 
> Have you gazed on the Runes of Chaos, held the Death Moon Orb in your trembling hands, entered the Devouring Portal and walked the Paths of the Doomed, or sat at the left hand of Szass Tam during the Ritual of Twin Burnings? No? Then speak not to me of wizards. Speak not to me of Thay.

![](Compendium/bestiary/humanoid/img/mages.webp#center)  
## Statblock

```statblock
"name": "Mage Apprentice (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"subtype": "wizard"
"alignment": "Neutral"
"ac": !!int "15"
"hp": !!int "49"
"hit_dice": "9d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "8"
  - !!int "14"
  - !!int "12"
  - !!int "16"
  - !!int "13"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "5"
  - "wisdom": !!int "3"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"senses": "passive Perception 13"
"languages": "Common plus one other language"
"cr": "2"
"actions":
  - "desc": "*Melee  or Ranged Attack Roll:* +5, reach 5 ft. or range 120 ft. *Hit:*\
      \ 14 (2d10 + 3) Force damage."
    "name": "Arcane Burst"
  - "desc": "The mage casts one of the following spells, using Intelligence as the\
      \ spellcasting ability (spell save DC 13, +5 to hit with spell attacks):\n\
      \n**At will:** [[mage-hand-xphb|Mage Hand]], [[prestidigitation-xphb|Prestidigitation]]\n\
      \n**1/day each:** [[disguise-self-xphb|Disguise Self]],\
      \ [[ice-knife-xphb|Ice Knife]], [[mage-armor-xphb|Mage Armor]]\
      \ (included in AC), [[thunderwave-xphb|Thunderwave]]"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/humanoid/token/mage-apprentice-xmm.webp"
```
^statblock