---
title: Quasit
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1
- monster/environment/abyss
- monster/environment/planar
- monster/size/tiny
- monster/type/fiend/demon
statblock: inline
aliases: ["Quasit"]
---
# Quasit
*Source: Monster Manual (2024) p. 252, Player's Handbook (2024) p. 355, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/books/monster-manual-2025/img/quasit.webp#right)  
## Quasit

*Demon of Discord and Disorder*

- **Habitat.** Planar (Abyss)  
- **Treasure.** None  

Tirelessly destructive, quasits sow discord through nasty pranks, sabotage, and ambushes. These tiny demons use chaos and violence to terrorize others. By shape-shifting into harmless but ill-omened creatures or by turning [[conditions#Invisible|invisible]], quasits sneak into places where they spy for villainous masters or set vicious traps. Quasits delight in hiding in dark places and—when least expected—bursting forth to slash foes with their [[conditions#Poisoned|poisoned]] claws.

Quasits are usually overlooked and underestimated by other demons. This drives them to prove themselves through cruel acts or by seeking paths to the Material Plane. Among mortals, quasits sow senseless chaos, and they might find kindred evil spirits among violent cultists and magic-users.

> [!quote] A quote from Otto the Bard  
> 
> A thing doesn't need to be big to be gut-flippingly dreadful. Just think of all the folks who're squeamish around spiders. Now imagine a spider as big as a cat and that wants to steal your tongue.

```statblock
"name": "Quasit (XMM)"
"size": "Tiny"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"hp": !!int "25"
"hit_dice": "10d4"
"modifier": !!int "3"
"stats":
  - !!int "5"
  - !!int "17"
  - !!int "10"
  - !!int "7"
  - !!int "10"
  - !!int "10"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 10"
"languages": "Abyssal, Common"
"cr": "1"
"traits":
  - "desc": "The quasit has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 5 (1d4 + 3) Slashing\
      \ damage, and the target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the start of the quasit's next turn."
    "name": "Rend"
  - "desc": "*Wisdom Saving Throw:* DC 10, one creature within 20 feet. *Failure:*\
      \ The target has the [[conditions#Frightened|Frightened]]\
      \ condition. At the end of each of its turns, the target repeats the save, ending\
      \ the effect on itself on a success. After 1 minute, it succeeds automatically."
    "name": "Scare (1/Day)"
  - "desc": "The quasit shape-shifts to resemble a bat ([[speed-xphb|Speed]]\
      \ 10 ft., Fly 40 ft.), a centipede (40 ft., Climb 40 ft.), or a toad (40 ft.,\
      \ Swim 40 ft.), or it returns to its true form. Its game statistics are the\
      \ same in each form, except for its [[speed-xphb|Speed]].\
      \ Any equipment it is wearing or carrying isn't transformed."
    "name": "Shape-Shift"
  - "desc": "The quasit casts [[invisibility-xphb|Invisibility]]\
      \ on itself, requiring no spell components and using Charisma as the spellcasting\
      \ ability.\n"
    "name": "Invisibility"
"source":
  - "XMM"
  - "XPHB"
  - "FRHoF"
"image": "Compendium/bestiary/fiend/token/quasit-xmm.webp"
```
^statblock