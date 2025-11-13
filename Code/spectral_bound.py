import numpy as np
import time
import matplotlib.pyplot as plt
import csv

def hdzme001d_bound(Ac, Delta, gamma=1.1):
    Herm_Ac = 0.5 * (Ac + Ac.T)
    lambdamax = np.max(np.real(np.linalg.eigvals(HermAc)))
    Delta_norm = np.linalg.norm(Delta, 2)
    return lambdamax + gamma * Deltanorm

def isstablereal(A):
    alpha = np.max(np.real(np.linalg.eigvals(A)))
    return alpha < 0, alpha

def isnormalmatrix(A, tol=1e-8):
    commutator = A @ A.T - A.T @ A
    return np.linalg.norm(commutator, 'fro') < tol

def generateuncertainmatrix(n, delta=0.3):
    Ac = np.random.randn(n, n)
    U = np.random.randn(n, n)
    V = np.random.randn(n, n)
    Delta = delta * U @ V.T / np.linalg.norm(U @ V.T, 2)
    A = Ac + Delta
    return Ac, A, Delta

def analyzebound(n=5, trials=5000, gammavals=[1.0, 1.1, 1.25, 1.5]):
    results = {}
    for gamma in gamma_vals:
        FN = FP = 0
        errors = []
        times = []
        normal_count = 0
        normal_errors = []

        for _ in range(trials):
            Ac, A, Delta = generateuncertainmatrix(n)
            truestable, alphaA = isstablereal(A)
            isnormal = isnormal_matrix(A)

            t0 = time.time()
            bound = hdzme001d_bound(Ac, Delta, gamma)
            pred_stable = bound < 0
            times.append((time.time() - t0) * 1000)

            error = bound - alpha_A
            errors.append(error)
            if is_normal:
                normal_count += 1
                normal_errors.append(error)

            if not truestable and predstable:
                FN += 1
            if truestable and not predstable:
                FP += 1

        results[gamma] = {
            'FN': FN,
            'FP': FP,
            'FN_rate': FN / trials * 100,
            'FP_rate': FP / trials * 100,
            'Error_mean': np.mean(errors),
            'Error_std': np.std(errors),
            'Time_mean': np.mean(times),
            'Normalerrorsmean': np.mean(normalerrors) if normalerrors else np.nan
        }

    return results

def saveresultstocsv(results, filename='benchmarkresults.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'gamma', 'FN', 'FP', 'FNrate', 'FPrate',
            'Errormean', 'Errorstd', 'Timemean', 'Normalerrors_mean'
        ])
        for gamma, data in results.items():
            writer.writerow([
                gamma, data['FN'], data['FP'], data['FNrate'], data['FPrate'],
                data['Errormean'], data['Errorstd'], data['Timemean'], data['Normalerrors_mean']
            ])

if name == "main":
    results = analyze_bound()
    saveresultsto_csv(results)
    print("✅ Resultados guardados en 'benchmark_results.csv'")