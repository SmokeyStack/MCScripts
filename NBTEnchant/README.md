# NBTEnchant
This script is used to generate `.mcstructure` files containing edited nbt data that is currently not possible to do ingame.

## Prerequisites
- [Python](https://www.python.org/downloads/) installed.

## Setup
- Download the two files.
- Run `pip install -r requirements.txt`.
- Run the script in a terminal.

## Arguments
- The `-i` or `--id` argument dictates the Enchantment ID. Default is 0. Enchantment ID can be found using the Minecraft Wiki or check the `vanilla_name` list for the corresponding name and index.
- The `-l` or `--level` argument dictates the Enchantment Level. Default is 1.
- The `-n` or `--name` argument dictates the item id. Default is `minecraft:enchanted_book`.
- Running this script with arguments will only result in one `.mcstructure` with the following arguments.

## Regolith
- For more information, click [here](https://bedrock-oss.github.io/regolith/docs/introduction) to see what Regolith is.
- Run `regolith install github.com/SmokeyStack/MCScripts/NBTEnchant` in the command line.
- Edit the `config.json` to get the item you desire.