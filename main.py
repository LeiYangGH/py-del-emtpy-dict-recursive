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


def visit_l(l):
    print('visit_l')
    deleted = 0
    for d in l:
        if DELETE in d:
            continue
        if 'item' in d:
            print(d['item'])
        sections = d['sections']
        if sections:

            if all(DELETE in se for se in sections):
                if not DELETE in d:
                    d[DELETE] = True
                    print('deleted')
                    deleted += 1
            for sec in sections:
                print(sec['item'])
                if DELETE in sec:
                    continue

                if not sec['sections'] and sec['value'] == 'None':
                    if not DELETE in sec:
                        sec[DELETE] = True
                        print('deleted')
                        deleted += 1
                deleted += visit_l(sec['sections'])
        elif d['value'] == 'None':
            if not DELETE in d:
                d[DELETE] = True
                # del l[index]
                print('deleted')
                deleted += 1
    return deleted


d = 1
while d > 0:
    print(d)
    d = visit_l(data)

pprint(data)
# pprint(json.dumps(data))
