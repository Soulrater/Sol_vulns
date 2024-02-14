elem = ['heat', 'life', 'dust', 'rain', 'mud', 'pressure', 'energy', 'wind', 'lava', 'fog', 'steam', 'smoke', 'ocean', 'mountain', 'seed', 'time', 'sun', 'metal', 'cloud', 'oil', 'river', 'worm', 'wave', 'swamp', 'magnet', 'stone', 'clay', 'tornado', 'hot-springs', 'fossil', 'coral', 'plant', 'nail', 'plastic', 'alcohol', 'antenna', 'apple', 'art', 'ash', 'balloon', 'beach', 'blizzard', 'blueprint', 'bottle', 'cactus', 'cloth', 'coal', 'coffee', 'coin', 'dam', 'desert', 'dolphin', 'electricity', 'explosion', 'fire-extinguisher', 'firework', 'fish', 'frost', 'furnace', 'gas', 'gasoline', 'glass', 'hail', 'hammer', 'ice', 'ice-storm', 'ink', 'island', 'lightning', 'meteor', 'music', 'paint', 'paper', 'party', 'pond', 'rod', 'sand', 'sky', 'snow', 'solar-panel', 'sound', 'squid', 'storm', 'sugar', 't-shirt', 'telescope', 'tequila', 'tree', 'umbrella', 'volcano', 'whale', 'windmill', 'wire', 'wood', 'yacht', 'fire-extinguisher']
import requests
import json

errors = {}
tiers = {}

for i in elem:
  resp = requests.get(f"https://elementerra-mainnet.s3.us-east-1.amazonaws.com/{i}.json")
  if resp.status_code not in [200, 201]:
    print(resp.text)
    errors[i] = resp.text
    continue
  tier = resp.json()["attributes"][0]["value"]
  tiers[i] = tier
  print(f"{i} is tier {tier}")
