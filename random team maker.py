import random
 
participants = ["Hari","Aryan","Surya","Goutam","M.G","Aadhi","Midhun","Lakshmi","Meenakshi","Anshika","Isha"]
num_groups = 5
 
def assign_to_groups(participants, num_groups, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
 
    random.shuffle(participants)
 
    groups = {}
    for i in range(num_groups):
        groups[i] = []
 
    for index, participant in enumerate(participants):
        group_num = index % num_groups
        groups[group_num].append(participant)
 
    return groups
 
groups = assign_to_groups(participants, num_groups, random_seed=12098401298472)
 
for group_num, group in groups.items():
    print(f"Group {group_num + 1}: {', '.join(group)}")
