import numpy as np
import matplotlib.pyplot as plt

# ============================================
# Parámetros de muestreo
# ============================================
fs = 1000          # Frecuencia de muestreo (Hz)
T = 1.0            # Duración de la señal (s)
N = int(fs * T)    # Número de muestras
t = np.linspace(0, T, N, endpoint=False)

# ============================================
# Definición de señales
# ============================================

# Señal 1: Senoidal pura de 50 Hz
x1 = np.sin(2 * np.pi * 50 * t)

# Señal 2: Suma de senoidales (50 Hz + 120 Hz + 200 Hz)
x2 = (np.sin(2 * np.pi * 50 * t) +
      0.5 * np.sin(2 * np.pi * 120 * t) +
      0.3 * np.sin(2 * np.pi * 200 * t))

# Señal 3: Pulso rectangular
x3 = np.where((t >= 0.3) & (t <= 0.6), 1.0, 0.0)

# Señal 4: Tren de pulsos (onda cuadrada)
x4 = np.sign(np.sin(2 * np.pi * 10 * t))

# ============================================
# Función para calcular y graficar FFT
# ============================================
def analizar_senal(t, x, fs, titulo):
    N = len(x)
    # Cálculo de la FFT
    X = np.fft.fft(x)
    # Vector de frecuencias
    freqs = np.fft.fftfreq(N, d=1/fs)
    
    # Solo frecuencias positivas
    idx = freqs >= 0
    freqs_pos = freqs[idx]
    magnitud = np.abs(X[idx]) / N * 2  # Normalización
    
    # Gráficas
    fig, axes = plt.subplots(1, 2, figsize=(14, 4))
    
    # Dominio del tiempo
    axes[0].plot(t, x, 'b', linewidth=1.2)
    axes[0].set_title(f'{titulo} - Dominio del Tiempo')
    axes[0].set_xlabel('Tiempo [s]')
    axes[0].set_ylabel('Amplitud')
    axes[0].grid(True, alpha=0.3)
    
    # Dominio de la frecuencia
    axes[1].stem(freqs_pos, magnitud, basefmt=" ", markerfmt='ro')
    axes[1].set_title(f'{titulo} - Espectro de Frecuencia')
    axes[1].set_xlabel('Frecuencia [Hz]')
    axes[1].set_ylabel('Magnitud')
    axes[1].set_xlim(0, 250)
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# ============================================
# Análisis de cada señal
# ============================================
analizar_senal(t, x1, fs, "Señal 1: Senoidal 50 Hz")
analizar_senal(t, x2, fs, "Señal 2: Suma de senoidales")
analizar_senal(t, x3, fs, "Señal 3: Pulso rectangular")
analizar_senal(t, x4, fs, "Señal 4: Onda cuadrada 10 Hz")