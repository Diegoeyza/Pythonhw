import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def find_zero_slope_point(vds, ids):
    """
    Identify the Vds point where the slope of the Ids curve becomes zero.
    """
    slopes = np.gradient(ids, vds)
    zero_slope_idx = np.argmin(np.abs(slopes))  # Closest to zero slope
    return vds[zero_slope_idx], ids[zero_slope_idx]

def smooth_triode_region(vds, ids, zero_slope_vds, zero_slope_ids):
    """
    Generate a smooth triode region starting at (0, 0) and transitioning
    naturally into the active region.
    """
    triode_vds = vds[vds <= zero_slope_vds]
    triode_ids = zero_slope_ids * np.sqrt(triode_vds / zero_slope_vds)
    active_region_vds = vds[vds > zero_slope_vds]
    active_region_ids = ids[vds > zero_slope_vds]
    return (
        np.concatenate([triode_vds, active_region_vds]),
        np.concatenate([triode_ids, active_region_ids]),
    )

def generate_additional_curves(vds1, ids1, vds2, ids2, num_curves=3, num_extrapolated=5):
    """
    Generate additional curves between and above two existing Ids vs Vds curves.
    """
    # Resample curves to match lengths
    vds_common = np.linspace(0, min(vds1.max(), vds2.max()), 500)
    ids1_resampled = np.interp(vds_common, vds1, ids1)
    ids2_resampled = np.interp(vds_common, vds2, ids2)
    
    # Identify zero-slope points
    vds1_zero, ids1_zero = find_zero_slope_point(vds_common, ids1_resampled)
    vds2_zero, ids2_zero = find_zero_slope_point(vds_common, ids2_resampled)
    
    # Generate intermediate Vgs curves with fewer curves
    curves = []
    for i in range(1, num_curves + 1):
        alpha = i / (num_curves + 1)  # Increase spacing by reducing num_curves+2
        
        # Interpolate Ids and zero-slope points
        ids_interpolated = (1 - alpha) * ids1_resampled + alpha * ids2_resampled
        vds_zero_interpolated = (1 - alpha) * vds1_zero + alpha * vds2_zero
        ids_zero_interpolated = (1 - alpha) * ids1_zero + alpha * ids2_zero
        
        # Smoothly generate triode region
        vds_interpolated, ids_interpolated = smooth_triode_region(
            vds_common, ids_interpolated, vds_zero_interpolated, ids_zero_interpolated
        )
        
        # Apply the scaling factor to Ids
        ids_interpolated *= 0.0001
        curves.append((vds_interpolated, ids_interpolated))
    
    # Generate extrapolated curves (above the existing range) with more variable separation
    for i in range(1, num_extrapolated + 1):
        alpha = i / (num_extrapolated + 1)  # Increase spacing by reducing num_extrapolated+2
        
        # Extrapolate Ids with a larger factor for higher Ids
        extrapolation_factor = 1 + alpha * 3.0  # Increased factor for more separation
        ids_extrapolated = ids2_resampled * extrapolation_factor
        
        # Adjust transition point for extrapolated curves
        # We shift the transition into the active region to match the original curves' behavior
        shift_factor = 1 + alpha * 1  # Increase this factor to make the shift more pronounced
        vds_zero_extrapolated = vds2_zero + shift_factor * (vds2_zero - vds1_zero)
        ids_zero_extrapolated = ids2_zero * extrapolation_factor
        
        # Smoothly generate triode region for extrapolated curves
        vds_extrapolated, ids_extrapolated = smooth_triode_region(
            vds_common, ids_extrapolated, vds_zero_extrapolated, ids_zero_extrapolated
        )
        
        # Apply the scaling factor to Ids
        ids_extrapolated *= 0.0001
        curves.append((vds_extrapolated, ids_extrapolated))
    
    return curves

def plot_mosfet_curves(file1, file2, num_curves=3, num_extrapolated=5):
    """
    Plot original and generated MOSFET curves from two CSV files.
    """
    # Load data from CSV files
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)
    
    vds1, ids1 = data1['Vds'].values, data1['Ids'].values
    vds2, ids2 = data2['Vds'].values, data2['Ids'].values
    
    # Generate additional curves
    additional_curves = generate_additional_curves(vds1, ids1, vds2, ids2, num_curves, num_extrapolated)
    
    # Plot original curves
    plt.figure(figsize=(10, 6))
    plt.plot(vds1, ids1 * 0.0001, label='Original Curve 1', linestyle='-', color='blue')  # Apply scaling here as well
    plt.plot(vds2, ids2 * 0.0001, label='Original Curve 2', linestyle='-', color='orange')  # Apply scaling here as well
    
    # Plot additional curves
    for i, (vds, ids) in enumerate(additional_curves):
        plt.plot(vds, ids, label=f'Generated Curve {i + 1}', linestyle='--')
    
    # Plot formatting
    plt.title('Ids vs Vds extrapolated')
    plt.xlabel('Vds (V)')
    plt.ylabel('Ids (A)')
    plt.legend(loc='upper left', fontsize='small', frameon=True)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage:
file1 = r"C:\Users\diego\Downloads\vds-ids - 1.5 Vg.csv"  # Replace with the actual path to the first CSV
file2 = r"C:\Users\diego\Downloads\vds-ids - 1v Vg.csv"  # Replace with the actual path to the second CSV
plot_mosfet_curves(file1, file2, num_curves=3, num_extrapolated=5)
