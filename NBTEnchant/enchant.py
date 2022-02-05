from pynbt import NBTFile, TAG_Byte, TAG_Compound,TAG_Float, TAG_Int, TAG_List, TAG_Long, TAG_Short, TAG_String
import argparse

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-i", "--id", help = "Enchantment ID", required = False, default = 0)
parser.add_argument("-l", "--level", help = "Enchantment Level", required = False, default = 1)

# Read arguments from command line
args = parser.parse_args()

enchant_id = int(args.id)
level_id = int(args.level)

# Each index corresponds to the max vanilla level
vanilla_enchants = [4,  4,  4,  4,  4,  3,  3,  3,  1,  5,  5,  5,  2,  2,  3,  5,  1,  3,  3,  5,  2,  1,  1,  3,  3,  2,  1,  1,  1,  5,  3,  3,  1,  1,  4,  3,  3]
vanilla_name = ['protection_',  'fire_protection_',  'feather_falling_',  'blast_protection_',  'projectile_protection_',  'thorns_',  'respiration_',  'depth_strider_',  'aqua_affinity_',  'sharpness_',  'smite_',  'bane_of_arthropods_',  'knockback_',  'fire_aspect_',  'looting_',  'efficiency_',  'silk_touch_',  'unbreaking_',  'fortune_',  'power_',  'punch_',  'flame_',  'infinity_',  'luck_of_the_sea_',  'lure_',  'frost_walker_',  'mending_',  'binding_',  'vanishing_',  'impaling_',  'riptide_',  'loyalty_',  'channeling_',  'multishot_',  'piercing_',  'quick_charge_',  'soul_speed_']

def setVal(id, level):
    value = {
        'format_version': TAG_Int(1),
        'size': TAG_List(TAG_Int, [1, 1, 1]),
        'structure': TAG_Compound({
            'block_indices': TAG_List(TAG_List, [
                TAG_List(TAG_Int, [0]),
                TAG_List(TAG_Int, [-1])
            ]),
            'entities': TAG_List(TAG_Compound, [{
                'Age': TAG_Short(0),
                'Health': TAG_Short(5),
                'Item': TAG_Compound({
                    'Count': TAG_Byte(1),
                    'Damage': TAG_Short(0),
                    'Name': TAG_String('minecraft:enchanted_book'),
                    'WasPickedUp': TAG_Byte(0),
                    'tag': TAG_Compound({
                        'ench': TAG_List(TAG_Compound, [{
                            'id': TAG_Short(id),
                            'lvl': TAG_Short(level)
                        }])
                    })
                }),
                'OwnerID': TAG_Long(-4294967295),
                'OwnerNew': TAG_Long(-4294967295),
                'Pos': TAG_List(TAG_Float, [0.0, 1.0, 0.0]),
                'Rotation': TAG_List(TAG_Float, [0.0, 0.0]),
                'UniqueID': TAG_Long(-12884901004),
                'identifier': TAG_String('minecraft:item')
            }]),
            'palette': TAG_Compound({
                'default': TAG_Compound({
                    'block_palette': TAG_List(TAG_Byte, []),
                    'block_position_data': TAG_Compound({})
                })
            })
        }),
        'structure_world_origin': TAG_List(TAG_Int, [
            0,
            1,
            0
        ])
    }
    nbt = NBTFile(value=value)
    with open(f'{vanilla_name[id]}{level}.mcstructure', 'wb') as io:
        nbt.save(io, True)

    with open(f'{vanilla_name[id]}{level}.mcstructure', 'rb') as io:
        nbt = NBTFile(io, '', '{}', True)
        print(nbt.pretty())

count=1

if(enchant_id != 0 or level_id != 1):
    setVal(enchant_id, level_id)
# Script to iterate each enchant 5 times
else:
    for x in vanilla_enchants:
        for a in range (5):
            setVal(enchant_id, x+count)
            count+=1
        count=1
        enchant_id+=1
