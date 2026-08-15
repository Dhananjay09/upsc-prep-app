import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_reforms_1991 (Ramesh Singh Ch.6)
# IMF conditions for 1991 reforms, Macro Stabilisation vs Structural Reform measures,
# LPG framework interpretation (liberalisation=direction, privatisation=path,
# globalisation=goal)
# ==================================================================

upsc.append({"q":"Consider the following statements about the IMF's conditions attached to its 1991 assistance to India:\n1. The rupee was devalued by 22 per cent, implemented in two phases.\n2. The peak import tariff was to be drastically reduced from 130 per cent to 30 per cent.\n3. All government expenditure was to be increased by 10 per cent annually to boost demand.\nHow many of the statements given above are correct?","o":["Only two","All three","Only one","None"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 reverses the actual condition — government expenditure was to be CUT (not increased) by 10% annually, covering costs like interest payments, pensions, provident fund contributions and subsidies, to consolidate the fiscal deficit."})

upsc.append({"q":"Assertion (A): Excise duties (now CENVAT) were hiked by 20 per cent as part of the 1991 IMF-linked reform conditions.\nReason (R): This hike was meant to neutralise the revenue shortfall arising from the drastic cut in customs/import tariffs.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are true and R explains A — since cutting the peak import tariff from 130% to 30% would sharply reduce customs revenue, the government simultaneously raised excise duties by 20% to offset this shortfall, alongside launching a broader tax structure modernisation programme."})

upsc.append({"q":"Which one of the following correctly distinguishes 'Macroeconomic Stabilisation Measures' from 'Structural Reform Measures' in India's 1991 reform programme?","o":["Macroeconomic Stabilisation Measures aim to boost aggregate demand (domestic and external), while Structural Reform Measures aim to boost the aggregate supply of goods and services","Macroeconomic Stabilisation Measures aim to boost aggregate supply, while Structural Reform Measures aim to boost aggregate demand","Both categories exclusively target reducing government expenditure","Structural Reform Measures apply only to the external sector, while Macroeconomic Stabilisation applies only to the domestic sector"],"a":0,"e":"Macroeconomic Stabilisation Measures target boosting aggregate demand (via enhanced purchasing power and employment), while Structural Reform Measures target boosting aggregate supply (via unshackling the economy to realise its productivity potential) — these are the two broad categories comprising India's 1991 reform programme."})

upsc.append({"q":"Which one of the following statements correctly captures the argument in defence of Structural Reform Measures against the criticism that they are inherently 'anti-poor'?","o":["Since production is undertaken by capitalists/producers, structural reforms may appear 'pro-rich' at first glance, but higher growth and income generated is what eventually enables increased purchasing power for the masses, even though this distribution takes time","Structural reform measures were universally accepted as pro-poor with no criticism from any quarter","Structural reforms directly and instantly redistribute income to the poor without any time lag","Structural reforms have nothing to do with production or supply-side considerations"],"a":0,"e":"The text explicitly acknowledges that structural reforms look 'pro-rich'/'pro-capitalist' since production is carried out by capitalists, but argues this is not equivalent to 'anti-poor' — higher growth/income is a prerequisite for eventually raising mass purchasing power, though the distribution of this increased income takes time, especially amid political instability."})

upsc.append({"q":"With reference to the LPG (Liberalisation, Privatisation, Globalisation) framework describing India's economic reforms, which one of the following correctly matches each term to its described role?","o":["Liberalisation shows the direction of reform; Privatisation shows the path of reform; Globalisation shows the ultimate goal of reform","Liberalisation shows the ultimate goal; Privatisation shows the direction; Globalisation shows the path","Privatisation shows the direction; Globalisation shows the path; Liberalisation shows the ultimate goal","All three terms are synonymous and interchangeable in describing India's reform process"],"a":0,"e":"As per the book's framing, Liberalisation indicates the DIRECTION of reform (pro-market orientation), Privatisation indicates the PATH (reducing state ownership/role), and Globalisation indicates the ultimate GOAL (integration with the world economy) — three distinct but complementary facets of the same reform process."})

upsc.append({"q":"The economic ideology underlying 'liberalisation' traces its philosophical roots to which broader political ideology, which developed over the preceding three centuries and took recognisable form by the early nineteenth century?","o":["Liberalism","Socialism","Mercantilism","Fabianism"],"a":0,"e":"Liberalisation's economic meaning derives from the broader political ideology of 'liberalism', which emerged from the breakdown of feudalism and the growth of market/capitalist society, later given economic expression through Adam Smith's laissez-faire principle."})

upsc.append({"q":"Consider the following statements about the political and social context of India's 1991 economic reforms:\n1. Political parties in India have historically been divided on the issue of reforms.\n2. The reforms were criticised by some as being prescribed and dictated by the IMF.\n3. Emotional issues such as religion and caste have been noted as playing a role in complicating the political maturity required for sustained reform.\nWhich of the statements given above is/are correct?","o":["1, 2 and 3","1 and 2 only","2 and 3 only","1 only"],"a":0,"e":"All three statements are correct — the text explicitly notes India's political parties' divided stance on reforms, criticism of the reforms as IMF-dictated, and the complicating role of emotional/identity-based issues (religion, caste) in achieving the political maturity needed for successful, sustained reform."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_reforms_1991_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")
