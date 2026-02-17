---
title: Guardian Naga
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/10
- monster/environment/desert
- monster/environment/forest
- monster/environment/planar
- monster/environment/upper
- monster/size/large
- monster/type/celestial
statblock: inline
aliases: ["Guardian Naga"]
---
# Guardian Naga
*Source: Monster Manual (2024) p. 161. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/celestial/img/guardian-naga.webp#right|850)  
## Guardian Naga

*Enduring Serpentine Lore Keeper*

- **Habitat.** Desert, Forest, Planar (Upper Planes)  
- **Treasure.** [[random-magic-items-relics|Relics]]  

Guardian nagas are immortal, serpentine scholars that possess perfect memories. They collect the histories and lore of those they live among, guarding cultures' stories and passing them on to new generations with infallible accuracy. Guardian nagas that outlive their host civilizations might linger in whatever ruins remain, preserving the civilizations' stories so their lost people might live on.

Roll on or choose a result from the Guardian Naga Lore table to inspire what a naga knows.

**Guardian Naga Lore**

| dice: 1d8 | The Guardian Naga Recalls... |
|-----------|------------------------------|
| 1 | The last words of an ancient sage or leader. |
| 2 | The location of a hidden city or continent. |
| 3 | A magic word, password, or riddle's answer. |
| 4 | The names of all who have told it stories. |
| 5 | An otherwise forgotten ritual or spell. |
| 6 | Recipes using regional ingredients. |
| 7 | Stories of forgotten gods and local spirits. |
| 8 | The vulnerabilities of a legendary monster. |
^guardian-naga-lore
```statblock
"name": "Guardian Naga (XMM)"
"size": "Large"
"type": "celestial"
"alignment": "Lawful Good"
"ac": !!int "18"
"hp": !!int "136"
"hit_dice": "16d10 + 48"
"modifier": !!int "4"
"stats":
  - !!int "19"
  - !!int "18"
  - !!int "16"
  - !!int "16"
  - !!int "19"
  - !!int "18"
"speed": "40 ft., climb 40 ft., swim 40 ft."
"saves":
  - "dexterity": !!int "8"
  - "constitution": !!int "7"
  - "intelligence": !!int "7"
  - "wisdom": !!int "8"
  - "charisma": !!int "8"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+11"
  - "name": "[[skills#History|History]]"
    "desc": "+11"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+11"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Paralyzed|paralyzed]],\
  \ [[conditions#Poisoned|poisoned]], [[conditions#Restrained|restrained]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 14"
"languages": "Celestial, Common"
"cr": "10"
"traits":
  - "desc": "If the naga dies, it returns to life in 1d6 days and regains all its\
      \ [[hit-points-xphb|Hit Points]] unless [[dispel-evil-and-good-xphb|Dispel\
      \ Evil and Good]] is cast on\
      \ its remains."
    "name": "Celestial Restoration"
"actions":
  - "desc": "The naga makes two Bite attacks. It can replace any attack with a use\
      \ of Poisonous Spittle."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +8, reach 10 ft. *Hit:* 17 (2d12 + 4) Piercing\
      \ damage plus 22 (4d10) Poison damage."
    "name": "Bite"
  - "desc": "*Constitution Saving Throw:* DC 16, one creature the naga can see within\
      \ 60 feet. *Failure:* 31 (7d8) Poison damage, and the target has the [[conditions#Blinded|Blinded]]\
      \ condition until the start of the naga's next turn. *Success:* Half damage\
      \ only."
    "name": "Poisonous Spittle"
  - "desc": "The naga casts one of the following spells, requiring no Somatic or Material\
      \ components and using Wisdom as the spellcasting ability (spell save DC 16):\n\
      \n**At will:** [[thaumaturgy-xphb|Thaumaturgy]]\n\n**1/day\
      \ each:** [[clairvoyance-xphb|Clairvoyance]], [[cure-wounds-xphb|Cure Wounds]]\
      \ (level 6 version), [[flame-strike-xphb|Flame Strike]]\
      \ (level 6 version), [[geas-xphb|Geas]], [[true-seeing-xphb|True Seeing]]"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/celestial/token/guardian-naga-xmm.webp"
```
^statblock