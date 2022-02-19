from pynbt import NBTFile, TAG_Byte, TAG_Compound,TAG_Float, TAG_Int, TAG_List, TAG_Long, TAG_Short, TAG_String
import argparse, os, shutil, json

vanilla_name = ['protection_',  'fire_protection_',  'feather_falling_',  'blast_protection_',  'projectile_protection_',  'thorns_',  'respiration_',  'depth_strider_',  'aqua_affinity_',  'sharpness_',  'smite_',  'bane_of_arthropods_',  'knockback_',  'fire_aspect_',  'looting_',  'efficiency_',  'silk_touch_',  'unbreaking_',  'fortune_',  'power_',  'punch_',  'flame_',  'infinity_',  'luck_of_the_sea_',  'lure_',  'frost_walker_',  'mending_',  'binding_',  'vanishing_',  'impaling_',  'riptide_',  'loyalty_',  'channeling_',  'multishot_',  'piercing_',  'quick_charge_',  'soul_speed_']

# Define the structure
def setVal(id, level, name):
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
                    'Name': TAG_String(name),
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

    # Writes the structure
    with open(f'{vanilla_name[id]}{level}.mcstructure', 'wb') as io:
        nbt.save(io, True)

    os.mkdir("BP/structures")
    dest = "BP/structures"
    src = f'{vanilla_name[id]}{level}.mcstructure'
    shutil.move(src, dest, copy_function=shutil.copytree)

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    f = open('../cache/filters/github.com/SmokeyStack/MCScripts/NBTEnchant/data/config.json')
    config = json.load(f)

    # Adding optional argument
    parser.add_argument("-i", "--id", help = "Enchantment ID", required = False, default = 0)
    parser.add_argument("-l", "--level", help = "Enchantment Level", required = False, default = 1)
    parser.add_argument("-n", "--name", help = "Item Identifier", required = False, default = "minecraft:enchanted_book")

    # Read arguments from command line
    args = parser.parse_args()

    enchant_id = config['enchantments'][0]['enchantment']
    level_id = config['enchantments'][0]['level']
    name_id = config['name']
    setVal(enchant_id, level_id, name_id)

if __name__ == '__main__':
    main()