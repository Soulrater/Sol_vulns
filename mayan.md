## Source
Mayan finance is a cross-chain swap auction protocol on Solana built on wormhole. The easy to use dapp allows users to carry out cross-chain one-click token swaps. \
\
![image](https://github.com/Soulrater/Sol_vulns/assets/159967673/6dfa9f6e-11e2-41f6-ad5e-c9455ffb38ba)

This functionality can also be imported into other dapps via the mayan swap widget which is imported into the page using a javascript block https://docs.mayan.finance/integration/swap-widget which as you might notice includes rpc urls\
\
![image](https://github.com/Soulrater/Sol_vulns/assets/159967673/93edee35-bc5f-4b23-acd2-1f906e41355a)

The javascript block however is visible to any user brave enough to search through the devtools of their browser.

By finding the exposed block, a user could view the list of exposed rpc keys. 

I easily found websites using Mayan's widget using Google-fu. 

## Targets
### Buybonk.com
Exposed hellomoon rpc key
### Myrothedog
Exposed quicknode rpc keys

## Impact
The exposed rpc keys are paid services that have a usage cap (after which a flat cost is charged) AND a ratelimit 

This seems like an easy way to rack up debt for the teams as well as DoS the service by maxing out the ratelimit.

![image](https://github.com/Soulrater/Sol_vulns/assets/159967673/4b87f838-2a7c-4ede-9af6-52ae93b588a0)
![image](https://github.com/Soulrater/Sol_vulns/assets/159967673/4efa1a8d-7c2d-42a0-b386-295609ffdefb)

## Remediation
I contacted the Mayan team first and got a surpising answer
![image](https://github.com/Soulrater/Sol_vulns/assets/159967673/2ec9d23c-e559-4977-921b-6ad8037fbb1b)

So I decided to contact the teams instead. 

Turns out buybonk was managed by the Mayan team which made them responsible for the issue (as mentioned)

I pointed this out to Mayan but my ticket never got a reply and was closed afterwards. 

## Conclusion
It seems web3 devs aren't bothered about exposing rpc keys despite the potential dangers that can be caused. 

I also learnt that security isn't paid much attention unless it directly affects user funds 

Which explained why there does not seem to be a lot of white hats on chain 

Oh well. 
