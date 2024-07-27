from nsdata import get_data as gd
from impacts import bolus_carb as bc

gd.get_data(option="recent_10")

impact = bc.impact_of_bolus_carb(bolus=0, carb=0, iob=0, cob=0, carb_ratio=0,bolus_ratio=0)
print(impact)
