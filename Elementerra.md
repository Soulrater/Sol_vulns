## Source
Elementerra is an on-chain alchemy Solana game where players win prizes by crafting and inventing new elements using existing discovered ones. https://www.elementerra.io/ https://elementerra.gitbook.io/elementerra/

The elements (NFTs) are split into different tiers with each tier requiring 4 elements of lesser tier to craft/invent  (4 tier-0 NFTs can be burnt to create a tier-1 NFT)

Clicking on an already discovered element reveals its tier and its recipe.
![image](https://github.com/Soulrater/Sol_vulns/assets/159967673/ba2abf97-3edb-424f-ad5b-5ec29dbfbb53)

Elements that have not been crafted are blacked out and can't be interacted with.
![image](https://github.com/Soulrater/Sol_vulns/assets/159967673/76b4751d-abf9-43b7-9136-bc4f286a5367)

However, checking any of the other unlocked element NFTs reveals a structure to the links of the metadata files.
![image](https://github.com/Soulrater/Sol_vulns/assets/159967673/23e36f1f-6e68-4a32-9609-8dbc3a35f179)

The metadata file also revealed the tier of the element
![Screenshot from 2024-02-14 03-03-16](https://github.com/Soulrater/Sol_vulns/assets/159967673/1586c827-fb1c-4577-b19e-b1d0c296fbe1)

By scanning the json files of the locked elements, I got their tiers 

PoC script: https://github.com/Soulrater/Sol_vulns/tree/main

## Impact
Discovering the tiers of unlocked elements allows a player to get an unfair edge over other players

## Remediation
I messaged Luffy on the elementerra team who was pleasant to talk to. 

I learnt that someone else had found the bug (or something similar) and made a website that included a list of tiers of all elements. 

He mentioned a priority for vulnerabilities that might expose the recipe of locked elements 

## Conclusion
Time to learn more about Solana accounts
