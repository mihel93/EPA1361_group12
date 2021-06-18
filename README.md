# A flood risk management strategy for the province of Overijssel

## Foreword

This is the directory for the EPA1361 project, A flood risk management strategy for the province of Overijssel,
where the final report for the project is composed based on the works from this directory. 

The authors are:

Group 12B
O. Atta –5149002
J. van den Brink –4560698
M. Deligrozev –5217652
I. Jabri –4291034
J. Seol –5271495
J. van Walsum –4483995


## Structure

To walk you through the steps, it is advised to follow the order of documents as below:

1. Open exploration - This notebook explores the space of the flood risk management model and will present a perspective in how the model behaves if no policy is implemented. 

2. Scenario Discovery - This notebook looks for the possible scenario space using directed search method and narrows down the scenario space for the policy experiment using PRIM.

3. Policy Comparison - This notebook identifies the possible set of policies by running the experiments using the Latin Hypercube Sampling (LHS) method and compares the result with the base case policy.

4. Multi-Objective Robustness Optimization (MORO) - This notebook guides to the most favourable set of policies for the province of Overijssel among the policies explored in step 3 using Multi-Objective Robustness Optimization (MORO).



## File structure

data/ - Data provided by github.com/quaquel/epa1361_open
dike_model/ - The original dike_model provided by github.com/quaquel/epa1361_open
images/ - The visualizations of plots
results/ - The csv and pkl files of experiment runs

1_open_exploration_base_case.ipynb
2_scenario_discovery.ipynb
3_comparison.ipynb
4_MORO.ipynb 

README.md
requirements.txt