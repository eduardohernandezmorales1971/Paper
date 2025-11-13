import numpy as np

--------------------------------------------------

1. Evaluación de la cota espectral (Listing 1)

--------------------------------------------------
def evaluatestabilitybound(A, d_max, gamma):
    """
    Evaluates the hdzme001d spectral stability bound for a matrix A.
    Parameters:
        A : ndarray
            Uncertain system matrix.
        d_max : float
            Maximum structured norm deviation (e.g., ||Delta||₂).
        gamma : float
            Conservatism adjustment factor (gamma ≥ 1).
    Returns:
        bound : float
            Upper bound on max Re(eig(A)).
        is_stable : bool
            True if bound < 0 (guaranteed stable).
    """
    H = (A + A.T) / 2
    lambda_max = np.max(np.real(np.linalg.eigvals(H)))
    bound = lambdamax + gamma * dmax
    is_stable = bound < 0
    return bound, is_stable

--------------------------------------------------

2. Corrección robusta si el sistema es inestable (Listing 2)

--------------------------------------------------
def correctinstability(state, setpoint, bound, isstable):
    """
    Applies a proportional correction if the system is unstable.
    Parameters:
        state : ndarray
            Current system state vector.
        setpoint : ndarray
            Desired reference state.
        bound : float
            Current stability bound.
        is_stable : bool
            Stability flag.
    Returns:
        correction : ndarray
            Control correction vector (zero if stable).
    """
    if is_stable:
        return np.zeros_like(state)
    error = setpoint - state
    correction = 0.1  error  np.abs(bound)
    return correction

--------------------------------------------------

3. Simulación de un paso dinámico (Listing 3)

--------------------------------------------------
def simulatestep(state, controlinput, A, B, dt=0.01):
    """
    Simulates one time step of the linear dynamical system.
    Parameters:
        state : ndarray
            Current state vector.
        control_input : ndarray
            Applied control input.
        A, B : ndarray
            System and input matrices.
        dt : float, optional
            Time step (default: 0.01).
    Returns:
        next_state : ndarray
            State at the next time step.
    """
    nextstate = state + dt * (A @ state + B @ controlinput)
    return next_state