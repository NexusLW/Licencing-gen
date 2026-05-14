# Generador de Licencias

> 🇬🇧 [English version](README.md)

Utilidad de Python para generar claves de licencia seguras con fechas de vencimiento. Creado para [CentralCore](https://github.com/marius-db/CentralCore).

## Descripción General

El Generador de Licencias es una herramienta para crear claves de licencia criptográficamente firmadas. Cada clave codifica el correo del usuario y su fecha de vencimiento, protegida por HMAC-SHA256 para evitar manipulaciones.

---

## Características

- Encriptación HMAC-SHA256 para generación segura de licencias
- Codificación Base64 para portabilidad y legibilidad
- Codificación de correo y fecha de vencimiento en cada clave
- Interfaz interactiva de línea de comandos
- Sin dependencias externas - usa solo librería estándar de Python

---

## Requisitos

Python 3.6 o superior. Sin dependencias externas.

---

## Uso

### Modo Interactivo

```bash
python licence_generator.py
```

El script solicita:
- Email: Dirección de correo electrónico del usuario
- Expiry: Fecha de vencimiento en formato YYYY-MM-DD

Ejemplo:
```
Email: usuario@ejemplo.com
Expiry (YYYY-MM-DD): 2025-12-31
  LICENSE KEY
============================================================
YWRtaW5AZXhhbXBsZS5jb218MjAyNS0xMi0zMXxhYmNkZWY=
============================================================
```

### Uso Programático

```python
from licence_generator import generate_license

# Generar una clave de licencia
license_key = generate_license("usuario@ejemplo.com", "2025-12-31")
print(license_key)
```

---

## Cómo Funciona

1. Combina el correo y fecha de vencimiento: correo|vencimiento
2. Genera hash HMAC-SHA256 usando una clave secreta
3. Codifica el hash en Base64
4. Combina datos con hash: datos|hash
5. Codifica todo en Base64

El resultado es una clave a prueba de manipulaciones que puede ser validada por cualquier sistema con la misma clave secreta.

---

## Notas de Seguridad

- Cambia la clave SECRET en entornos de producción
- Mantén la clave SECRET confidencial - nunca la confirmes en control de versiones
- Usa HTTPS al transmitir claves de licencia
- Siempre valida las licencias del lado del servidor
- Considera usar un servicio de gestión de claves para uso en producción

---

## Proyectos Relacionados

- [CentralCore](https://github.com/marius-db/CentralCore) - Aplicación de escritorio que usa estas claves de licencia para validación de módulos
