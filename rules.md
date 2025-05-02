

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


## Deciding turn order
- The player with the highest *total* initiative goes first
- If initiative is tied then the player who lost the last game goes first
- If it's the first game of a series; flip a coin / roll dice / gentlemen's agreement


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
- If a player is [Recalling ](#recalling) then the token should be placed at the edge of the current tile nearest the player's Nexus
<!-- - If a player decides to move a champion to an unwarded zone with no champions currently occupying it, then instead of moving the champion token and revealing which zone you have moved to, simply flip over the token to show the `MISSING` face.   -->


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
- The attacking player can play any number of attack augmentation cards from their hand
- Calculate the total damage of the champion including their attack stat, items and augmentation cards
- Declare the amount of damage you will do to the enemy champions in the lane


#### Defense stage
- The defending player can decide which of their champions is the target of the damage
- A player may only nominate a champion to be the target of damage once per `Battle`
- In cases where there are fewer defenders than attackers `e.g. 3v4`, the nominations are rotational. The defender must have each of their champions be nominated to receive damage before it resets and you can go back to the first champion. 
- The defending player can play any number of defense augmentation cards from their hand
- Be aware of `targeted damage` from Passives or from the [Focus](#focus) card. This may allow a champion's damage to specifically hit one of the opponent's champions. E.g:
```
You have a Zed that uses the `Assassinate` passive to deal his damage directly to the enemy Vayne, dealing 10 damage. In this case your opponent must have their Vayne handle the 10 damage and not split it among other champions in the lane.
```
- There is no need to specify the order of defensive cards such as [Barrier](#barrier) or the champion's that have heal, these effects are considered to work between damage being dealt. E.g:
```
Zed deals 10 damage to Vayne who has 9 life remaining, however the Soraka uses her ultimate to heal the Vayne for 2 health. Even if Vayne was technically full life, the heal will still mitigate the damage making Zed do an effective 8 damage and therefore the Vayne would survive.
```
- If the damage exceeds the the defense then deal the difference in damage to the selected champion and reduce their health accordingly. 


### Smite
- The Smite phase occurs as after Battle phases are complete
- Champions who have died during the Battle phase cannot Smite


### End
- Handle any `Passive` effects
- Handle any [Champion Deaths](#champion-death)
- Gain rewards for killed champions


## Earning gold

- Gold is central store held by the player, not the specific champions
- Gold earned from one lane can be used to buy items for champions in another lane

### Passives
- A number of passives can earn gold
- They should be handled at the start of a player's turn

### Killing minions
- Champions earn gold by killing minions in lane
- The champion must be in the outer-most zone that has a standing tower in their lane
- Once per turn, either at the start or the end, the player can claim the gold from their [Farming income](#farming-gold) stat
- See [Splitting gold](#splitting-gold) section for situations where multiple champions are in a lane

### Killing jungle mobs
- Monsters spawn in the jungle areas
- On each quandrant there are 2 jungle camps each taking 1 turn to kill
- For each jungle camp earn the amount of gold for the champion's [Farming income](#farming-gold) stat
- Once a quandrant has been cleared the camps will not respawn until the champion has left the zone

### Killing champions
- When an enemy champion's health has been reduced to 0 that champion dies
- Send the champion back to their base and collect gold
```
First blood = 4g
Kill = 3g
```

### Destorying towers
- When an enemy champion is out of lane you may choose to hit the tower
- When the tower has been reduced to 0 life it is destroyed
- Earn gold for the player's team
```
Tower kill = 4g
```

### Splitting gold
- If two champions occupy a lane they do not both collect the maximum amount of gold
- Choose the highest [Farming income](#farming-gold) and then add 1 for every friendly champion in the same zone. 
```
Anivia has a gold farming stat of 4g per turn
Vayne has a gold farming stat of 3g per turn
If Vayne joins the same lane as Anivia then the gold earned by turn for that zone would be 4g + 1g
```
- The exception to this rule is any champion that has the `Support` passive
- A `Support` will earn their [Farming income](#farming-gold) stat regardless of how many other champions are in the same zone


# Recalling
- Recalling costs the champion their movement turn
- Move the champion token to the edge of the current zone
- At the start of their next turn the champion teleports to the base


## Buying items
- Items can only be bought for a champion in the base
- A champion can gold up to 6 items


# Champion Death
- When a champion dies they return to their base zone
- The champion remains dead for 1 turn
- At the start of their next turn the champion respawns and can make a movement


# Smite
- Any champion without a `Smite` stat is considered to have a skill of 1
- If a champion from both teams are in a zone with an Epic Monster
- On the final turn to kill an Epic Monster it will be smited
- Smites should be settled using a dice
- If both Smiters have the same Smite skill then they each have a 50/50 chance
```
Roll a dice
1,2,3 = Player 1 wins
4,5,6 = Player 2 wins
```
- If the Smite skills are different the dice rolls change
```
Player 1 has Smite skill 2 
Player 2 has Smite skill 3
Difference = 1
1,2 = Player 1 wins
3+ = Player 2 wins
```
- A Smiter always has at least 1 chance on a dice to get the Smite 
- The most extreme examples that can occur are:
```
1 = Player 1 wins
2+ = Player 2 wins 

and the reverse :

5 or below = Player 1 wins
6 = Player 2 wins
```

# Ending a game
- The game ends when one Nexus has been destroyed
- In order to hit a Nexus all the towers in at least one lane must be destroyed
- And both base towers must be destroyed

# Cards

### Focus
- Specify which enemy champion takes damage first

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

### Tower dive
- Enemy champion must be in the same tile
- Current tile must have an active tower

- Charge the enemy under their tower
- Roll a dice and follow the below table to determine the outcome
```
| Roll    | Damage dealt  | Damage taken  |
|---------|---------------|---------------|
|  1,2,3  |       0       |       2       |
|    4    |       2       |       2       |
|   5,6   |       2       |       0       |
```
- If a champion is Tower diving both enemy base towers roll a second dice
- A champion does not deal extra damage with the second roll
- The roll determines if the champions takes more damage
- If you deal damage to the base towers the attacking player can choose which tower takes the damage

### Counter-gank
- Usable during the opponent's movement phase
- If the opponent moves an additional champion into a lane or jungle zone
- Move one of your champions from an adjacent zone into the one being attacked

### Crit
- Deal +50% (rounded down) damage for this Attack phase
- Does not work on Ultimate abilities


# Champion stats

### Initiative
- Used at the start of the game to determine the turn order
- Total the initiative of all of your champions and compare this against your opponent's initiative value

### Health
- The total amount of health a champion can have
- Set health value to full at the start of the game and on any recalls or respawns

### Attack
- The base damage the champion deals during an `Attack` stage

### Defense
- The base reduction of damage taken

### Farming income
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

### Smite
- The champion's ability to secure large monster objectives
- If another champion is in the same zone, compare the two highest Smite values
- See [Smite](#smite) for more details


# Champion list

- Ornn
- Malphite
- Shen

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

