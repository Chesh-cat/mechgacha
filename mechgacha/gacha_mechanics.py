from dataclasses import dataclass
from enum import Enum

class TagType:
    arm = "arm"
    leg = "leg"
    power = "power"
    body = "body"
    cosmetic = "cosmetic"


@dataclass
class Mech:
    # a person with a loot table
    username:str = ""
    loot:set = ()

@dataclass
class Item:
    name: str
    description: str
    tags:tuple = () # "arm", "leg", etc
    stars:int = 1
    extradata = ()

    def __post_init__(self):
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])

                if field_type is tuple and current_type is list:
                    self.__dict__[name] = tuple(self.__dict__[name])
                else:
                    raise TypeError(f"The field `{name}` was assigned by `{current_type}` instead of `{field_type}`")

    def to_dict(self):
        # convert item into a dict, for saving in the DB
        return {"name": self.name, "description": self.description, "tags": self.tags, "stars": self.stars, "extradata": self.extradata}

# these are just helper functions
def itemHelperFunction(requiredTag):
    def makeItem(*args, **kwargs):
        item = Item(*args, **kwargs)
        item.tags = [requiredTag]
        return item
    return makeItem

PowerItem = itemHelperFunction("power")
WeaponItem = itemHelperFunction("weapon")
LegsItem = itemHelperFunction("legs")
ArmsItem = itemHelperFunction("arms")
BodyItem = itemHelperFunction("body")
CockpitItem = itemHelperFunction("cockpit")

def BodyPlanItem(name, description, bodyplan, stars=1):

    #body plan is a dict of {tagName: number}

    # todo: expand this out
    item = Item(name, description)
    item.bonusdata = bodyplan
    item.tags = ["bodyplan"]
    return item

    

class ItemInInventory:
    id: str
    item_data: Item
    original_owner: str
    
    

def check_gacha_table():
    for person in all_people:
        pass
        
