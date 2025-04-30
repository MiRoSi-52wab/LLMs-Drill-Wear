import math

# -----------------------------
# Predefined coefficients (estimated based on physics)
alpha_0 = 1.5
alpha_1 = 2e-3   # per MPa (Young's modulus)
alpha_2 = 0.8    # dimensionless (Poisson's ratio)
alpha_3 = 1.5e-2 # per HV (Hardness)

# Wear sensitivity factor
beta = 1.5  # 150% torque increase at full wear

# Mechanistic model exponent (from drilling papers)
b = -0.6

# -----------------------------
# Functions

def compute_C2(E, nu, H):
    return alpha_0 + alpha_1 * E + alpha_2 * nu + alpha_3 * H

def compute_sharp_torque(C2, R, f, w, p_deg):
    p_rad = math.radians(p_deg)
    sin2_p = math.sin(p_rad)**2

    term1 = (C2 * (R**2) * f) / (b + 2)
    term2 = C2 * f * (w**2) * sin2_p

    return term1 + term2  # In Nmm

def estimate_wear(T_measured, T_sharp, beta):
    W = (T_measured - T_sharp) / (beta * T_sharp)
    return max(0.0, min(W, 1.0))

def auto_check_torque(T_measured, T_sharp, beta):
    T_failure = T_sharp * (1 + beta)
    if T_measured < 0.7 * T_sharp:
        print("\n⚠️ Warning: Measured torque is much LOWER than expected for sharp tool. Check units or sensor!")
    elif T_measured > 1.1 * T_failure:
        print("\n⚠️ Warning: Measured torque is much HIGHER than expected even for fully worn tool. Check units!")
    else:
        print("\n✅ Measured torque is within expected range.")

# -----------------------------
# User Input Section
print("\n===== Torque and Wear Prediction Mini-App =====")

# Material inputs
E = float(input("Enter Young's Modulus E (MPa): "))
nu = float(input("Enter Poisson's Ratio ν: "))
H = float(input("Enter Hardness H (HV): "))

# Drill and process inputs
R = float(input("Enter Drill Radius R (mm): "))
f = float(input("Enter Feed Rate f (mm/rev): "))
w = float(input("Enter Web Thickness w (mm): "))
p_deg = float(input("Enter Point Angle p (degrees): "))

# Measured torque input
T_measured_input = float(input("Enter Measured Torque (specify if N.m or N.mm): "))
unit_choice = input("Is this value in N.m? (y/n): ").lower()

if unit_choice == 'y':
    T_measured = T_measured_input * 1000  # Convert to Nmm
else:
    T_measured = T_measured_input  # Already in Nmm

# -----------------------------
# Run the model
C2 = compute_C2(E, nu, H)
T_sharp = compute_sharp_torque(C2, R, f, w, p_deg)

# Auto-check measured torque
auto_check_torque(T_measured, T_sharp, beta)

# Estimate wear
W = estimate_wear(T_measured, T_sharp, beta)

# -----------------------------
# Display results
print("\n===== Results =====")
print(f"Calculated C2 (sharp tool): {C2:.2f}")
print(f"Predicted Sharp Torque: {T_sharp/1000:.3f} Nm")
print(f"Measured Torque: {T_measured/1000:.3f} Nm")
print(f"Estimated Wear Level: {W*100:.1f}%")

print("\n===== End of Calculation =====\n")
