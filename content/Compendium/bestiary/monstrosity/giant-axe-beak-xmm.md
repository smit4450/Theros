---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/5
- monster/environment/arctic
- monster/environment/grassland
- monster/environment/hill
- monster/size/huge
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Giant Axe Beak"
---
# Giant Axe Beak
*Source: Monster Manual (2024) p. 24*
![](/Compendium/bestiary/monstrosity/img/axe-beak.webp#right)

Giant axe beaks typically dwell in secluded, primeval realms, such as isolated islands or underground wildernesses. They often compete with dinosaurs and other giant beasts for territory.

## Axe Beaks

*Flightless Avian Predators*

- **Habitat.** Arctic, Grassland, Hill  
- **Treasure.** None  

Axe beaks are flightless, birdlike creatures with distinctive axe-shaped beaks. Swift predators, they chase down prey and use their beaks to hack through foliage protecting their quarry. Axe beaks live in varied environments. Colorfully plumed axe beaks race across tropical plains, while axe beaks with snowy feathers hunt the tundra.

Axe beaks are difficult to train, but those hatched and raised in captivity can become reliable mounts.

> [!quote] A quote from Batley Summerfoot, Adventurer  
> 
> The thing's got an axe for a face and a giant, angry rooster for everything else—of course I want to ride it!


## Statblock

```statblock
"name": "Giant Axe Beak"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "84"
"hit_dice": "8d12 + 32"
"modifier": !!int "5"
"stats":
  - !!int "21"
  - !!int "14"
  - !!int "19"
  - !!int "3"
  - !!int "12"
  - !!int "5"
"speed": "50 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"senses": "passive Perception 14"
"languages": ""
"cr": "5"
"actions":
  - "desc": "The axe beak makes one Sharpened Beak attack and one Talons attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +8, reach 10 ft. *Hit:* 18 (2d12 + 5) Slashing damage,\
      \ and a creature within 5 feet of the target (axe beak's choice) takes 6 (1d12)\
      \ Slashing damage."
    "name": "Sharpened Beak"
  - "desc": "*Melee Attack Roll:* +8, reach 5 ft. *Hit:* 14 (2d8 + 5) Piercing damage.\
      \ If the target is a Large or smaller creature, it has the [Prone](/Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Talons"
"source":
  - "XMM"
"image": "/Compendium/bestiary/monstrosity/token/giant-axe-beak-xmm.webp"
```
^statblock

## Environment

arctic, grassland, hill