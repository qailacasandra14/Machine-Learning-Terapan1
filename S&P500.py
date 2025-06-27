
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Load data
df = pd.read_csv('DataS&P500.csv') 

# Preprocessing: ubah kolom numerik dari object ke float
for col in ['Terakhir', 'Pembukaan', 'Tertinggi', 'Terendah']:
    df[col] = df[col].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

# Pilih fitur dan target
X = df[['Pembukaan', 'Tertinggi', 'Terendah']]
y = df['Terakhir']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisasi
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model dan GridSearch
model = KNeighborsRegressor()
param_grid = {'n_neighbors': range(1, 21)}
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='r2')
grid_search.fit(X_train_scaled, y_train)

# Output hasil terbaik
print("Best Parameters:", grid_search.best_params_)
print("Best R2 Score:", grid_search.best_score_)
