import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_evolution_indian_economy (Ramesh Singh Ch.3)
# Colonial economic legacy data: literacy/life expectancy at Independence,
# Angus Maddison's per capita growth estimates, British-dominated industry sectors
# ==================================================================

upsc.append({"q":"Consider the following statements about India's socio-economic condition at the time of Independence:\n1. India's literacy rate stood at only around 17 per cent.\n2. Life expectancy at birth was around 32.5 years.\n3. Aggregate real output growth during the first half of the 20th century was estimated at less than 2 per cent per year.\nWhich of the statements given above is/are correct?","o":["All three","Only two","Only one","None"],"a":0,"e":"All three statements are correct, reflecting the abject state of India's economy and social sector at Independence: ~17% literacy, ~32.5 years life expectancy at birth (B.R. Tomlinson), and near-stagnant aggregate real output growth (A. Vaidyanathan)."})

upsc.append({"q":"According to economic statistician Angus Maddison's estimates cited in the discussion of colonial India's economic performance, which one of the following is correct?","o":["India's per capita growth was a meagre 0.2 per cent between 1870 and 1947, compared with about 1 per cent in the UK during the same period","India's per capita growth exceeded the UK's during the colonial period 1870-1947","India had zero per capita growth from 1600 all the way through 1947 with no distinction between sub-periods","Maddison's data shows India's per capita income was higher than the UK's throughout the colonial period"],"a":0,"e":"Maddison's estimates show India recorded no per capita growth from 1600-1870, and only a meagre 0.2% per capita growth rate from 1870-1947 — far below the UK's roughly 1% during the same 1870-1947 period, quantifying the growth gap under colonial rule."})

upsc.append({"q":"Which one of the following sets of industries is correctly identified as having been dominated by British firms during the colonial period in India?","o":["Shipping, banking, insurance, coal, plantation crops and jute","Textiles, steel, cement and automobiles","Information technology, pharmaceuticals and telecommunications","Agriculture, handicrafts and cottage industries exclusively"],"a":0,"e":"British firms dominated shipping, banking, insurance, coal, plantation crops (like tea) and jute during the colonial era, while indigenous Indian capitalists who did emerge remained heavily dependent on British commercial capital — a structural distortion of colonial industrialisation."})

upsc.append({"q":"The term 'drain of wealth', used to describe a defining feature of India's colonial economic experience, refers to which one of the following?","o":["The unilateral transfer of investible capital from India to Britain by the colonial state","A natural resource depletion phenomenon unrelated to colonial policy","The outflow of gold reserves from British banks to Indian banks","A term describing post-Independence capital flight after 1947"],"a":0,"e":"The 'drain of wealth' specifically denotes the one-way, unilateral transfer of India's investible capital to Britain under colonial rule, compounding the broader 'unequal exchange' that crippled India's indigenous commerce, trade, and handloom industry."})

upsc.append({"q":"Assertion (A): The colonial state's economic vision for India centred on increasing India's capacity to export primary products.\nReason (R): This export orientation was designed to fund the purchase/import of British manufactured goods, meet the drain of capital, and cover the revenue requirements of imperial defence.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are true and R correctly explains A — the colonial economic strategy of promoting Indian primary-product exports served the specific downstream purposes of financing British manufactured-goods imports, offsetting the capital drain, and meeting imperial defence revenue needs."})

upsc.append({"q":"Which one of the following statements correctly characterises the pre-Independence period's economic performance as described in the text?","o":["It was a period of near stagnation, showing almost no meaningful change in the structure of production or levels of productivity","It was a period of rapid industrial diversification comparable to contemporaneous Western Europe","It saw India's agriculture sector consistently outpacing world agricultural growth rates","It was marked by sustained per capita income growth exceeding 2 per cent annually"],"a":0,"e":"The pre-Independence period is explicitly characterised as one of 'near stagnation' with almost no structural change in production or productivity levels — the opposite of rapid industrial diversification or sustained per capita growth."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_evolution_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")
