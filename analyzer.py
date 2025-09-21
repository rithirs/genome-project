import random
import csv
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import os

HEIGHTS = ['Tall', 'Average', 'Short']
EYES = ['Black', 'Brown', 'Blue', 'Green']
HAIRS = ['Black', 'Brown', 'Blonde', 'Red']
BLOODS = ['A', 'B', 'AB', 'O']
SKINS = ['Fair', 'Medium', 'Dark']

TRAITS = {
    "height": HEIGHTS,
    "eye": EYES,
    "hair": HAIRS,
    "blood": BLOODS,
    "skin": SKINS,
}

def generate_population(n=50):
    population = []
    for _ in range(n):
        person = {
            "height": random.choice(HEIGHTS),
            "eye": random.choice(EYES),
            "hair": random.choice(HAIRS),
            "blood": random.choice(BLOODS),
            "skin": random.choice(SKINS),
        }
        population.append(person)
    return population

def trait_counts(population, trait):
    values = [person[trait] for person in population]
    return dict(Counter(values))

def dominant_trait(population, trait):
    counts = trait_counts(population, trait)
    dominant = max(counts, key=counts.get)
    return dominant

def analyze_traits(population):
    summary = {}
    for trait in TRAITS:
        summary[trait] = dominant_trait(population, trait)
    return summary

def save_csv(population, filename="dataset.csv"):
    keys = population[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(population)

def generate_graphs(population, out_dir='static/graphs'):
    os.makedirs(out_dir, exist_ok=True)
    graphs = {}
    for trait, options in TRAITS.items():
        counts = trait_counts(population, trait)
        labels = list(counts.keys())
        values = list(counts.values())
        plt.figure(figsize=(4,3))
        plt.bar(labels, values, color='skyblue')
        plt.title(f"{trait.title()} Distribution")
        plt.xlabel(trait.title())
        plt.ylabel("Count")
        bar_path = f"{out_dir}/{trait}_bar.png"
        plt.savefig(bar_path)
        plt.close()
        graphs[f"{trait}_bar"] = bar_path

        # Pie chart
        plt.figure(figsize=(4,3))
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title(f"{trait.title()} Distribution")
        pie_path = f"{out_dir}/{trait}_pie.png"
        plt.savefig(pie_path)
        plt.close()
        graphs[f"{trait}_pie"] = pie_path
    return graphs
