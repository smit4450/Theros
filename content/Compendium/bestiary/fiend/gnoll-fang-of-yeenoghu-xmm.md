---
title: Gnoll Fang of Yeenoghu
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/4
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/size/medium
- monster/type/fiend
statblock: inline
aliases: ["Gnoll Fang of Yeenoghu"]
---
# Gnoll Fang of Yeenoghu
*Source: Monster Manual (2024) p. 141*  

![](Compendium/bestiary/fiend/img/gnolls.webp#right|850)  
Gnolls possessed by demonic vestiges of the demon lord Yeenoghu, fangs of Yeenoghu direct the chaos of gnoll packs. Along the way, these fanatics seek grisly omens from Yeenoghu and strive to interpret the demon lord's vicious goals.

## Gnolls

*Fiends in Feral Flesh*

- **Habitat.** Desert, Forest, Grassland, Hill  
- **Treasure.** [[random-magic-items-armaments|Armaments]], Individual  

The first gnolls arose from hyenas that fed on flesh tainted by the Abyss. Their corruption and violence delighted the demon lord Yeenoghu, who encouraged their numbers and spread them across the multiverse. Ever since, gnolls have been the cackling servants of Yeenoghu, existing to cause ruin and to feast on what remains.

> [!quote] A quote from Iggwilv  
> 
> Yeenoghu claims gnolls not as his brood but as maggots purposefully released to infest a despised carcass. They are a pernicious rot the Beast of Butchery spreads across mortal worlds. Whatever they once were, they were remade and are now his.

## Statblock

```statblock
"name": "Gnoll Fang of Yeenoghu (XMM)"
"size": "Medium"
"type": "fiend"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"hp": !!int "71"
"hit_dice": "11d8 + 22"
"modifier": !!int "4"
"stats":
  - !!int "17"
  - !!int "15"
  - !!int "15"
  - !!int "10"
  - !!int "11"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "constitution": !!int "4"
  - "wisdom": !!int "2"
  - "charisma": !!int "3"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 10"
"languages": "Abyssal, Gnoll"
"cr": "4"
"actions":
  - "desc": "The gnoll makes one Bite attack and two Bone Flail attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 6 (1d6 + 3) Piercing\
      \ damage plus 7 (2d6) Poison damage, and the target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the start of the gnoll's next turn."
    "name": "Bite"
  - "desc": "*Melee Attack Roll:* +5, reach 10 ft. *Hit:* 7 (1d8 + 3) Piercing\
      \ damage."
    "name": "Bone Flail"
"bonus_actions":
  - "desc": "Immediately after dealing damage to a creature that is already [[conditions#Bloodied|Bloodied]],\
      \ the gnoll moves up to half its [[speed-xphb|Speed]],\
      \ and it makes one Bite attack."
    "name": "Rampage (2/Day)"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/gnoll-fang-of-yeenoghu-xmm.webp"
```
^statblock