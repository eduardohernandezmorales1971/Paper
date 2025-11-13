Spectral Bound for Robust Stability Validation

   This repository contains the manuscript, code, and simulation data for the proposed ultra-fast spectral bound.

Contents
   - 📄 Manuscript (PDF)
   - 🧮 Python and MATLAB code
   - 📊 Benchmark results
   - 📜 README with technical and ceremonial documentation

Author
   Eduardo Hernández Morales  
   Independent Researcher, Morelia, Michoacán, México  
   ORCID: https://orcid.org/0009-0004-5366-8511


📦 Estructura del Repositorio

Este repositorio contiene los componentes esenciales del método hdzme001d para validación robusta de estabilidad espectral en sistemas inciertos.

📄 Manuscritos

- /manuscript/hdzme001dspectralbound.pdf — Artículo internacional con formulación teórica, validación masiva y aplicaciones reales
- /manuscript/tesis.pdf — Tesis original con fundamentos algebraicos y motivación histórica
- /manuscript/articulo_nacional.pdf — Versión nacional con enfoque pedagógico y contextual

🐍 Código

- /code/spectral_bound.py — Script principal que ejecuta 20,000 simulaciones para validar la cota hdzme001d. Genera:
  - benchmark_results.csv con tasas de error, tiempos y falsos positivos/negativos
  - sensitivity_gamma.png con gráfica de sensibilidad

- /code/hdzme001d_utilities.py — Módulo auxiliar con funciones para:
  - Evaluar la cota espectral en tiempo real
  - Aplicar corrección si el sistema es inestable
  - Simular un paso dinámico

- /code/example_usage.py — Ejemplo práctico que muestra cómo usar las funciones anteriores en un sistema incierto

📊 Datos

- /data/benchmark_results.csv — Resultados empíricos de 20,000 simulaciones con 4 valores de γ

---

🚀 Ejecución

Para ejecutar el análisis completo:

`bash
python spectral_bound.py
`

Para usar las funciones en simulaciones:

`python
from hdzme001dutilities import evaluatestabilitybound, correctinstability, simulate_step
