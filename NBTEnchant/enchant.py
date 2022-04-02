from pynbt import NBTFile, TAG_Byte, TAG_Compound,TAG_Float, TAG_Int, TAG_List, TAG_Long, TAG_Short, TAG_String
import argparse, json, random, os

vanilla_name = ['protection',  'fire_protection',  'feather_falling',  'blast_protection',  'projectile_protection',  'thorns',  'respiration',  'depth_strider',  'aqua_affinity',  'sharpness',  'smite',  'bane_of_arthropods',  'knockback',  'fire_aspect',  'looting',  'efficiency',  'silk_touch',  'unbreaking',  'fortune',  'power',  'punch',  'flame',  'infinity',  'luck_of_the_sea',  'lure',  'frost_walker',  'mending',  'binding',  'vanishing',  'impaling',  'riptide',  'loyalty',  'channeling',  'multishot',  'piercing',  'quick_charge',  'soul_speed']

# Define the structure
def setVal(name, item_list):
    value = {
	    'format_version': TAG_Int(1),
	    'size': TAG_List(TAG_Int, [1, 1, 1]),
	    'structure': TAG_Compound({
		    'block_indices': TAG_List(TAG_List, [
			    TAG_List(TAG_Int, [0]),
			    TAG_List(TAG_Int, [-1])
		    ]),
            'entities': TAG_List(TAG_Compound, item_list),
		    'palette': TAG_Compound({
			    'default': TAG_Compound({
				    'block_palette': TAG_List(TAG_Byte, []),
				    'block_position_data': TAG_Compound({})
			    })
		    })
	    }),
	    'structure_world_origin': TAG_List(TAG_Int, [0, 1, 0])
    }

    nbt = NBTFile(value=value)

    # Writes the structure
    os.makedirs('BP/structures', exist_ok = True)
    with open(f'BP/structures/{name}.mcstructure', 'wb') as io:
        nbt.save(io, True)


def checkEnch(name):
    for a in range(len(vanilla_name)):
        if(vanilla_name[a]==name):
            return a

def main():
    id_list = []
    ench_list = []
    item_list = []
    
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-i", "--id", help = "Enchantment ID", required = False, default = 0)
    parser.add_argument("-l", "--level", help = "Enchantment Level", required = False, default = 1)
    parser.add_argument("-n", "--name", help = "Item Identifier", required = False, default = "minecraft:enchanted_book")
    parser.add_argument('--regolith', action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    #Checks if it is Regolith or CLI
    if(args.regolith):
        # Read arguments from config file
        f = open('data/NBTEnchant/config.json')
        config = json.load(f)

        name = config['structures'][0]['name']
        for a in config['structures'][0]['items']:
            id_list.append(a)

        for a in config['structures'][0]['enchantments']:
            if(len(a)==1):
                ench_list.append({'id': TAG_Short(checkEnch(a['enchantment'])), 'lvl': TAG_Short(1)})
            else:
                ench_list.append({'id': TAG_Short(checkEnch(a['enchantment'])), 'lvl': TAG_Short(a['level'])})
        
        for a in range(len(id_list)):
            item_list.append({
                    'Age': TAG_Short(0),
                    'Health': TAG_Short(5),
                    'Item': TAG_Compound({
                        'Count': TAG_Byte(1),
                        'Damage': TAG_Short(0),
                        'Name': TAG_String(id_list[a]),
                        'WasPickedUp': TAG_Byte(0),
                        'tag': TAG_Compound({
                            'ench': TAG_List(TAG_Compound, ench_list)
                        })
                    }),
                    'OwnerID': TAG_Long(-4294967295),
                    'OwnerNew': TAG_Long(-4294967295),
                    'Pos': TAG_List(TAG_Float, [0.0, 1.0, 0.0]),
                    'Rotation': TAG_List(TAG_Float, [0.0, 0.0]),
                    'UniqueID': TAG_Long(random.randint(-10000000,10000000)),
                    'identifier': TAG_String('minecraft:item')
            })
    else:
        name = str(vanilla_name[int(args.id)]) + '_' + str(int(args.level))
        item_list.append({
            'Age': TAG_Short(0),
            'Health': TAG_Short(5),
            'Item': TAG_Compound({
                'Count': TAG_Byte(1),
                'Damage': TAG_Short(0),
                'Name': TAG_String(args.name),
                'WasPickedUp': TAG_Byte(0),
                'tag': TAG_Compound({
                    'ench': TAG_List(TAG_Compound, [{
                        'id': TAG_Short(int(args.id)),
                        'lvl': TAG_Short(int(args.level))
                    }])
                })
            }),
            'OwnerID': TAG_Long(-4294967295),
            'OwnerNew': TAG_Long(-4294967295),
            'Pos': TAG_List(TAG_Float, [0.0, 1.0, 0.0]),
            'Rotation': TAG_List(TAG_Float, [0.0, 0.0]),
            'UniqueID': TAG_Long(random.randint(-10000000,10000000)),
            'identifier': TAG_String('minecraft:item')
        })
    setVal(name, item_list)

if __name__ == '__main__':
    main()