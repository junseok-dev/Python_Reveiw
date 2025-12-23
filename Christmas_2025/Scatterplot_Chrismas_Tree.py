
import matplotlib.pyplot as plt
import numpy as np

def create_christmas_tree():
    """
    Generates a Data Science Christmas Tree using Matplotlib.
    The foliage is generated using random uniform distributions, resembling data points.
    """
    print("Initializing Data Science Christmas Tree Protocol...")
    
    # Set seed for reproducibility
    np.random.seed(25)

    # Setup the figure
    fig, ax = plt.subplots(figsize=(10, 12))
    dark_bg = '#1a1a2e'
    fig.patch.set_facecolor(dark_bg)
    ax.set_facecolor(dark_bg)

    # ---------------------------------------------------------
    # 1. Generate Tree Foliage (The Data)
    # ---------------------------------------------------------
    # We will use 3 overlapping triangles (trapezoids) to form the tree
    # Modeled as uniform distributions with shrinking width
    
    # Bottom layer
    n_points_bottom = 4000
    y_bottom = np.random.uniform(1, 4.5, n_points_bottom)
    w_bottom = 3.5 * (1 - (y_bottom - 1) / 3.5)
    x_bottom = np.random.uniform(-w_bottom, w_bottom)

    # Middle layer
    n_points_mid = 3000
    y_mid = np.random.uniform(4, 7.5, n_points_mid)
    w_mid = 2.8 * (1 - (y_mid - 4) / 3.5)
    x_mid = np.random.uniform(-w_mid, w_mid)

    # Top layer
    n_points_top = 2000
    y_top = np.random.uniform(7, 9.5, n_points_top)
    w_top = 1.8 * (1 - (y_top - 7) / 2.5)
    x_top = np.random.uniform(-w_top, w_top)

    # Combine all layers
    x_tree = np.concatenate([x_bottom, x_mid, x_top])
    y_tree = np.concatenate([y_bottom, y_mid, y_top])

    # Plot the foliage
    ax.scatter(x_tree, y_tree, s=2, c='#2ecc71', alpha=0.6, label='Tree Nodes')
    # Add some "depth" with darker points
    ax.scatter(x_tree, y_tree, s=1, c='#27ae60', alpha=0.3)

    # ---------------------------------------------------------
    # 2. Add Ornaments (Anomalies / Clusters)
    # ---------------------------------------------------------
    # Select random points to be ornaments
    n_ornaments = 120
    # Choose random indices
    idx = np.random.choice(len(x_tree), n_ornaments, replace=False)
    
    # Colors for the ornaments
    colors = ['#e74c3c', '#f1c40f', '#3498db', '#9b59b6', '#e67e22']
    ornament_colors = np.random.choice(colors, n_ornaments)
    
    ax.scatter(x_tree[idx], y_tree[idx], s=30, c=ornament_colors, edgecolors='white', linewidth=0.5, zorder=5)

    # ---------------------------------------------------------
    # 3. Add The Star (Global Maxima)
    # ---------------------------------------------------------
    ax.scatter(0, 9.7, s=500, c='#f1c40f', marker='*', edgecolors='#f39c12', linewidth=1, zorder=10)
    # Glow effect for the star
    ax.scatter(0, 9.7, s=1000, c='#f1c40f', marker='o', alpha=0.2, zorder=9)

    # ---------------------------------------------------------
    # 4. Add Snow (Noise)
    # ---------------------------------------------------------
    n_snow = 300
    x_snow = np.random.uniform(-5, 5, n_snow)
    y_snow = np.random.uniform(0, 10, n_snow)
    sizes_snow = np.random.uniform(5, 20, n_snow)
    ax.scatter(x_snow, y_snow, s=sizes_snow, c='white', alpha=0.3, zorder=0)

    # ---------------------------------------------------------
    # 5. Decoration and Text
    # ---------------------------------------------------------
    
    # Custom Trunk
    ax.fill_between([-0.5, 0.5], [0, 0], [1, 1], color='#795548', zorder=1)

    # Text
    plt.title("Merry Christmas\n& Happy New Year!", color='white', fontsize=20, fontfamily='monospace', pad=20)
    plt.xlabel("x_distribution", color='gray')
    plt.ylabel("y_height", color='gray')
    
    # Add a code snippet as a caption
    code_caption = "y_tree = f(Christmas_Spirit) + epsilon"
    plt.text(0, -0.5, code_caption, color='#2ecc71', fontsize=12, ha='center', fontfamily='monospace', alpha=0.8)

    # Adjust Limits and remove spines
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1, 11)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='x', colors='gray')
    ax.tick_params(axis='y', colors='gray')

    # Save
    output_file = 'christmas_tree_data_science.png'
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, facecolor=dark_bg)
    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    create_christmas_tree()
