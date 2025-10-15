# Cashgrab - A text-based crime simulator

## Welcome to **Cashgrab**, a text-based game where you rise through the underworld to build your criminal empire. Make money, run scams, gamble, and plan heists—everything it takes to become the ultimate crime boss.

# Text-Based Business/Crime Simulation Game

## Overview
This project is a text-based game simulating business and crime development. It incorporates:  
- A probability system influencing the outcome of actions  
- Saved player progression  
- Eventually competitive play against other users  

## Goals
- **Account Balance:** Players have an overall account balance affected by the outcomes of mini-games.  
- **World Interaction:** Users can interact with the game world through mini-games.  
- **Level Progression (Reputation):** Advancing in reputation unlocks access to further actions within the game world.  
- **Probability-Based Outcomes:** Success rates use probability functions; higher-risk actions offer higher rewards.  
- **Items & Upgrades:** Players can purchase items with in-game currency that affect reputation and success rates in mini-games or actions.  
- **Game Over Condition:** The game ends when a player’s overall balance reaches £0.

## Features
- **Strategic gameplay:** Manage money, resources, and risk  
- **Multiple criminal paths:** Gambling, scams, theft, and more  
- **Dynamic events:** Random encounters that can make or break your empire  
- **Text-based interface:** Fully playable in your terminal  
- **Replayable:** Different choices lead to unique outcomes

## Activities & Mini‑Games

The world is split into themed activity tracks. Each activity has a **reputation (Rep)** requirement to unlock — higher Rep unlocks higher‑risk, higher‑reward content.

### Casino Games
| Activity | Required Rep | Description |
|---|---:|---|
| Roulette | 0 | Classic wheel gambling — low barrier, variable payouts. |
| Blackjack | 1 | Card game with strategy — better rewards for skill. |
| Slots | 2 | High variance, chance-driven slot machines. |
| Grand Prize Wheel Spin | 3 | High-tier prize wheel with significant payouts and consequences. |

### Cybercrime
| Activity | Required Rep | Description |
|---|---:|---|
| Phishing Scams | 1 | Social-engineering puzzles that net cash/reputation if successful. |

### Robberies
| Activity | Required Rep | Description |
|---|---:|---|
| Petrol Stations | 1 | Quick, lower-risk robberies with modest payout. |
| Home Invasion | 2 | Riskier break-ins with higher reward and greater chance of consequences. |
| Cash Vans | 3 | Coordinated heist requiring planning and resources. |
| Credit Union | 4 | High-stakes robbery with large payoff and heavy fallout risk. |
| State Bank | 5 | Endgame-level robbery: massive reward, extreme risk and consequences. |

### Buying / Selling Illicit Goods
| Activity | Required Rep | Description |
|---|---:|---|
| Physical Blackmarket | 0 | Street dealers and local markets — entry-level trade. |
| Deep Web Markets | 1 | Higher-value illicit goods traded on hidden markets — more profit, more risk. |

> **Unlock rules:** Players gain Reputation (Rep) by completing activities, achieving objectives, and spending in‑game currency on reputation‑boosting items. When a player's Rep reaches the required threshold, the corresponding activities become available.



## Releases
The executable will be released when ready for testing.  

Otherwise, you can create your own executable using PyInstaller:  

```bash
pip install pyinstaller



