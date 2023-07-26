```python
import pandas as pd
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['alien_life_predictor']
collection = db['subscriptions']

def track_adoption_rate():
    # Fetch subscription data
    subscription_data = pd.DataFrame(list(collection.find()))

    # Calculate the number of unique users
    unique_users = subscription_data['user_id'].nunique()

    # Calculate the number of unique institutions
    unique_institutions = subscription_data['institution_id'].nunique()

    # Calculate the adoption rate
    adoption_rate = (unique_users + unique_institutions) / (subscription_data.shape[0])

    return adoption_rate
```