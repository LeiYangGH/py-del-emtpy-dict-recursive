import json
from pprint import pprint

data = [
    {
        "date": "2017-05-31",
        "sections": [
            {
                "item": "BalanceSheetFormat2Heading",
                "value": "None",
                "sections": [
                    {
                        "item": "TotalAssets",
                        "value": "None",
                        "sections": [
                            {
                                "item": "FixedAssets",
                                "value": "None",
                                "sections": [
                                    {
                                        "item": "IntangibleAssets",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    },
                                    {
                                        "item": "PropertyPlantEquipment",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    },
                                    {
                                        "item": "InvestmentsFixedAssets",
                                        "value": "None",
                                        "sections": [
                                            {
                                                "item": "LoansToGroupUndertakings",
                                                "value": "None",
                                                "sections": [

                                                ]
                                            },
                                            {
                                                "item": "OwnShares",
                                                "value": "None",
                                                "sections": [

                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "item": "InvestmentProperty",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    },
                                    {
                                        "item": "BiologicalAssetsNon-current",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    }
                                ]
                            },
                            {
                                "item": "CurrentAssets",
                                "value": "None",
                                "sections": [
                                    {
                                        "item": "TotalInventories",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    },
                                    {
                                        "item": "BiologicalAssetsCurrent",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    },
                                    {
                                        "item": "Debtors",
                                        "value": "None",
                                        "sections": [
                                            {
                                                "item": "PrepaymentsAccruedIncome",
                                                "value": "None",
                                                "sections": [

                                                ]
                                            },
                                            {
                                                "item": "DeferredTaxAssetDebtors",
                                                "value": "None",
                                                "sections": [

                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "item": "CurrentAssetInvestments",
                                        "value": "None",
                                        "sections": [
                                            {
                                                "item": "InvestmentsInGroupUndertakings",
                                                "value": "None",
                                                "sections": [

                                                ]
                                            },
                                            {
                                                "item": "OwnShares",
                                                "value": "None",
                                                "sections": [

                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "item": "CashBankOnHand",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    }
                                ]
                            },
                            {
                                "item": "PrepaymentsAccruedIncome",
                                "value": "None",
                                "sections": [

                                ]
                            }
                        ]
                    },
                    {
                        "item": "TotalLiabilities",
                        "value": "None",
                        "sections": [
                            {
                                "item": "Equity",
                                "value": 9014904.0,
                                "sections": [

                                ]
                            },
                            {
                                "item": "ProvisionsFor",
                                "value": "None",
                                "sections": [
                                    {
                                        "item": "RetirementBenefitObligationsSurplus",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    }
                                ]
                            },
                            {
                                "item": "Creditors",
                                "value": "None",
                                "sections": [
                                    {
                                        "item": "UseCurrentNon",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    },
                                    {
                                        "item": "TradeCreditorsTradePayables",
                                        "value": "None",
                                        "sections": [

                                        ]
                                    }
                                ]
                            },
                            {
                                "item": "AccruedLiabilitiesNot",
                                "value": "None",
                                "sections": [

                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

DELETE = 'D'


def mark_d_delete(d):
    if 'item' in d and d['item'] == 'Equity':
        print('*' * 70)
    if DELETE in d:
        return 0
    else:
        d[DELETE] = True
        print('deleted')
        return 1


def visit_l(parent_d, l):
    print('visit_l')
    deleted = 0
    if parent_d and l and all(DELETE in x for x in l):
        deleted += mark_d_delete(parent_d)
    for d in l:
        if DELETE in d:
            continue
        if 'item' in d:
            print(d['item'])
        sections = d['sections']
        if sections:
            if all(DELETE in se for se in sections):
                deleted += mark_d_delete(d)
            for sec in sections:
                print(sec['item'])
                if DELETE in sec:
                    continue
                if (not sec['sections']) and sec['value'] == 'None':
                    deleted += mark_d_delete(sec)
                deleted += visit_l(sec, sec['sections'])
        elif d['value'] == 'None':
            deleted += mark_d_delete(d)
    return deleted


d = 1
while d > 0:
    print(d)
    d = visit_l(None, data)

pprint(data)

# print(json.dumps(data))
