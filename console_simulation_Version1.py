import time
from analyzer import TRAITS, dominant_trait

def loading_bar(trait, result):
    print(f"Analyzing {trait.title()}... Matching with genome database...")
    for percent in [25, 50, 75, 100]:
        print(f"... {percent}% ...", end="", flush=True)
        time.sleep(0.4)
    print(f"\n✔ Most common {trait.title()} found → {result}\n")

def analyze_with_loading(population):
    for trait in TRAITS:
        result = dominant_trait(population, trait)
        loading_bar(trait, result)