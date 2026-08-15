import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_basic_concepts (Ramesh Singh Ch.1, Introduction)
# Distribution network models, three economic systems (capitalism/Adam Smith,
# state economy/Marx, mixed economy/Keynes)
# ==================================================================

upsc.append({"q":"Consider the following statements about the three historically existing 'distribution network models' for goods and services in an economy:\n1. In the state distribution model, the government supplies goods and services with no direct payment by consumers, as practised in the former Soviet Union and Communist China.\n2. In the market distribution model, prices are determined by demand and supply in the open market, characteristic of Euro-American capitalist economies.\n3. The state-market mix model, the most prevalent mode today, combines freely/subsidised state-supplied goods with market-supplied goods requiring consumer payment.\nHow many of the statements given above are correct?","o":["All three","Only two","Only one","None"],"a":0,"e":"All three statements accurately describe the state, market, and state-market mix distribution models, with the mixed model being the most commonly followed today, its precise state-market ratio evolving with an economy's changing socio-economic composition."})

upsc.append({"q":"The origins of the capitalist economic system are most closely associated with which one of the following works and authors?","o":["Adam Smith's 'The Wealth of Nations' (1776)","Karl Marx's 'Das Kapital'","John Maynard Keynes' 'The General Theory of Employment, Interest and Money'","David Ricardo's 'Principles of Political Economy and Taxation'"],"a":0,"e":"Adam Smith's 'Wealth of Nations' (1776) is credited with laying the intellectual foundation of capitalism, emphasising division of labour, laissez-faire (non-interference), and the 'invisible hand' of market forces bringing economic equilibrium — ideas adopted into US public policy just a year after publication."})

upsc.append({"q":"Which one of the following terms is NOT among the alternative names historically used for the capitalist economic system, as it spread across Euro-America by 1800?","o":["Centrally Planned Economy","Private Enterprise System","Free Enterprise System","Market Economy"],"a":0,"e":"'Centrally Planned Economy' is instead an alternative name for the STATE economy (socialist/communist systems based on Karl Marx's ideas), not capitalism — capitalism has been alternatively termed Private Enterprise System, Free Enterprise System, or Market Economy."})

upsc.append({"q":"Consider the following statements about the 'State Economy' model rooted in Karl Marx's ideas:\n1. It first emerged in the erstwhile USSR following the Bolshevik Revolution of 1917, and took its 'ideal shape' in the People's Republic of China from 1949.\n2. Socialist economies emphasised collective ownership of the means of production with a large state role, while communist economies advocated state ownership of all properties including labour.\n3. For Marx, communism was envisioned as a transitional stage eventually leading to socialism.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 reverses Marx's actual formulation — he envisioned SOCIALISM as the transitional stage leading to COMMUNISM (not the other way round), though this transition never materialised in practice as originally theorised."})

upsc.append({"q":"Which one of the following events is credited with dealing a major setback to the belief in the market's self-correcting 'invisible hand', directly motivating John Maynard Keynes' 1936 work?","o":["The Great Depression (1929)","World War I (1914-1918)","The Bolshevik Revolution (1917)","The formation of the People's Republic of China (1949)"],"a":0,"e":"The Great Depression (starting 1929), which spread from the USA to Western Europe causing mass unemployment and economic collapse, exposed the failure of pure laissez-faire Smithonian economics to self-correct, directly prompting Keynes' 'General Theory of Employment, Interest and Money' (1936) and the mixed-economy approach."})

upsc.append({"q":"Assertion (A): Both capitalist critics of state economies and state-economy proponents used similar rhetorical accusations against each other.\nReason (R): Capitalist economies accused socialist/communist systems of practising 'state capitalism' where the state itself became the sole exploitator, while socialist/communist economies accused capitalism of being inherently exploitative.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are true and R explains A — this mutual 'exploitation' framing (capitalism accused of exploiting labour/consumers; state economies accused of practising 'state capitalism' with the state as sole exploitator) characterised the intense communist versus anti-communist intellectual debates lasting until roughly the mid-1980s."})

upsc.append({"q":"Which one of the following statements correctly distinguishes 'economics' from 'economy' as used in the introductory conceptual framework of this book?","o":["Economy is 'economics at play' in a particular context, while economics is the broader discipline studying economic activities and principles","Economy and economics are fully interchangeable terms with no conceptual distinction","Economics refers only to government policy, while economy refers only to private enterprise activity","Economy is a subset of political science, while economics is a subset of sociology"],"a":0,"e":"The text explicitly frames 'economy' as economics being applied/practised in a specific real-world context (a country's actual economic system and activity), while 'economics' is the broader academic discipline that studies economic activities, principles and behaviour."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_basic_concepts_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")
