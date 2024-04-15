Overview
--------

A Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. Uses for Jupyter Notebooks include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more. Jupyter Notebooks are widely used in academia and industry for data analysis, scientific research, and education. They're a tool to streamline the process of working with data, writing code, and communicating results and insights.

JupyterHub is a multi-user version of the highly popular Jupyter Notebook, designed to serve notebooks to multiple users. It provides a convenient way to serve Jupyter Notebook and other types of interactive Jupyter environments to users who do not need to install anything on their own computers. JupyterHub runs in the cloud or on your own hardware, and it makes it easy to serve a pre-configured data science environment to any user with a web browser. This flexibility and ease of use have made it a fundamental tool in teaching, learning, and conducting data science at scale.

JupyterLab is an extensible environment for interactive and reproducible computing, based on the web. It is the next-generation web-based user interface for Project Jupyter and offers all the familiar building blocks of the classic Jupyter Notebook (like notebooks, terminals, text editors, file browsers, rich outputs, etc.) in a flexible and powerful user interface. JupyterLab has become increasingly popular for data science, scientific computing, and machine learning projects that require powerful tools and an efficient workflow.JupyterLab is designed to provide a comprehensive environment for scientific workflows that is both user-friendly and powerful. It is seen as the evolution of the classic notebook, providing a more robust and flexible interface that catifies to a wider range of workflows and integration needs.

Fire Insights comes with integration with Jupyter, JupyterLab and JupyterHub.

Details
=====

Fire can be used to, easily, create a downsampled dataset. Fire provides a **Sample** processor for it.

Once the dataset size is small, data scientists can use it to build model in Jupyter notebook.

Once the modeling process is complete, the algorithm can be run on the full data in Fire.

The Analytical Apps in Sparkflows, can submit Jupyter Notebook jobs on Kubernetes.
