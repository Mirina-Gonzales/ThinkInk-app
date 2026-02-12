# 🌍 Guía de Internacionalización (i18n) - ThinkInk App

## Resumen del Sistema

Se ha implementado un sistema de internacionalización (i18n) simple basado en **JSON** para permitir que ThinkInk sea **completamente bilingüe (Español/English)**.

---

## 📁 Archivos Creados

```
src/i18n/
├── __init__.py              # Exports para importar fácilmente
├── i18n_service.py          # Servicio de traducciones (lógica)
└── translations.json        # Diccionario de traducciones (ES/EN)
```

---

## 🔧 Cómo Funciona

### 1. Archivo `translations.json`
- Contiene TODAS las cadenas de texto traducidas
- Estructura: `{ "es": { key: value, ... }, "en": { key: value, ... } }`
- **+100 claves de traducción** (botones, labels, mensajes, etc.)

### 2. Servicio `i18n_service.py`
- Clase `I18nService`: Carga y gestiona traducciones
- Función `t()`: Abreviada para obtener traducciones
- Fácil de usar: `t('app_title', 'es')` → devuelve la cadena

### 3. `app.py` (Página Principal)
- Selector de idioma con botones (🇪🇸 Español / 🇬🇧 English)
- Almacena idioma en `st.session_state.language`
- TODO el contenido usa `t()` para traducción automática

---

## 📝 Cómo Usar en el Código

### Importar
```python
from src.i18n import i18n, t
```

### Obtener idioma actual (en Streamlit)
```python
import streamlit as st

lang = st.session_state.language  # 'es' o 'en'
```

### Usar traducciones

**Opción 1: Función corta `t()`** (Recomendado)
```python
title = t('app_title', lang)
st.title(title)

subtitle = t('app_subtitle', lang)
st.markdown(subtitle)
```

**Opción 2: Servicio completo**
```python
from src.i18n import i18n

title = i18n.get('app_title', lang)
st.title(title)
```

---

## 🔄 Paso a Paso: Implementar en una Página

### Ejemplo: Actualizar `pages/01_📚_Principal.py`

**ANTES (Solo español):**
```python
import streamlit as st

st.set_page_config(page_title="📚 ThinkInk - Principal", ...)
st.title("📚 Análisis Reflexivo")
st.markdown("Preguntas para mejorar tu lectura")
```

**DESPUÉS (Bilingüe):**
```python
import streamlit as st
from src.i18n import t

st.set_page_config(page_title="📚 ThinkInk", ...)

# Obtener idioma del session_state
lang = st.session_state.get('language', 'es')

# Usar traducciones
st.title(t('principal_title', lang))
st.markdown(t('principal_info_section', lang))
```

---

## 📚 Claves de Traducción Disponibles

### App Principal
- `app_title` - Título de la app
- `app_subtitle` - Subtítulo
- `language` - Selector de idioma
- `spanish` - Botón español
- `english` - Botón inglés

### Página Principal
- `principal_title` - Título de página
- `principal_pre_questions` - Preguntas previas
- `principal_post_questions` - Preguntas finales
- `principal_author_bio` - Sobre el autor
- Y más...

### Página Gemini
- `gemini_title` - Título Gemini
- `gemini_only_books` - Mensaje "solo libros"
- `input_mode` - "¿De dónde obtener?"
- `input_mode_list` - "De la lista"
- `input_mode_search` - "Búsqueda inteligente"
- Y más...

**Ver `src/i18n/translations.json` para la lista completa (~100+ claves)**

---

## 🚀 Implementación Recomendada

### Paso 1: Actualizar `pages/01_📚_Principal.py`
1. Agregar import: `from src.i18n import t`
2. Obtener idioma: `lang = st.session_state.get('language', 'es')`
3. Reemplazar strings:
   - `st.title("...")` → `st.title(t('principal_title', lang))`
   - `st.markdown("...")` → `st.markdown(t('key_name', lang))`

### Paso 2: Actualizar `pages/02_🤖_Gemini_AI.py`
1. Mismo proceso que la página Principal
2. Usar claves: `gemini_*`, `input_mode_*`, `btn_*`, etc.

### Paso 3: Verificar
```bash
# Probar en español
# Probar en inglés (cambiar botón en sidebar)
# Verificar que TODO el contenido cambie de idioma
```

---

## 💡 Tips

### Agregar Nuevas Traducciones

**En `translations.json`:**
```json
{
  "es": {
    "my_new_key": "Texto en español"
  },
  "en": {
    "my_new_key": "Text in English"
  }
}
```

**En el código:**
```python
text = t('my_new_key', lang)
```

### Mantener Consistencia
- Usar **nombres de clave descriptivos**
- Ej: `btn_summary`, `label_title`, `msg_warning`
- Facilita buscar y actualizar

### Para Cambios Multilinea
Usar múltiples líneas en JSON:
```json
"comparison_manual": "### 📚 Página Principal\n- ✅ Preguntas\n- ✅ Reflexión"
```

---

## 📊 Progreso de Implementación

| Página | Estado | Detalles |
|--------|--------|----------|
| app.py (Home) | ✅ 100% | Completamente bilingüe con selector |
| 01_Principal | ⏳ Pendiente | Necesita agregar i18n |
| 02_Gemini | ⏳ Pendiente | Necesita agregar i18n |

---

## 🔍 Validar que Funciona

### Test Rápido
```bash
streamlit run app.py
```

1. Aparecen botones 🇪🇸 y 🇬🇧 en el sidebar
2. Haz click en cada uno
3. El contenido debe cambiar de idioma
4. Los cambios son instantáneos

---

## 🐛 Troubleshooting

**Problema:** Error al importar i18n
```python
ModuleNotFoundError: No module named 'src.i18n'
```
**Solución:** Asegurar que estás en la raíz del proyecto
```bash
cd /path/to/ThinkInk-app
streamlit run app.py
```

**Problema:** Traducción no aparece, muestra la clave
```python
t('wrong_key_name', lang)  # Devuelve: 'wrong_key_name'
```
**Solución:** Verificar que la clave existe en `translations.json`

**Problema:** Cambio de idioma no se refleja
```python
lang = st.session_state.language  # NO funciona
```
**Solución:** Usar siempre con default
```python
lang = st.session_state.get('language', 'es')  # ✅ Funciona
```

---

## 📖 Referencia Rápida

```python
# ===== IMPORTAR =====
from src.i18n import i18n, t

# ===== OBTENER IDIOMA =====
lang = st.session_state.get('language', 'es')

# ===== USAR EN STREAMLIT =====
st.title(t('key_name', lang))
st.markdown(t('another_key', lang))
st.button(t('btn_submit', lang))
st.text_input(t('input_label', lang))

# ===== CONDICIONALES POR IDIOMA =====
if lang == 'es':
    # Solo español
    pass
else:
    # Solo inglés
    pass
```

---

## 🎯 Siguiente Paso

Actualizar las dos páginas principales:
1. `pages/01_📚_Principal.py` 
2. `pages/02_🤖_Gemini_AI.py`

Reemplazar todos los strings con llamadas a `t()`.

Total de strings a traducir: ~80+ por página = **160+ traducciones aprox.**

Ya está todo listo en `translations.json`, solo hay que actualizar el código.

---

**Documentación creada:** Febrero 2025  
**Sistema:** i18n basado en JSON  
**Idiomas soportados:** Español (es), Inglés (en)  
**Escalable a:** Más idiomas sin cambiar código
