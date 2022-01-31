# NBTEnchant
This script is used to generate `.mcstructure` files containing edited nbt data that is currently not possible to do ingame. For my needs, it generates each enchantments 5 times with 5 levels higher than the vanilla limit. Ex: It will generate 5 `.mcstructure` with the Fortune enchantment, however, the first one will be Fortune 4, then Fortune 5, and so on until Fortune 8, which is 5 higher than the vanilla limit.

## Prerequisites
- [Python](https://www.python.org/downloads/) installed.

## Setup
- Download the two files.
- Run `pip install -r requirements.txt`.
- Run the script in a terminal.

## Arguments
- The `-i` or `--id` argument dictates the Enchantment ID. Default is 0. Enchantment ID can be found using the Minecraft Wiki or check the `vanilla_name` list for the corresponding name and index.
- The `-l` or `--level` argument dictates the Enchantment Level. Default is 1.
- Running this script with arguments will only result in one `.mcstructure` with the following arguments.