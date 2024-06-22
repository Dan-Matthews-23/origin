class TierInfo:
  def __init__(self, tier_one_name, tier_two_name, tier_three_name):
    self.tier_one_name = tier_one_name
    self.tier_two_name = tier_two_name
    self.tier_three_name = tier_three_name

class FactionData:
  def __init__(self, faction_name, tier_info):
    self.faction_name = faction_name
    self.tier_info = tier_info

# Creating data objects
spartan_tiers = TierInfo("Recruit", "Knight", "Elite")
spartan_data = FactionData("Spartan", spartan_tiers)

amazon_tiers = TierInfo("Training", "Scout", "Master")
amazon_data = FactionData("Amazon", amazon_tiers)

# Calling the data
faction_data = spartan_data  # or amazon_data
tier_two_name = faction_data.tier_info.tier_two_name  # access nested data

# All data can be stored in a list
all_factions = [spartan_data, amazon_data]
