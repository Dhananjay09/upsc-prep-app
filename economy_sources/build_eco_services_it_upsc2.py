import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_services_it (Ramesh Singh Ch.10, intro/global data)
# India's global services ranking, GVA/employment comparisons, state-wise services GSVA,
# FDI in services classification and share
# ==================================================================

upsc.append({"q":"Consider the following statements about India's global services sector standing (2006-2016):\n1. India's ranking among the world's 15 largest economies (by overall GDP) in services improved from 14th position in 2006 to 7th position in 2016.\n2. Among these top 15 economies, China recorded the highest increase in services' share of Gross Value Added during 2006-16, followed by India and Spain.\n3. In 2016, India recorded the highest services GVA growth rate among these economies, ahead of China.\nHow many of the statements given above are correct?","o":["All three","Only two","Only one","None"],"a":0,"e":"All three statements are correct: India's rank rose from 14th (2006) to 7th (2016); China led in services-GVA-share increase (9.8pp) followed by India (7.1pp) and Spain (7.0pp); and in 2016 India's services GVA growth (7.8%) topped even China's (7.4%) among these economies."})

upsc.append({"q":"Assertion (A): India's share of services employment is relatively low despite its high services GVA growth.\nReason (R): Among the world's 15 largest economies, India (along with China) was an exception where services accounted for less than two-thirds of total employment in 2016, with India's share at just 30.6 per cent — the lowest among these economies.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both are true and R explains A: despite strong GVA growth, services accounted for only 30.6% of India's employment in 2016 (the lowest share among the top-15 economies, alongside China as the only other sub-two-thirds economy) — illustrating that value-added growth in services has not been matched by proportionate employment generation."})

upsc.append({"q":"With reference to services export growth trends, consider the following statements:\n1. World services export growth dipped into negative territory in 2015, ending a positive run that had lasted six years since 2009.\n2. As per WTO data for the first half of 2017, India's services export growth (9.9%) exceeded the world average (4.3%), China's, and Russia's.\n3. Both world and India's services exports returned to positive territory in 2016 after the 2015 dip.\nWhich of the statements given above is/are correct?","o":["1 and 3 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 3 are correct. Statement 2 is false — while India's 9.9% growth exceeded the world average (4.3%) and China's (0.2%), it was actually LOWER than Russia's, which recorded the highest growth at 18.4% in H1 2017."})

upsc.append({"q":"Consider the following statements about the state-wise distribution of India's services sector, per Economic Survey 2017-18 data:\n1. Services contributed over 50 per cent of Gross State Value Added (GSVA) in 15 out of 32 states/UTs.\n2. Delhi and Chandigarh recorded the highest services share of GSVA, exceeding 80 per cent, while Sikkim recorded the lowest at 31.7 per cent.\n3. In terms of services GSVA growth for 2016-17, Uttar Pradesh recorded the highest growth and Bihar the lowest.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 reverses the actual ranking — Bihar topped services GSVA growth at 14.5% in 2016-17, while Uttar Pradesh was at the bottom with just 7.0% growth, not the other way round."})

upsc.append({"q":"Which one of the following statements about FDI in India's services sector is correct?","o":["The combined FDI share of the top 10 service sectors (as per DIPP's classification) accounted for 56.6 per cent of cumulative FDI inflows during April 2000-October 2017, rising to 65.8 per cent of FDI equity inflows during 2017-18 (up to October)","FDI in services sector has a precisely and universally agreed classification with no ambiguity","The services sector's share of FDI inflows declined during 2017-18 compared to the cumulative 2000-2017 average","Retail trading, agriculture services and education are officially part of DIPP's core services sector definition without needing separate addition"],"a":0,"e":"The correct figures are 56.6% (cumulative, April 2000-October 2017) rising to 65.8% (2017-18 up to October) — the text explicitly notes classification ambiguity in FDI-services data, and that retail trading, agriculture services, education, book printing and air transport are ADDITIONAL sectors beyond the core 10-sector DIPP definition, whose inclusion raises the overall share further (to 58.5% and 69.6% respectively)."})

upsc.append({"q":"Which one of the following best describes the debate over 'services-led growth' versus 'manufacturing-led growth' as resolved in Economic Survey 2014-15?","o":["The Survey favoured manufacturing, citing empirical studies on employment potential, labour force needs, and formality/informality issues, alongside championing 'Make in India' and enhanced railway investment","The Survey conclusively favoured continued exclusive reliance on services-led growth","The Survey recommended abandoning the manufacturing sector entirely in favour of agriculture","The debate remains entirely unresolved with no official government position taken"],"a":0,"e":"Despite services contributing over 62% of GDP during 2001-12, the Economic Survey 2014-15 tilted the debate towards manufacturing, citing its employment-generation potential and labour-force considerations, aligning with the 'Make in India' initiative and calls for greater railway investment."})

upsc.append({"q":"Consider the following statements about the sustainability of India's services-led growth model, as discussed in the concern raised by Rupa Chanda:\n1. Growth driven predominantly by exports of skill-based services is considered less sustainable unless matched by internal demand.\n2. Broad-based growth within services, with backward and forward linkages to the rest of the economy, is considered necessary for balanced and employment-oriented growth.\n3. Further FDI liberalisation and infrastructural/regulatory reforms are seen as unhelpful in diversifying the sources of services-sector growth.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — the text explicitly states that further infrastructural/regulatory reforms and FDI liberalisation in services CAN HELP diversify growth sources and provide momentum, not that they are unhelpful."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_services_it_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")
