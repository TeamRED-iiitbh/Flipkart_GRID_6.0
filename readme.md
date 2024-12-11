# Flipkart GRID 6.0  

This project tackles two core problems:  
1. **Product Attribute Extraction** - Extraction of attributes from product data.  
2. **Freshness Detection for Groceries** - Determining the freshness of grocery items.

## Directory Structure  

```bash
📂 Project Directory  
├── 📁 CODE             # Source Files
│   ├── 📂 build 
│   └── 📂 utilities
│  
├── 📁 IMAGE            # Output Images
├── 📁 MODEL            # Trained models (e.g., best.pt)  
├── 📁 VIDEO            # Sample Videos (input)  
├── 📝 main_fresh.py    # Grocery freshness detection script.  
├── 📝 main_product.py  # Product attribute extraction script.  
└── 📄 requirements.txt # package dependencies.  
```

## Setting Up the Environment  

1. **Create and Activate Conda Environment**:  
   ```bash
   conda create --name grid python=3.10 -y
   conda activate grid
   ```  

2. **Install Required Libraries**:  
   Use the `requirements.txt` file to install the necessary dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Run the Application**:  
   - For **product attribute extraction**, run:  
     ```bash
     python main_product.py
     ```  
   - For **grocery freshness detection**, run:  
     ```bash
     python main_fresh.py
     ```

## Accessing the User Interface  

Once the scripts are running, you can access the **web-based UI** for interacting with the outputs at:  
[Flipkart GRID 6.0 UI](https://flipkart-grid-ui.vercel.app/)  