---
title: Hythonia
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/17
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Hythonia"]
---
# Hythonia
*Source: Mythic Odysseys of Theros p. 252*  

![](Compendium/bestiary/npc/img/hythonia.webp#right|850)  
Theros's reclusive medusas often delight in collecting and expanding their galleries of petrified victims. Unlike other medusas, Hythonia isn't merely a collector; she's an artist.

When Hythonia came to the island of Skathos, the inhabitants worshiped her as an avatar of the god Pharika. The cultists eagerly offered themselves up to the medusa's petrifying gaze in hopes of gaining Pharika's favor. Seeing herself surrounded by willing devotees, Hythonia formulated a cruel plan. After encouraging them to engage in wild rituals, Hythonia began turning her followers to stone, weaving their forms to create a grisly throne made of their petrified bodies.

While the medusa's victims have dwindled, tales of the medusa queen and the divine secrets she hoards have not. Hythonia eagerly trades the mysteries she knows but demands a constant price: a beautiful individual to become part of her throne.
```statblock
"name": "Hythonia (MOT)"
"size": "Large"
"type": "monstrosity"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "199"
"hit_dice": "21d10 + 84"
"modifier": !!int "3"
"stats":
  - !!int "21"
  - !!int "17"
  - !!int "19"
  - !!int "14"
  - !!int "16"
  - !!int "18"
"speed": "40 ft., climb 40 ft., swim 40 ft."
"saves":
  - "strength": !!int "11"
  - "constitution": !!int "10"
  - "charisma": !!int "10"
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+10"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+9"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+9"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+9"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|darkvision]] 120 ft., passive Perception\
  \ 19"
"languages": "Common"
"cr": "17"
"traits":
  - "desc": "Hythonia's spellcasting ability is Charisma (spell save DC 18). She can\
      \ innately cast [[animate-objects-xphb|animate objects]]\
      \ once per day requiring no material components.\n\n**1/day:** [[animate-objects-xphb|animate objects]]"
    "name": "Innate Spellcasting"
  - "desc": "If Hythonia fails a saving throw, she can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
  - "desc": "When a creature that can see Hythonia's eyes starts its turn within 30\
      \ feet of her, Hythonia can force it to make a DC 18 Constitution saving throw\
      \ if she isn't [[conditions#Incapacitated|incapacitated]]\
      \ and can see the creature. If the saving throw fails by 5 or more, the creature\
      \ is instantly [[conditions#Petrified|petrified]]. Otherwise,\
      \ on a failed save the creature begins to turn to stone and is [[conditions#Restrained|restrained]].\
      \ The [[conditions#Restrained|restrained]] creature must\
      \ repeat the saving throw at the end of its next turn, becoming [[conditions#Petrified|petrified]]\
      \ on a failure or ending the effect on a success. The petrification lasts until\
      \ the creature is freed by the [[greater-restoration-xphb|greater restoration]]\
      \ spell or other magic. Unless [[conditions#Surprised|surprised]],\
      \ a creature can avert its eyes to avoid the saving throw at the start of its\
      \ turn. If the creature does so, it can't see Hythonia until the start of its\
      \ next turn, when it can avert its eyes again. If the creature looks at Hythonia\
      \ in the meantime, it must immediately make the save. If Hythonia sees herself\
      \ reflected on a polished surface within 30 feet of her and in an area of bright\
      \ light, she is affected by her own gaze."
    "name": "Petrifying Gaze"
  - "desc": "If Hythonia is reduced to 0 hit points, she doesn't die or fall [[conditions#Unconscious|unconscious]].\
      \ Instead, she sheds her skin, regains 199 hit points, and moves up to her speed\
      \ without provoking opportunity attacks."
    "name": "Shed Skin (Mythic Trait; Recharges after a Short or Long Rest)"
"actions":
  - "desc": "Hythonia makes three attacks: one with her claws, one to constrict, and\
      \ one with her snaky hair."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +11 to hit, reach 5 ft., one target. *Hit:*\
      \ 9 (1d8 + 5) slashing damage plus 4 (1d8) poison damage."
    "name": "Claws"
  - "desc": "*Melee Weapon Attack:* +11 to hit, reach 15 ft., one Large or smaller\
      \ creature. *Hit:* 16 (2d10 + 5) bludgeoning damage, and the target is [[conditions#Grappled|grappled]]\
      \ (escape DC 19). Until this grapple ends, the target is [[conditions#Restrained|restrained]]\
      \ and takes 15 (3d6 + 5) bludgeoning damage at the start of each of its turns,\
      \ and Hythonia can't constrict another target."
    "name": "Constrict"
  - "desc": "*Melee Weapon Attack:* +11 to hit, reach 10 ft., one target. *Hit:*\
      \ 31 (4d12 + 5) bludgeoning damage, and Hythonia can pull the target up to\
      \ 5 feet closer to her if it is a Large or smaller creature."
    "name": "Snaky Hair"
"lair_actions":
  - "desc": "On initiative count 20 (losing initiative ties), Hythonia can take a\
      \ lair action to cause one of the following effects. She can't use the same\
      \ effect two rounds in a row:\n\n- Hythonia briefly animates creatures that\
      \ have been [[conditions#Petrified|petrified]] by her gaze.\
      \ Each statue attacks one creature within 5 feet of it, with a +11 bonus to\
      \ hit and dealing 10 (3d6) bludgeoning damage on a hit. If a Medium or smaller\
      \ creature takes this damage, it is also [[conditions#Grappled|grappled]]\
      \ (escape DC 15).  \n- Hythonia causes spectral snakes to erupt from a point\
      \ she can see within 150 feet of her. Each creature within 20 feet of that point\
      \ must succeed on a DC 19 Constitution saving throw or take 5 (2d4) piercing\
      \ damage and become [[conditions#Poisoned|poisoned]] until\
      \ the end of its next turn. While [[conditions#Poisoned|poisoned]]\
      \ in this way, the creature has disadvantage on Intelligence checks and Intelligence\
      \ saving throws, and it behaves as if under the effect of the [[confusion-xphb|confusion]]\
      \ spell.  "
    "name": ""
"regional_effects":
  - "desc": "The region containing Hythonia's lair is warped by her presence, which\
      \ creates one or more of the following effects:\n\n- A large population of snakes\
      \ dwells in the region.  \n- Trees within 1 mile of the lair are petrified wood.\
      \ Plants that stay within 500 feet of the lair for 1 day turn to stone.  \n\
      - Small bodies of water within 1 mile of the lair become poisonous. A creature\
      \ that drinks the water must succeed on a DC 19 Constitution saving throw or\
      \ become [[conditions#Poisoned|poisoned]] for 8 hours. An\
      \ affected creature can repeat the saving throw at the end of each hour.  "
    "name": ""
"legendary_description": "Legendary Action Uses: 3. Immediately after another creature's\
  \ turn, Hythonia can expend a use to take one of the following actions. Hythonia\
  \ regains all expended uses at the start of each of their turns."
"legendary_actions":
  - "desc": "Hythonia moves up to her speed without provoking opportunity attacks."
    "name": "Move"
  - "desc": "Hythonia makes one attack with her snaky hair."
    "name": "Snaky Hair"
  - "desc": "Hythonia causes stone spikes to erupt from the ground in a 30-foot radius\
      \ centered on her. The area becomes difficult terrain until the start of her\
      \ next turn. Any creature, other than Hythonia, takes 9 (2d8) piercing damage\
      \ for every 5 feet it moves on those spikes."
    "name": "Petrified Earth (Costs 2 Actions)"
"mythic_description": "If Hythonia's mythic trait is active, she can use the options\
  \ below as legendary actions for 1 hour after using Shed Skin."
"mythic_actions":
  - "desc": "Hythonia makes two attacks with her claws. If both attacks hit the same\
      \ creature, it takes an extra 7 (2d6) poison damage and must succeed on a\
      \ DC 18 Constitution saving throw or become [[conditions#Paralyzed|paralyzed]]\
      \ until the start of her next turn."
    "name": "Numbing Claws"
  - "desc": "Hythonia can force a sighted creature she has [[conditions#Grappled|grappled]]\
      \ to see her eyes and be affected by her gaze."
    "name": "Look at Me (Costs 3 Actions)"
"source":
  - "MOT"
"image": "Compendium/bestiary/npc/token/hythonia-mot.webp"
```
^statblock