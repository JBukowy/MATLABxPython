# MATLABxPython

This repository is to act as an onboarding for persons knowledgable with programming concepts in matlab but wish to adopt python as an alternative language. We will walk through installing python and working with virtual environments - understanding object oriented programming concepts and standard library data structures - as well as numpy, data science, and machine learning approaches and tools.

Most resources will be provided in jupyter notebooks, but before we access those - let's make sure that we have an appropriate version of python installed and that we are working in a virtual environment.

# Step 1: Check Python Installation
First, let's check if Python is already installed on your system. Open a new Jupyter Notebook and create a cell with the following code:

__macOS (using [Homebrew](https://brew.sh/)):__

_in a terminal window_

```brew install python```

__Windows (using the installer from Python's website)__

Download and run the installer from [python.org](python.org).

# Step 2: Create a Virtual Environment
Create a new virtual environment named myenv:

```python -m venv matlabxpython```

# Step 3: Activate the Virtual Environment
Activate the virtual environment. The activation command differs based on your operating system.

__macOS/Linux:__

```source matlabxpython/bin/activate```

__Windows:__

```matlabxpython\Scripts\activate```

You should see the virtual environment name (myenv) in your terminal prompt, indicating that it's active.

# Step 4: Install necessary libraries for running Jupyter Notebooks

With the virtual environment activated, install Jupyter Notebook:
```pip install jupyter```

In addition to jupyter, this command will also install all of the other necessary (and missing libraries) to be able to run jupyter.

# Step 5: Launch Jupyter Notebook
Start the Jupyter Notebook server from you terminal:
```jupyter notebook```

This command will start a local server and typically open your default web browser to the Jupyter Notebook interface. If you select the default kernel - it will use the virtual environment that you just created which is currently activated.

# Step 6: Creating and using Jupyter Notebooks
Open a new notebook or navigate to an existing notebook in the Jupyter interface.

## A word about python virtual environments, versions, and jupyter notebook kernels.

A __Python virtual environment__ is an isolated environment for Python projects, allowing you to manage dependencies and packages separately from the system-wide Python installation.

Use Cases:

- Dependency Management: Different projects may require different versions of the same packages. Virtual environments prevent version conflicts.
- Isolated Development: Each project can have its own environment with its own dependencies, making it easier to manage and deploy applications.
- Reproducibility: Ensures that the environment can be reproduced on different machines, which is crucial for collaboration and deployment.

A __Jupyter kernel__ is a computational engine that executes the code contained in Jupyter Notebooks. Each kernel is associated with a specific programming language and environment. For our purposes we will be using the virtual environment that we created in python as our jupyter kernel.

By associating a Jupyter Notebook kernel with a virtual environment, you ensure that the notebook uses the Python interpreter and packages from that virtual environment. This setup is crucial for managing dependencies and avoiding conflicts between different projects.

__Python is notoriously brittle when it comes to versions__ To save a lot of heartache one way to combat this is to record what package versions you are using in a virtual environment - especially when your experiment is working.
Using the following command will export a list of libraries/packages and their versions that the kernel is currently using.

```pip freeze > requirements.txt```

While this may not completely eliminate versioning headaches it is an easy first step to helping make work reproducible.

## Visual Studio Code
Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft. It is highly popular among developers due to its robust feature set, extensibility, and performance. VS Code supports a wide range of programming languages and development workflows, making it a versatile tool for various coding tasks.

Features of VS Code
- IntelliSense: Provides intelligent code completion, parameter info, quick info, and member lists.
- Debugging: Integrated debugging support for various languages.
- Extensions: A rich ecosystem of extensions available through the VS Code Marketplace, enabling additional features and language support.
- Version Control: Built-in support for Git and other version control systems.
- Terminal: Integrated terminal for running command-line tools within the editor.
- Customization: Highly customizable through settings, themes, and keybindings.
Why VS Code is Useful for Working with Jupyter Notebooks
- Jupyter Extension: VS Code has a Jupyter extension that allows you to create, edit, and run Jupyter Notebooks directly within the editor. This extension provides a seamless interface for working with .ipynb files.

### Getting Started with Jupyter Notebooks in VS Code
Install VS Code: Download and install Visual Studio Code from the official [website](https://code.visualstudio.com/).

Install the Python Extension: Open VS Code and install the Python extension from the Extensions Marketplace.

Install the Jupyter Extension: Install the Jupyter extension from the Extensions Marketplace to enable Jupyter Notebook support.

Create or Open a Notebook: Use the Command Palette (Ctrl+Shift+P or Cmd+Shift+P on macOS) to create a new Jupyter Notebook or open an existing one.

Associate Venv Kernel with notebook: Open the top working folder that contains your project and virtual environment subfolders. You can then create a new workbook.ipynb in vscode and find the venv kernel in the kernel selection pullodown menu.

Run Cells and Explore Outputs: Write code in the notebook cells and run them interactively. Use the built-in tools to explore variable states, visualize data, and debug your code.

With all of these steps in place, we can start to work with the same tools and go through some basics of using python.
