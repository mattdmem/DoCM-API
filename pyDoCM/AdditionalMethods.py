from DoCMWS import Variants

class VariantMethods:
    def __init__(self):
        pass

    @staticmethod
    def get_diseases(hgvs):
        v = Variants()
        result = v.variant_detail(hgvs)
        if result:
            diseases={}
            for d in result["diseases"]:
                if d["disease"] not in diseases:
                    disease = d["disease"]
                    diseases[disease]={}
                    diseases[disease]["source_pubmed_id"]=[]
                    diseases[disease]["source_pubmed_id"].append(d["source_pubmed_id"])
                else:
                    diseases[disease]["source_pubmed_id"].append(d["source_pubmed_id"])
            return diseases
        else:
            return None

    @staticmethod
    def get_drugs(hgvs):
        v = Variants()
        result = v.variant_detail(hgvs)
        if result:
            drugs={}
            for d in result["drug_interactions"]:
                if d["drug"] not in drugs:
                    drug = d["drug"]
                    drugs[drug]=[]
                    drugs[drug].append(d)
                else:
                    drugs[drug].append(d)
            return drugs
        else:
            return None

