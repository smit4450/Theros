---
title: Vrock
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/6
- monster/environment/abyss
- monster/environment/planar
- monster/size/large
- monster/type/fiend/demon
statblock: inline
aliases: ["Vrock"]
---
# Vrock
*Source: Monster Manual (2024) p. 319. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/fiend/img/vrock.webp#right|850)  
## Vrock

*Demon of Carnage and Ruin*

- **Habitat.** Planar (Abyss)  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Screeching, vulturelike demons, vrocks soar from the Abyss to spread ruin and slaughter. Their filthy feathers carry magical toxins from the Lower Planes, creating a noxious cloud capable of killing those who escape the vrocks' vicious beaks and claws. To further terrorize their foes, vrocks unleash an otherworldly screech so terrible it can halt creatures in their tracks.
```statblock
"name": "Vrock (XMM)"
"size": "Large"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"hp": !!int "152"
"hit_dice": "16d10 + 64"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "15"
  - !!int "18"
  - !!int "8"
  - !!int "13"
  - !!int "8"
"speed": "40 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "5"
  - "wisdom": !!int "4"
  - "charisma": !!int "2"
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 11"
"languages": "Abyssal; telepathy 120 ft."
"cr": "6"
"traits":
  - "desc": "If the vrock dies outside the Abyss, its body dissolves into ichor, and\
      \ it gains a new body instantly, reviving with all its [[hit-points-xphb|Hit Points]]\
      \ somewhere in the Abyss."
    "name": "Demonic Restoration"
  - "desc": "The vrock has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The vrock makes two Shred attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 10 (2d6 + 3) Piercing\
      \ damage plus 10 (3d6) Poison damage."
    "name": "Shred"
  - "desc": "*Constitution Saving Throw:* DC 15, each creature in a 20-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the vrock. *Failure:* The target has the [[conditions#Poisoned|Poisoned]]\
      \ condition and repeats the save at the end of each of its turns, ending the\
      \ effect on itself on a success. While [[conditions#Poisoned|Poisoned]],\
      \ the target takes 5 (1d10) Poison damage at the start of each of its turns.\
      \ Emptying a flask of Holy Water on the target ends the effect early."
    "name": "Spores (Recharge 6)"
  - "desc": "*Constitution Saving Throw:* DC 15, each creature in a 20-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the vrock (demons succeed automatically). *Failure:* 10 (3d6)\
      \ Thunder damage, and the target has the [[conditions#Stunned|Stunned]]\
      \ condition until the end of the vrock's next turn."
    "name": "Stunning Screech (1/Day)"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/vrock-xmm.webp"
```
^statblock