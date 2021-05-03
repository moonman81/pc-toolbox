from pc_lib import pc_api, pc_utility

# --Configuration-- #

parser = pc_utility.get_arg_parser()
# INSERT ARGS HERE
args = parser.parse_args()

# --Initialize-- #

settings = pc_utility.get_settings(args)
pc_api.configure(settings)

# --Main-- #

# INSERT CODE HERE
result = pc_api.current_user()
print(result)