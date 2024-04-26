import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

def find_optimal_store_location(customers, competitors, candidate_locations):
    min_distance = float('inf')
    optimal_location = None
    
    for location in candidate_locations:
        # Calculate distances from each candidate location to customers and competitors
        distances_to_customers = cdist([location], customers)
        distances_to_competitors = cdist([location], competitors)
        
        # Find the minimum distance to customers and competitors
        min_distance_to_customers = np.min(distances_to_customers)
        min_distance_to_competitors = np.min(distances_to_competitors)
        
        # Combine distances to customers and competitors (e.g., using a weighted sum)
        combined_distance = min_distance_to_customers - 0.5 * min_distance_to_competitors
        
        # Update optimal location if combined distance is minimized
        if combined_distance < min_distance:
            min_distance = combined_distance
            optimal_location = location
    
    return optimal_location, min_distance

# Example usage
# Generate synthetic data for customers, competitors, and candidate store locations
np.random.seed(0)
num_customers = 100
num_competitors = 10
num_candidate_locations = 20

customers = np.random.rand(num_customers, 2)  # Customer locations (2D)
competitors = np.random.rand(num_competitors, 2)  # Competitor locations (2D)
candidate_locations = np.random.rand(num_candidate_locations, 2)  # Candidate store locations (2D)

# Find the optimal store location based on the closest pair problem
optimal_location, min_distance = find_optimal_store_location(customers, competitors, candidate_locations)

# Visualize customer locations, competitor locations, candidate store locations, and optimal store location
plt.figure(figsize=(10, 8))
plt.scatter(customers[:, 0], customers[:, 1], c='blue', label='Customers')
plt.scatter(competitors[:, 0], competitors[:, 1], c='red', label='Competitors')
plt.scatter(candidate_locations[:, 0], candidate_locations[:, 1], c='green', label='Candidate Locations')
plt.scatter(optimal_location[0], optimal_location[1], c='orange', label='Optimal Store Location', marker='*', s=200)
plt.legend()
plt.title('Retail Store Placement')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()

print("Optimal store location:", optimal_location)
print("Minimum combined distance:", min_distance)
