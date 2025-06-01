

# Map

- Is made up of a single board with 3 lanes and 4 jungle areas
- Divided into two halves; blue and red side
- Each half is split into 3 bands to represent movement tiles
	- Band 1
		- Base
	- Band 2
		- Second tower
	- Band 3
		- First tower
	
- Bands 1 and 2 are further cut into 5 tiles to separate the bands vertically
- Each side has 8 towers
	- 2 in each lane
	- 2 in front of Nexus
	
	
	
# Rules

## Objective 
- Be the first player to destroy the enemy Nexus
- To reach the Nexus you must destory all towers in at least one lane and both towers defending the Nexus


## Card hand
- Each player can hold up to 5 cards. This is called the `LIMIT`
	- Some passive or item effects can increase the `LIMIT`
- Players should start by drawing cards equal to the `LIMIT`
- Players will draw 1 or more cards per turn depending on the number of cards currently in their hand
	- You can always draw cards up until your `LIMIT`
	- If you are already at your `LIMIT` then draw 1 card


## Preparation
- Set out the shop cards so that they are available to both players
- Set the tower markers on the map
- Set the champion cards face up and visible to both players
- Set the champion tokens corresponding to the champion cards so that they are available to both players
- Set out 5 champion boards (health and ultimate cooldown spinners)
- Players draw to their hand `LIMIT` [Card Hand](#card-hand)
- Set out gold tokens


## Draft 
- Players will go through `Pick` and `Ban` stages
- Blue side always picks first
- The stages are: 
```
Ban stage 1
|  Blue  |  1 champion  |
|  Red   |  2 champions |
|  Blue  |  1 champion  |

Pick stage 1
|  Blue  |  1 champion  |
|  Red   |  2 champions |
|  Blue  |  2 champions |
|  Red   |  1 champion  |

Ban stage 2
|  Red   |  1 champion  |
|  Blue  |  1 champion  |

Pick stage 2
|  Blue  |  1 champion  |
|  Red   |  2 champions |
|  Blue  |  1 champion  |
```
- When a champion is `banned` move that card to the side so that it's visible to both players
- When a champion is `picked` the player should take the card and corresponding champion token and move it to their side of the board and make it visible to both players


## Starting positions
- Starting with the Blue player
- Take turns placing each champion's token at the first tower of a lane on the respective sides of the map
- Once the last champion has been placed in their lane the game starts

## Phases

### Draw
- The player draws up to their card `LIMIT` 
- If at their `LIMIT` already then only draw 1 card


### Farming gold
- Gain gold for each champion that's alive in a Zone with minions or jungle mobs
- Jungle mobs exist in the jungle zones
- Minions exist at the most-outer standing `Tower`
- See [Splitting Gold](#splitting-gold) for rules when multiple champions are in the same zone


### Movement
- One at a time on each champion the player can decide to move them or not
- By default, champions can only move 1 tile per turn
- If a player decides to move a champion then they must move the token to the adjacent target tile
- If a player is [Recalling](#recalling) then the token should be placed at the edge of the current tile nearest the player's Nexus
<!-- - If a player decides to move a champion to an unwarded zone with no champions currently occupying it, then instead of moving the champion token and revealing which zone you have moved to, simply flip over the token to show the `MISSING` face.   -->


#### Ganking
- To gank a lane a champion must be in an adjacent tile
- Move the champion to the desired lane 
- Roll a dice
- On a 3+ the ganker can join the battle phase and deal damage to enemy champions in the lane


#### Play style
- Champions in lane can choose to fight in 3 different ways; Playing Safe, Normal, Aggressive 

- Safe 			= 		-1 to Gold Income and -1 to enemy Gank attempts
- Aggressive	= 		-1 to Gold Income, +1 additional rolls on attacks, +1 to enemy gank attempts


### Battle
- The battle phase takes place in one lane at a time
- The current turn's player decides the order to take their battles
- If a lane has more than 1 of the player's champions, the player can decide which order the champion's attack in
- The `Battle` phase is made of a rotating `Attack` and `Defense` stage where, starting with the attacking player, champions take turns doing and receiving damage. E.g:
```
Battle in the bot lane
Both players have 2 champions
It's player 1's turn so they decide which of their champions attack's first
Attack damage is calculated and dealt to enemy champion's
Player 2 then decides how to split the damage across their champions
Then it's player 2's turn to attack with one of their champions. 
Player 1 then defends.
Repeat until all champions have made their attacks
```
- A player does not *have* to start a battle in a lane, or attack with every champion. They can pass if they want. 
- Some ultimates e.g. [Anivia](#anivia) are not just additive damage. These ultimates should be handled as a separate effect. But must be played during the declared champion's `Attack` or `Defense` stage. 


#### Attack stage
- Choose a target for your attack 
- An attack consists on a champion's attack damage + a number of dice rolls called Additional Hits
- For each 4+ dice roll add 1 damage
- Attacks and Champion Abilities / Ultimates that deal damage are performed in the same Attack Stage
- They are however treated as different attacks, therefore if a champion has an item that reduces your damage by 1, that is 1 per attack type; attack, ability, ultimate
- This also means you can use your attacks, abilities and ultimates on different targets


#### Defense stage
- If the defending player has a Tank in the same zone they can choose to allocate the damage to them
- Damage is first dealt to the Armour of a champion
- After all the armour has been lost the damage starts being dealt to the health
- Champion Armour refreshes at the start of that player's next turn but champion health can only be recovered by healing or recalling


#### Hitting in Tower range
- Extra move usuable at the end of the fighing phase
- The target enemy must be at or below 2 health
- Enemy champion must be in the same tile
- Current tile must have an active tower

- Charge the enemy under their tower
- Roll a dice and follow the below table to determine the outcome
```
| Roll    | Damage dealt  | Damage taken  |
|---------|---------------|---------------|
|  1,2,3  |       0       |       2       |
|    4    |       1       |       2       |
|    5    |       1       |       1       |
|    6    |       2       |       0       |
```
- If a champion is Tower diving both enemy base towers roll a second dice
- A champion does not deal extra damage with the second roll
- The roll determines if the champions takes more damage
- If you deal damage to the base towers the attacking player can choose which tower takes the damage


### Smite
- The Smite phase occurs after all Battle phases are complete
- Champions who have died during the Battle phase cannot Smite


### End
- Handle any `Passive` effects
- Handle any [Champion Deaths](#champion-death)
- Gain rewards for killed champions


## Earning gold

### Passives
- A number of passives can earn gold
- They should be handled at the start of a player's turn

### Killing minions
- Champions earn gold by killing minions in lane
- The champion must be in the outer-most zone that has a standing tower in their lane
- At the end of the player's turn, the player can claim the gold from their [Farming income](#farming-gold) stat
- See [Splitting gold](#splitting-gold) section for situations where multiple champions are in a lane

### Killing jungle mobs
- Monsters spawn in the jungle areas
- Whilst a Jungle-type champion is in the jungle they will earn gold at the end of the player's turn

### Killing champions
- When an enemy champion's health has been reduced to 0 that champion dies
- Send the champion back to their base and collect gold
```
First blood = 5g
Kill = 3g
```

### Destroying towers
- When an enemy champion is out of lane you may choose to hit the tower
- When the tower has been reduced to 0 life it is destroyed
- Gold is granted to the champions in the lane. The total remains the same but the player can choose how to divide it among those champions.
- When attacking a tower perform a dice roll for each champion in the zone
- On a 3 or below that champion takes 1 damage
```
Tower kill = 4g
```

### Splitting gold
- If two champions occupy a lane they do not both collect 
- The player must choose which champion receives the gold
- Gold cannot be divided among champions
- The exception to this rule is are Support-type champions who receive their gold income regardless of how many other champions are in the same zone


# Recalling
- Recalling costs the champion their movement turn
- Move the champion token to the edge of the current zone
- At the start of their next turn the champion teleports to the base
- Gold from minions is earned whilst recalling
- Recalling champions cannot be attacked except by abilties/ultimates that state such. The only other way to attack a recalling champion is a Tower Dive
- A successful dive cancels a recall even if it doesn't kill the champion


## Buying items
- Champion must be in the base to buy items
- A champion can hold up to 6 items


# Champion Death
- When a champion dies they return to their base zone
- At the start of their next turn the champion respawns and can make a movement


# Smite
- Killing an Epic monster is performed during the Smite stage
- Non-Jungler type champions do not have Smite and therefore contribute 1 to the Smite roll
- Jungler type champions have Smite and control 6 to the Smite roll
- Both players roll 2 dice each
- Add the result and Smite contribution of all allies witin the zone
- The highest result wins the Smite and secures the Epic monster kill

# Ending a game
- The game ends when one Nexus has been destroyed
- In order to hit a Nexus all the towers in at least one lane must be destroyed
- And both base towers must be destroyed

# Cards

### Focus
- Specify which enemy champion takes damage

### Attack
- Add 1 to attack

### Block
- Add 1 to defense

### Sacrifice
- Nominate any of your living champions in the lane to receive the damage of the next attack, even if they have already been nominated to receive damage this turn

### Flash
- Flash away out of reach of the enemy's attacks. Any damage that they would have done to you is negated
- *Beware: If the enemy also uses Flash they will catch up and the damage will still apply*
- Multiple Flash cards may be played 

### Teleport
- Immediately return to a lane with an active friendly `Tower`

<!-- ### Ward
- Place a ward token on any Zone on the map
- Whilst the ward is active, allow sight of a hidden character if they are in or pass through that Zone

### Oracle's lens
- Destory any ward in the Zone currently occupied by one of your champions -->

### Barrier
- Apply a defensive aura to absorb 2 damage from damage this turn
- Only one barrier may be used per champion per turn

### Demolish
- During your attack on a tower add 3 damage to the attack

### Counter-gank
- Usable during the opponent's movement phase
- If the opponent moves an additional champion into a lane or jungle zone
- Move one of your champions from an adjacent zone into the one being attacked


# Champion stats


### Health
- The total amount of health a champion can have
- Set health value to full at the start of the game and on any recalls or respawns

### Attack
- The base damage the champion deals during an `Attack` stage

### Defense
- The amount of damage a champion can receive before their health starts being used
- Defense shields refresh at the start of the player's next turn

### Gold income
- The amount of gold received per turn if the champion is in a Zone with minions or jungle mobs
- Jungle mobs exist in the jungle zones
- Minions exist at the most-outer `Tower` that is standing in a lane

### Passive
- Special effects that can be used at different phases of the game
- Each `Passive` displays in what phase it can be used

### Ultimate
- Special ability that can be used at different phases of the game
- Most `Ultimates` are used during the [Battle](#battle) phase but some may be used at other times
- Shows the number of turns it takes to `Cooldown` before it can be used again


# Champion list

- Ornn
- Malphite
- Shen
- Poppy

- Nocturne
- Fiddlesticks
- Lee Sin

- Sylas
- Anivia
- Twisted Fate
- Zed

- Vayne
- Jinx
- Jhin
- Ashe

- Yuumi
- Soraka
- Rakan
- Taric

