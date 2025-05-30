import numpy as np
import matplotlib.pyplot as plt

def perform_pca(X):
    """
    Perform Principal Component Analysis (PCA) on a 2D dataset.
    
    Parameters:
    - X: np.ndarray of shape (n_samples, 2), input data.

    Returns:
    - mean: mean of the data
    - eigenvalues: sorted eigenvalues
    - eigenvectors: corresponding eigenvectors
    - projected_data: data projected onto principal components
    """
    # Step 1: Center the data
    mean = X.mean(axis=0)
    X_centered = X - mean

    # Step 2: Covariance matrix
    cov_matrix = np.cov(X_centered.T)

    # Step 3: Eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Step 4: Sort eigenvalues and eigenvectors
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Step 5: Project the data
    projected_data = X_centered @ eigenvectors[:,0]

    if (len(projected_data.shape)==2):
        plt.figure(figsize=(8, 6))
        plt.scatter(projected_data[:, 0], projected_data[:, 1], color='blue', label='Projected points')
        plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
        plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)
        plt.title('PCA Projection')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    return mean, eigenvalues, eigenvectors, projected_data



X = np.array([
    [30,0], [30,10], [10,10], [20, 20],
    [20, 30], [10, 30], [10, 40]
], dtype=np.float64)

plt.scatter(X[:,0],X[:,1])
plt.show()

mean, evals, evecs, proj = perform_pca(X)
print(evecs[:,0])

