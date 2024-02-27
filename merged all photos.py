from moviepy.editor import ImageSequenceClip
from PIL import Image
import os

# Ruta donde se encuentran tus fotos
directorio_fotos = '# photo path'
# Nombre del archivo de video de salida
nombre_archivo_salida = 'video_final.mp4'
# Duración en segundos que deseas mostrar cada foto
duracion_foto = 5
# Tamaño uniforme al que se redimensionarán todas las imágenes (ancho, alto)
tamaño_objetivo = (1920, 1080)

# Lista para almacenar las rutas de las imágenes redimensionadas
archivos_redimensionados = []

# Lista todos los archivos en el directorio y filtra los que son imágenes
archivos = [archivo for archivo in os.listdir(directorio_fotos) if archivo.endswith((".jpg", ".jpeg", ".png"))]
archivos.sort()  # Ordena los archivos por nombre

# Redimensiona las imágenes
for archivo in archivos:
    ruta_completa = os.path.join(directorio_fotos, archivo)
    img = Image.open(ruta_completa)
    img_redimensionada = img.resize(tamaño_objetivo, Image.Resampling.LANCZOS)  # Corrección aquí
    ruta_temporal = os.path.join(directorio_fotos, f"temp_{archivo}")
    img_redimensionada.save(ruta_temporal)
    archivos_redimensionados.append(ruta_temporal)

# Crea un clip de video a partir de las imágenes redimensionadas
clip = ImageSequenceClip(archivos_redimensionados, durations=[duracion_foto] * len(archivos_redimensionados))

# Exporta el video
clip.write_videofile(nombre_archivo_salida, fps=24)

# Opcional: Limpia las imágenes temporales redimensionadas
for archivo in archivos_redimensionados:
    os.remove(archivo)
