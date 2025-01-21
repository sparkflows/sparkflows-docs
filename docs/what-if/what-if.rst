What-If Analysis
=================

This document provides an overview of What-If Analysis, explaining its features and importance. It also details step-by-step instructions for accessing and using the What-If Simulator in Sparkflows to analyze and validate machine learning models effectively.


Overview
-----------

What-If Analysis is a powerful technique that allows users to explore and evaluate the potential outcomes of different scenarios by altering input variables or conditions, providing valuable insights into decision-making processes and model behavior. It serves as a crucial tool in fields like finance, engineering, and data science, helping analysts and decision-makers anticipate and prepare for various possible situations.

**Unveiling the Power of What-If Analysis:**

What-If are invaluable tools for data scientists and business analysts alike. They enable you to gain insights into model predictions under varying input scenarios, making them essential for debugging, explanation, fairness, and security of your machine learning models.

**The What-If Simulator:**

Once you’ve trained a machine learning model using Sparkflows, you gain access to the What-If simulator, a dynamic feature that empowers you to experiment with a multitude of input combinations for critical features and observe the resulting predictions. What-If Analysis is a fundamental component of this, allowing you to investigate model behavior and output stability.

**Accessibility and Customization:**

Data scientists can harness the What-If simulator seamlessly within the Visual ML interface. Additionally, you can share this feature with a broader audience by embedding it in interactive dashboards. What-If Analysis goes beyond traditional assessment practices, offering a deeper understanding of your model’s behavior.

**Tailored Input Manipulation and Impact Assessment:**

The What-If simulator offers unparalleled flexibility. You can adjust input values using intuitive drop-down menus and sliders, input your own values, or simulate scenarios where specific features are missing. On the right-hand side, you can promptly assess the updated prediction based on your input variations.

**What-If Analysis - Validating Model Stability:**

What-If Analysis is a vital validation technique for machine learning models. It involves scoring your trained model on single rows, multiple rows, or an entire dataset with potentially interesting simulated values. Then, you compare the model’s new outcomes to the predicted outcomes on the original data. WIA helps determine whether your model’s behavior and outputs remain stable when data is intentionally perturbed or other changes are simulated.

**Ensuring Trust and Fairness:**

Machine learning models can exhibit drastically different predictions for minor changes in input variables. For instance, when making predictions that influence financial decisions, What-if analysis can help you understand the impact of changing essential input variables. If the model responds in expected ways when critical variables change, it enhances trust in the model. Similarly, if changes to sensitive variables have minimal impact, it signifies fairness in the model predictions.

Incorporating What-If Analysis into your machine learning workflow with Sparkflows is essential for robust, explainable, and fair model development and deployment.


Steps to Access and Use the What-If Tool in Sparkflows
---------------------------------------------------------
Below are the steps and ways on how the What-If can be accessed in Sparkflows:

Step 1 : Access the What-If Tool
++++++++++++++++++++++++++++++++++
Access the What-If tool from either the left menu of the Model Repository page or the main menu on top.

   .. figure:: ../_assets/what-if/whatif-1.png
      :alt: What-If
      :width: 65%

Step 2 : Select Dataset and Engine to generate Input Controls
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Select the dataset and engine to perform the What-If analysis, and click on Run.

   .. figure:: ../_assets/what-if/whatif-2-select-dataset-engine.png
      :alt: What-If
      :width: 65%

Clicking on Run performs the summary statistic computation on the data and automatically creates the dropdown for categorical features and sliders for numerical features as shown below:

   .. figure:: ../_assets/what-if/whatif-3-auto-creates-sliders-dropdown.png
      :alt: What-If
      :width: 20%

   .. figure:: ../_assets/what-if/whatif-3-auto-creates-sliders-dropdown-2.png
      :alt: What-If
      :width: 20%


Step 3 : View Summary Statistics
+++++++++++++++++++++++++++++++++++++
Access the summary statistics for the data in the **Features** tab.

   .. figure:: ../_assets/what-if/whatif-4-features-metadata.png
      :alt: What-If
      :width: 65%


Step 4 : Adjust Inputs and View Predictions
+++++++++++++++++++++++++++++++++++++++++++++
Use the sliders and dropdowns to modify input values and click on **Score** to view the prediction along with Shapley values that explain the outcome.

   .. figure:: ../_assets/what-if/whatif-5-choose-value-slider.png
      :alt: What-If
      :width: 20%


Step 5 : Analyze Use Cases
+++++++++++++++++++++++++++++

#. Perform What-If analysis to evaluate **regression** use cases.

   .. figure:: ../_assets/what-if/whatif-6-click-on-score-gets-shapley-contributions-regression.png
      :alt: What-If
      :width: 65%

#. Conduct What-If analysis to explore **binomial** classification predictions.

   .. figure:: ../_assets/what-if/whatif-7-click-on-score-gets-shapley-contributions-classification.png
      :alt: What-If
      :width: 65%



