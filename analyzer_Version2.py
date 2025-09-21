import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import os

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