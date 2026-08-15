import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_inflation (Ramesh Singh Ch.7)
# Phillips Curve, Friedman/Phelps critique & NAIRU, Reflation, Stagflation,
# Inflation Targeting framework (Feb 2015 Agreement)
# ==================================================================

upsc.append({"q":"The Phillips Curve, which posits a trade-off between inflation and unemployment, is named after which economist and based on which seminal study?","o":["A.W.H. Phillips, based on his 1958 study of unemployment and wage-rate changes in the United Kingdom (1861-1957)","Milton Friedman, based on his 1968 study of the natural rate of unemployment","Edmund Phelps, based on his 1967 paper on expectations-augmented inflation","John Maynard Keynes, based on his 1936 General Theory"],"a":0,"e":"The Phillips Curve is named after A.W.H. (Bill) Phillips, a New Zealand-born electrical engineer turned LSE economist, based on his 1958 paper 'The Relation between Unemployment and the Rate of Change of Money Wage Rates in the United Kingdom, 1861-1957', published in Economica."})

upsc.append({"q":"Consider the following statements about the Phillips Curve and the economic policy wisdom it inspired during the 1960s:\n1. It suggested an inverse relationship between inflation and unemployment — lower inflation associated with higher unemployment, and vice versa.\n2. Central banks in developed economies began framing monetary policies exploiting this trade-off, believing unemployment could be permanently reduced at the cost of slightly higher inflation.\n3. Developing economies uniformly found the framework straightforward to apply, since they typically faced low inflation alongside high unemployment.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — developing economies found the framework confusing to apply because many were simultaneously battling HIGH (often double-digit) inflation alongside high unemployment, not the low-inflation/high-unemployment combination the theory anticipated."})

upsc.append({"q":"Which two economists are credited with challenging the Phillips Curve in the early 1970s, arguing that the inflation-unemployment trade-off was only short-term and that there existed a 'natural rate of unemployment' unaffected by monetary policy in the long run?","o":["Milton Friedman and Edmund Phelps","John Maynard Keynes and Alfred Marshall","Paul Samuelson and William Nordhaus","Joseph Stiglitz and Carl Walsh"],"a":0,"e":"Milton Friedman (1976 Nobel Laureate) and Edmund Phelps challenged the Phillips Curve, arguing the trade-off vanished once people adjusted their inflation expectations and demanded higher wages, pushing unemployment back to its 'natural rate' regardless of monetary policy in the long run."})

upsc.append({"q":"The Non-Accelerating Inflation Rate of Unemployment (NAIRU), a concept arising from the Friedman-Phelps critique of the Phillips Curve, refers to:","o":["The unemployment rate at which upward and downward pressures on inflation and wages neutralise each other, leaving inflation stable with no tendency to change","The highest possible unemployment rate an economy can sustain during a recession","The unemployment rate that automatically eliminates inflation entirely to zero per cent","A fixed unemployment target set annually by the RBI's Monetary Policy Committee"],"a":0,"e":"NAIRU is the unemployment rate at which inflationary/wage pressures balance out, keeping inflation constant — it represents the lowest sustainable unemployment level without triggering rising inflation, not a zero-inflation guarantee or an RBI-set annual target."})

upsc.append({"q":"Consider the following statements about 'Reflation' as an economic phenomenon:\n1. It can refer to a deliberate government strategy of raising public expenditure, cutting taxes, and lowering interest rates to reduce unemployment and boost growth, even at the cost of a rising fiscal deficit.\n2. It can also refer to a temporary, sudden price rise in certain goods as an economy recovers from a recession following stimulative policy measures.\n3. Reflation is definitionally identical to stagflation.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct — reflation has two related senses (deliberate stimulus-driven growth strategy, and the resulting temporary price rise during recession recovery). Statement 3 is false, since stagflation (simultaneous high inflation AND high unemployment/stagnant growth) is essentially the opposite phenomenon to reflation's goal of REDUCING unemployment."})

upsc.append({"q":"Which one of the following statements about 'stagflation' is correct?","o":["It first prominently arose in the US economy during the 1970s, triggered by the oil price shocks of 1973 and 1979, and falsified the conventional Phillips Curve trade-off assumption","It refers to a situation of low inflation combined with low unemployment","It was first observed in India during the early 1990s Balance of Payments crisis","It describes a scenario where inflation and unemployment always move in strictly opposite directions, as predicted by the Phillips Curve"],"a":0,"e":"Stagflation — high inflation combined with high unemployment/stagnant growth — first prominently emerged in the 1970s US economy due to the 1973 and 1979 oil price shocks, directly contradicting the Phillips Curve's inflation-unemployment trade-off assumption and prompting a shift towards monetarist and supply-side economic policies."})

upsc.append({"q":"India formally commenced 'inflation targeting' through which agreement, signed in February 2015 between the Government of India and the RBI?","o":["The Agreement on Monetary Policy Framework","The Fiscal Responsibility and Budget Management Act","The Urjit Patel Committee Report","The Financial Sector Legislative Reforms Commission Report"],"a":0,"e":"The Agreement on Monetary Policy Framework, signed in February 2015 between the GoI and RBI, formally established India's inflation-targeting regime, aiming for a stable, officially targeted rate of inflation as a core monetary policy objective."})

upsc.append({"q":"Assertion (A): Inflation targeting is generally conducted by a country's Central Bank rather than its Finance Ministry.\nReason (R): Inflation targeting is fundamentally a monetary policy tool aimed at achieving a stable, officially announced target range for inflation.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are true and R explains A — since inflation targeting is a monetary policy instrument, it naturally falls within the Central Bank's (RBI's) mandate rather than the Finance Ministry's, consistent with how India's GoI-RBI Agreement on Monetary Policy Framework (2015) operationalised it."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_inflation_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")
