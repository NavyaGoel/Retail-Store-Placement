import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from scipy.spatial import ConvexHull

def find_optimal_store_location(customers, competitors, candidate_locations):
    min_distance = float('inf')
    optimal_location = None

    if len(customers) > 3:
        try:
            customer_hull = ConvexHull(customers)
            centroid = np.mean(customers[customer_hull.vertices], axis=0)
            optimal_location = centroid
        except ValueError:
            customer_hull = np.empty((0, 2))  # Empty array for plotting consistency

    return optimal_location, min_distance, customer_hull

# Example usage
np.random.seed(0)
num_customers = 100
num_competitors = 10
num_candidate_locations = 20

customers = np.random.rand(num_customers, 2)  # Customer locations (2D)
competitors = np.random.rand(num_competitors, 2)  # Competitor locations (2D)
candidate_locations = np.random.rand(num_candidate_locations, 2)  # Candidate store locations (2D)

optimal_location, min_distance, customer_hull = find_optimal_store_location(customers, competitors, candidate_locations)

plt.figure(figsize=(10, 8))
plt.scatter(customers[:, 0], customers[:, 1], c='blue', label='Customers')
plt.scatter(competitors[:, 0], competitors[:, 1], c='red', label='Competitors')

plt.scatter(candidate_locations[:, 0], candidate_locations[:, 1], c='green', alpha=0.3, label='All Candidates')

# Plot the convex hull
for simplex in customer_hull.simplices:
    plt.plot(customers[simplex, 0], customers[simplex, 1], 'k--', alpha=0.5)

# Plot the centroid of the convex hull of customer locations
plt.scatter(optimal_location[0], optimal_location[1], c='orange', label='Optimal Store Location', marker='*', s=200)

plt.legend()
plt.title('Retail Store Placement')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()

print("Optimal store location (centroid of convex hull):", optimal_location)
print("Minimum combined distance:", min_distance)
