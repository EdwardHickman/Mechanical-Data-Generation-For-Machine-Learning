# **Mechanical Data Generation For Machine Learning**
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/maintenance%20status-deprecated-red)

A Python-based tool designed to streamline and automate the analysis of stress-strain data for composite materials, significantly reducing testing time and costs. This tool eliminates the need for manual stress-strain testing by leveraging web scraping, data processing, and visualization technologies.

---

## **Features**
- **Automation of Stress-Strain Analysis**: Eliminates manual testing, reducing testing time by **95%** and enabling significant cost savings.
- **Efficient Data Collection**: Utilizes **Selenium** for web scraping to streamline the acquisition of materials data from reputable sources.
- **Data Processing and Visualization**: 
  - Extracts key stress-strain data points and generates **detailed graphs** for analysis.
  - Implements **Matplotlib** to reorganize and interpolate data plots, enhancing **readability** and **usability**.
- **Future Analysis Support**: Identifies critical control points to aid in long-term data analysis and predictive modeling.

---

## **Getting Started**

### **Prerequisites**
- Python 3.10 or higher
- Required Python libraries:
  - Selenium
  - Matplotlib
  - Pandas
  - NumPy

---

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/EdwardHickman/Mechanical-Data-Generation-For-Machine-Learning
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Ensure you have the appropriate web driver installed for Selenium (e.g., ChromeDriver for Google Chrome).

---

## **Usage**

### **Step 1: Automate Data Collection**
Run homepage.py and enter a material name to scrape stress-strain data from a trusted materials database.  
```bash
python homepage.py
```

### **Step 2: Review the Output**

After running the scripts, the following outputs will be available:
- Graphs: Visualizations highlighting stress-strain behavior and key control points.
- Processed Data: A cleaned dataset stored in a CSV file for future analysis or integration will be opened when a graph is selected.

---

## **Impact**
- Reduced **testing time**, accelerating material development and analysis cycles.
- Improved **data accessibility** and **readability**, enabling faster and more accurate insights.
- Eliminated manual stress-strain testing, resulting in **significant cost savings** and efficiency improvements.
- Supported **future predictive modeling** through detailed graphs and key control points extracted from raw materials data.

---

## **Future Enhancements**
- Expand compatibility to support a wider range of **material types** and **testing scenarios**.
- Integrate **machine learning models** to predict stress-strain behavior and other material properties.
- Expand data gathering from a wider **variety of sources**.

---

## **What I Learned**
- Advanced Python programming, including **Selenium for web scraping** and **Matplotlib for data visualization**.
- Effective techniques for **automating manual processes** to save time and reduce costs.
- Skills in **data interpolation** and **cleaning** to improve the usability and accuracy of datasets.
- Practical experience in designing tools that support **real-world applications** in material science and engineering.


   

