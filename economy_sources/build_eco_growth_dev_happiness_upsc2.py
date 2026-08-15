import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_growth_dev_happiness (Ramesh Singh Ch.2)
# Growth vs development combinations, Gulf countries as first 'growth without
# development' case, Mahbub ul Haq, welfare economics origin
# ==================================================================

upsc.append({"q":"Which one of the following correctly lists the three theoretically possible combinations of growth and development discussed in development economics?","o":["Higher growth and higher development; Higher growth but lower development; Lower growth but higher development","Higher growth and higher development; Lower growth and lower development only","Only higher growth combinations are theoretically possible","Development is always directly proportional to growth with no exceptions"],"a":0,"e":"The three recognised combinations are: higher growth with higher development, higher growth with lower development, and lower growth with higher development — illustrating that growth (quantitative progress) and development (quantitative plus qualitative progress) do not automatically move together."})

upsc.append({"q":"Which group of economies is cited as the first instance economists identified of 'growth without development' — high income/growth levels without comparable development levels — giving rise to the branch of 'development economics'?","o":["The Gulf countries","The East Asian Tiger economies","The Latin American economies","The Scandinavian economies"],"a":0,"e":"The Gulf countries, despite achieving far higher income and growth levels through oil wealth, showed development levels not commensurate with their income — this mismatch is credited with catalysing the emergence of 'development economics' as a distinct field."})

upsc.append({"q":"Which economist is credited with articulating the conceptual distinction between economic growth and economic development by the early 1970s?","o":["Mahbub ul Haq","Amartya Sen","Simon Kuznets","Gunnar Myrdal"],"a":0,"e":"Mahbub ul Haq, a leading Pakistani economist, is credited with clearly articulating the growth-versus-development distinction by the early 1970s — he later also played a central role in creating the UNDP's Human Development Index in 1990."})

upsc.append({"q":"Assertion (A): 'Welfare economics' emerged as a distinct branch of economics following the Great Depression.\nReason (R): The Great Depression broke down the previously assumed automatic circular relationship between growth and development, prompting the establishment of the 'welfare state' concept and heightened policy concern for development.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are true and R explains A — the Great Depression's disruption of the assumed growth-development circularity, combined with the rise of welfare-state thinking, directly gave birth to welfare economics as governments and economists grappled with the immediacy of development concerns."})

upsc.append({"q":"Consider the following statements about the conceptual difference between 'growth' and 'development' in economics:\n1. Growth is generally understood as purely quantitative progress in an economy.\n2. Development is understood as both quantitative and qualitative progress.\n3. Two families with identical income levels will always show identical levels of development.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — the text explicitly illustrates that two families with the SAME income can show DIFFERENT development levels depending on how they allocate spending toward health, education, and savings versus other priorities."})

upsc.append({"q":"Which one of the following statements best describes the 'two kinds of difficulties' economists faced in developing a formula to measure development?","o":["Difficulty in defining what exactly constitutes development, and difficulty in identifying measurable determinants/traits reflecting it","Lack of any international interest from bodies like the UNO, IMF or World Bank in measuring development","Complete absence of any data on income levels across countries","Universal agreement on development's definition but disagreement only on statistical software"],"a":0,"e":"The core difficulties were conceptual (defining what constitutes 'development' given its many possible dimensions — income, healthcare, nutrition, literacy, safe drinking water, social security, etc.) and methodological (identifying appropriate measurable determinants) — not a lack of institutional interest, which was in fact strong from UNO/IMF/WB."})

upsc.append({"q":"Which one of the following correctly captures the argument for a 'circular relationship' between growth and development, as described in the text?","o":["Growth suitably channelled into development accelerates further growth, while poorly managed growth with neglected development eventually causes growth itself to decline","Growth and development are entirely independent phenomena with no causal connection in either direction","Development always causes growth to decline permanently once achieved","Growth automatically and unconditionally produces development in every case"],"a":0,"e":"The 'circular relationship' means growth, if properly channelled into development, feeds back to accelerate further growth and expand the population covered by development — but growth achieved with neglected/ill-cared development eventually undermines growth itself, showing the two are interdependent rather than independent or automatic."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_growth_dev_happiness_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")
