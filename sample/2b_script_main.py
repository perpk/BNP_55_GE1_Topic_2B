from has_protein_weight_eq import has_protein_weight_eq

# B.
## i.
prot_1st_name = input("Please enter the name of a protein...")
weight_prot_1_1st_measure = input(f"Please enter the weight in g for the first measurement of {prot_1st_name}...")
weight_prot_1_2nd_measure = input(f"Please enter the weight in g for the second measurement of {prot_1st_name}...")

prot_1 = {prot_1st_name: [weight_prot_1_1st_measure, weight_prot_1_2nd_measure]}

## ii.
prot_2nd_name = input("Please enter the name of another protein...")
weight_prot_2_1st_measure = input(f"Please enter the weight in g for the first measurement of {prot_2nd_name}...")
weight_prot_2_2nd_measure = input(f"Please enter the weight in g for the second measurement of {prot_2nd_name}...")

prot_2 = {prot_2nd_name: [weight_prot_2_1st_measure, weight_prot_2_2nd_measure]}

## iii.
prot_l3 = [prot_1, prot_2]

### iv.
has_prot_1_weight_gt_10 = has_protein_weight_eq(prot_1, 10)
has_prot_2_weight_gt_10 = has_protein_weight_eq(prot_2, 10)

if any(has_prot_1_weight_gt_10):
    print(f"Protein {prot_1st_name} showed weight with value eq. to 10")

if any(has_prot_2_weight_gt_10):
    print(f"Protein {prot_2nd_name} showed weight with value eq. to 10")

# v.
prot_3rd_name = input("Now, please enter the name of a 3rd protein...")
weight_prot_3_1st_measure = input(f"Please enter the weight in g for the 1st measurement of {prot_3rd_name}...")
weight_prot_3_2nd_measure = input(f"Please enter the weight in g for the 2nd measurement of {prot_3rd_name}...")

prot_3 = {prot_3rd_name: [weight_prot_3_1st_measure, weight_prot_3_2nd_measure]}

has_prot_3_weight_gt_10 = has_protein_weight_eq(prot_3, 10)

if any(has_prot_3_weight_gt_10):
    print(f"Protein {prot_3rd_name} showed weight with value eq. to 10")

prot_l3.append(prot_3)

# vi.
prot_l3.remove(prot_1)

# vii.
prot_l3.reverse()
print(prot_l3)


