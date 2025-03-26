This project uses a K-Nearest Neighbors (KNN) model to predict soccer player positions (defense or midfield) based on key performance stats from the `players_XX.csv` dataset, derived from EA Sports FIFA 20 data.  

## Key Features  
- **Data Preprocessing**: Loaded and cleaned the dataset with Pandas, filtering out goalkeepers and categorizing positions as 'defense' (e.g., RB, CB, LB) or 'midfield' based on player position strings.  
- **Feature Selection**: Focused on four critical stats—`shooting`, `passing`, `dribbling`, and `defending`—to train the model.  
- **Model Training**: Implemented a KNN classifier (scikit-learn) with a train-test split (60/40, stratified) to predict positions.  
- **Performance**: Achieved a maximum accuracy of ~87.6% with `k=30` or `k=100` neighbors.  
- **Predictions**: Successfully classified real players like Steven Gerrard (midfield), Nemanja Vidic (defense), Jack Grealish (midfield), and Matty Cash (midfield) using their stats.  

## Tech Stack  
- Python  
- Pandas & NumPy (data manipulation)  
- Scikit-learn (KNN classifier, train-test split)  
- Dataset: `players_XX.csv` (FIFA 20 player stats)  

## Model Insights  
- **K-Value Testing**:  
  - `k=1`: 83.05%  
  - `k=3`: 85.64%  
  - `k=5`: 85.90%  
  - `k=10`: 86.79%  
  - `k=15`: 87.50%  
  - `k=30`: 87.61% (peak accuracy)  
  - `k=100`: 87.61%  
- **Accuracy Limit**: ~87% based on selected features, suggesting room for improvement with additional stats or features.  

## Usage  
1. Load the `players_XX.csv` dataset.  
2. Run the script to train the KNN model.  
3. Input new player stats (e.g., `[shooting, passing, dribbling, defending]`) to predict their position.  

Explore the code to see how machine learning can analyze soccer player roles! Contributions or ideas for improving accuracy are welcome.
