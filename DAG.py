import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# This script simulates two independent traits (`talent` and `beauty`)
# and demonstrates how conditioning on a common effect (a collider)
# — here `is_celebrity` — can induce a spurious association between
# otherwise independent variables. See README.md for more detail.

#1. Set seed for reproducibility
np.random.seed(42)
n=10000

#2. Simulate Independent Feathers (True Causal Effects = 0)
# Simulate two independent standard normal traits
talent = np.random.normal(loc=0, scale=1, size=n)
beauty = np.random.normal(loc=0, scale=1, size=n)

#3. Create the Collider (Celebraty Satus)
# Someone becomes a celebrity if they are either talented or beautiful, but not both. This creates a collider.
# Create a latent score that depends on both traits + noise.
# Turning this into a binary indicator produces a collider:
# `is_celebrity` is a common effect of `talent` and `beauty`.
Celebrity_score= talent + beauty + np.random.normal(loc=0, scale=0.5, size=n)
is_celebrity = (Celebrity_score > 1.5).astype(int)

#combine into a DataFrame

df= pd.DataFrame({'talent': talent, 'beauty': beauty, 'is_celebrity': is_celebrity})

# Analysis 1: General Pop (The Unconditioned, True Graph)

# 1) Regression in the full population (no conditioning)
model_pop = smf.ols('talent ~ beauty', data=df).fit()

print("Analysis 1: General Population (Unconditioned)")
print(f"Estimated Coefficient for Beauty: {model_pop.params['beauty']:.4f}")
print(f"P-value for Beauty: {model_pop.pvalues['beauty']:.4f}")

#Analysis 2: Conditioned on Celebrity Status (The Collider)
# 2) Regression conditioned on the collider (`is_celebrity`)
df_celebrity = df[df['is_celebrity'] == 1]
model_collider = smf.ols('talent ~ beauty', data=df_celebrity).fit()

print("\nAnalysis 2: Conditioned on Celebrity Status (Collider)")
print(f"Estimated Coefficient for Beauty: {model_collider.params['beauty']:.4f}")
print(f"P-value for Beauty: {model_collider.pvalues['beauty']:.4f}")

# Optional: if you want to visualize, uncomment the block below.
# plt.figure(figsize=(12,5))
# plt.subplot(1,2,1)
# plt.scatter(df['beauty'], df['talent'], alpha=0.2)
# plt.title('Full sample')
# plt.xlabel('beauty'); plt.ylabel('talent')
# plt.subplot(1,2,2)
# plt.scatter(df_celebrity['beauty'], df_celebrity['talent'], alpha=0.3, color='orange')
# plt.title('Celebrities only (conditioned on collider)')
# plt.xlabel('beauty'); plt.ylabel('talent')
# plt.tight_layout()
# plt.show()
