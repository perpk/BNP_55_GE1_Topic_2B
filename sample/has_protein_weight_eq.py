def has_protein_weight_eq(prot_dict, weight):
    return [float(w) == weight for w in [i for i in list(*prot_dict.values())]]
