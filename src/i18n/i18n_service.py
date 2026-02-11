import json
import os
from typing import Dict, Any

class I18nService:
    """Servicio de internacionalización (i18n) para ThinkInk"""
    
    def __init__(self):
        """Inicializa el servicio de traducciones"""
        # Obtener ruta al archivo de traducciones
        current_dir = os.path.dirname(os.path.abspath(__file__))
        translations_file = os.path.join(current_dir, 'translations.json')
        
        # Cargar traducciones
        with open(translations_file, 'r', encoding='utf-8') as f:
            self.translations: Dict[str, Dict[str, str]] = json.load(f)
        
        # Idiomas disponibles
        self.available_languages = list(self.translations.keys())
        self.default_language = 'es'
    
    def get(self, key: str, language: str = 'es') -> str:
        """
        Obtiene una cadena traducida
        
        Args:
            key: Clave de traducción (ej: 'app_title')
            language: Código de idioma ('es' o 'en')
            
        Returns:
            Cadena traducida, o la clave si no existe
        """
        # Si el idioma no existe, usa el por defecto
        if language not in self.translations:
            language = self.default_language
        
        # Obtener traducción
        return self.translations[language].get(key, key)
    
    def translate_dict(self, lang: str) -> Dict[str, str]:
        """
        Obtiene un diccionario completo de traducciones para un idioma
        
        Args:
            lang: Código de idioma
            
        Returns:
            Diccionario con todas las traducciones del idioma
        """
        return self.translations.get(lang, self.translations[self.default_language])


# Instancia global para usar en toda la app
i18n = I18nService()


def t(key: str, lang: str = 'es') -> str:
    """
    Función abreviada para obtener traducciones
    
    Uso:
    from src.i18n.i18n_service import t
    
    title = t('app_title', 'es')
    """
    return i18n.get(key, lang)
