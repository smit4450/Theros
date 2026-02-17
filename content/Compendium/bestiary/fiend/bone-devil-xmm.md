---
title: Bone Devil
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/9
- monster/environment/nine-hells
- monster/environment/planar
- monster/size/large
- monster/type/fiend/devil
statblock: inline
aliases: ["Bone Devil"]
---
# Bone Devil
*Source: Monster Manual (2024) p. 52. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/fiend/img/bone-devil.webp#right|850)  
## Bone Devil

*Devil of Dread and Obedience*

- **Habitat.** Planar (Nine Hells)  
- **Treasure.** [[random-magic-items-implements|Implements]]  

Bone devils are gaunt, nightmarish Fiends with pallid skin stretched tight over frames that combine human and insectile features. Also known as osyluths, these Fiends command weaker devils and other beings aligned with infernal legions. Bone devils ensure that the commands of hellish sovereigns are exacted efficiently and that non-devils fulfill their commitments to the Nine Hells. They slay those who renege on infernal deals, sending treacherous mortal souls to face unspeakable punishments.

When not serving their diabolical masters, bone devils tempt self-obsessed mortals with promises of other creatures' adulation and obedience. These devils prop up petty tyrants, helping them grow increasingly calloused and amoral.

Bone devils travel across the multiverse to fulfill diabolical orders. If left with no other choices, they might conscript mortals to aid them in their vicious goals. Roll on or choose a result from the Bone Devil Objectives table to inspire a bone devil's goals.

> [!quote] A quote from Sylvira Savikas, Candlekeep Sage  
> 
> Bone devils are just one of a thousand reasons never to make a deal with a devil, but they're a significant one. Break said deal, and it'll likely be one of these nightmares that drags you down to the Nine Hells.

**Bone Devil Objectives**

| dice: 1d4 | The Bone Devil Seeks To... |
|-----------|----------------------------|
| 1 | Capture a soul that escaped the Nine Hells. |
| 2 | Convey a message or make an example of someone in the name of an archdevil. |
| 3 | Find someone who broke a deal with a devil. |
| 4 | Slay someone or steal something as part of its pact with a wicked magic-user. |
^bone-devil-objectives
```statblock
"name": "Bone Devil (XMM)"
"size": "Large"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "16"
"hp": !!int "161"
"hit_dice": "17d10 + 68"
"modifier": !!int "7"
"stats":
  - !!int "18"
  - !!int "16"
  - !!int "18"
  - !!int "13"
  - !!int "14"
  - !!int "16"
"speed": "40 ft., fly 40 ft."
"saves":
  - "strength": !!int "8"
  - "intelligence": !!int "5"
  - "wisdom": !!int "6"
  - "charisma": !!int "7"
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+7"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+6"
"damage_resistances": "cold"
"damage_immunities": "fire, poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft. (unimpeded\
  \ by magical [[darkness-rules-xphb|Darkness]]), passive\
  \ Perception 12"
"languages": "Infernal; telepathy 120 ft."
"cr": "9"
"traits":
  - "desc": "If the devil dies outside the Nine Hells, its body disappears in sulfurous\
      \ smoke, and it gains a new body instantly, reviving with all its [[hit-points-xphb|Hit Points]]\
      \ somewhere in the Nine Hells."
    "name": "Diabolical Restoration"
  - "desc": "The devil has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The devil makes two Claw attacks and one Infernal Sting attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +8, reach 10 ft. *Hit:* 13 (2d8 + 4) Slashing\
      \ damage."
    "name": "Claw"
  - "desc": "*Melee Attack Roll:* +8, reach 10 ft. *Hit:* 15 (2d10 + 4) Piercing\
      \ damage plus 18 (4d8) Poison damage, and the target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the start of the devil's next turn. While [[conditions#Poisoned|Poisoned]],\
      \ the target can't regain [[hit-points-xphb|Hit Points]]."
    "name": "Infernal Sting"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/bone-devil-xmm.webp"
```
^statblock