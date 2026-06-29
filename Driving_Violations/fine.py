import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Indian_Traffic_Violations.csv")

paid_df = df[df["Fine_Paid"] == "Yes"]

pivot = paid_df.pivot_table(
    index="Location",
    columns="Violation_Type",
    values="Fine_Amount",
    aggfunc="sum"
).fillna(0) / 1_000_000

colors = [
    "#e74c3c", "#3498db", "#2ecc71", "#f39c12",
    "#9b59b6", "#1abc9c", "#e67e22", "#e91e63", "#00bcd4"
]

states = pivot.index.tolist()
violations = pivot.columns.tolist()
x = np.arange(len(states))
bar_width = 0.08

fig, ax = plt.subplots(figsize=(16, 7))

for i, (violation, color) in enumerate(zip(violations, colors)):
    offset = (i - len(violations) / 2) * bar_width + bar_width / 2
    bars = ax.bar(
        x + offset,
        pivot[violation],
        width=bar_width,
        color=color,
        label=violation,
        edgecolor="white"
    )

ax.set_title(
    "Total Fine Paid per Violation Type across All States (₹ Millions)",
    fontsize=14, fontweight="bold", pad=15
)
ax.set_xlabel("State", fontsize=12)
ax.set_ylabel("Total Fine Paid (₹ Millions)", fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(states, rotation=20, ha="right", fontsize=11)
ax.legend(
    title="Violation Type",
    fontsize=9,
    title_fontsize=10,
    loc="upper right",
    bbox_to_anchor=(1.15, 1)
)
ax.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("state_violation_fine_barchart.png", dpi=300,
            bbox_inches="tight")
plt.show()
print("✅ Graph saved as state_violation_fine_barchart.png")
