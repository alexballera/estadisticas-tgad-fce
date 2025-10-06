"""
Helper para cargar datasets - Estadística I TGAD FCE-UBA

Este módulo proporciona funciones auxiliares para cargar datasets
de manera consistente en todos los notebooks del curso.
"""

from pathlib import Path
import pandas as pd


class DatasetLoader:
    """Clase para facilitar la carga de datasets del curso."""
    
    def __init__(self, notebook_path='.'):
        """
        Inicializa el cargador de datasets.
        
        Parameters:
        -----------
        notebook_path : str
            Ruta del notebook actual (usar '.' si está en la carpeta del notebook)
        """
        self.notebook_path = Path(notebook_path).resolve()
        self.data_dir = self._find_data_dir()
    
    def _find_data_dir(self):
        """Encuentra la carpeta data/ desde cualquier ubicación del proyecto."""
        current = self.notebook_path
        
        # Buscar hacia arriba hasta encontrar data/
        for _ in range(5):  # Máximo 5 niveles hacia arriba
            data_path = current / 'data'
            if data_path.exists():
                return data_path
            current = current.parent
        
        raise FileNotFoundError(
            "No se encontró la carpeta 'data/'. "
            "Asegúrate de estar en el directorio del proyecto."
        )
    
    def load_titanic(self, dataset='train'):
        """
        Carga el dataset Titanic.
        
        Parameters:
        -----------
        dataset : str
            'train', 'test', o 'submission'
        
        Returns:
        --------
        pd.DataFrame
        """
        filename_map = {
            'train': 'train.csv',
            'test': 'test.csv',
            'submission': 'gender_submission.csv'
        }
        
        if dataset not in filename_map:
            raise ValueError(f"Dataset debe ser uno de: {list(filename_map.keys())}")
        
        path = self.data_dir / 'shared' / 'titanic' / filename_map[dataset]
        return pd.read_csv(path)
    
    def load_bank(self, full=False):
        """
        Carga el dataset Banking.
        
        Parameters:
        -----------
        full : bool
            Si True, carga bank-full.csv; si False, carga bank.csv
        
        Returns:
        --------
        pd.DataFrame
        """
        filename = 'bank-full.csv' if full else 'bank.csv'
        path = self.data_dir / 'shared' / 'banking' / filename
        return pd.read_csv(path, sep=';')
    
    def load_financial(self, year):
        """
        Carga el dataset Financial Data para un año específico.
        
        Parameters:
        -----------
        year : int
            Año del dataset (2014-2018)
        
        Returns:
        --------
        pd.DataFrame
        """
        if year < 2014 or year > 2018:
            raise ValueError("El año debe estar entre 2014 y 2018")
        
        path = self.data_dir / 'shared' / 'financial' / f'{year}_Financial_Data.csv'
        return pd.read_csv(path)
    
    def load_credit_card(self):
        """
        Carga el dataset de Default Credit Card.
        
        Returns:
        --------
        pd.DataFrame
        """
        path = self.data_dir / 'shared' / 'otros' / 'default of credit card clients.xls'
        return pd.read_excel(path, header=1)
    
    def load_custom(self, relative_path):
        """
        Carga un dataset personalizado desde data/.
        
        Parameters:
        -----------
        relative_path : str
            Ruta relativa desde data/ (ej: 'U5/mi_dataset.csv')
        
        Returns:
        --------
        pd.DataFrame
        """
        path = self.data_dir / relative_path
        
        if not path.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {path}")
        
        # Detectar tipo de archivo y cargar apropiadamente
        if path.suffix == '.csv':
            return pd.read_csv(path)
        elif path.suffix in ['.xlsx', '.xls']:
            return pd.read_excel(path)
        else:
            raise ValueError(f"Tipo de archivo no soportado: {path.suffix}")
    
    def list_datasets(self):
        """Lista todos los datasets disponibles por categoría."""
        datasets = {
            'Titanic': list((self.data_dir / 'shared' / 'titanic').glob('*.csv')),
            'Banking': list((self.data_dir / 'shared' / 'banking').glob('*.csv')),
            'Financial': list((self.data_dir / 'shared' / 'financial').glob('*.csv')),
            'Otros': list((self.data_dir / 'shared' / 'otros').glob('*.*'))
        }
        
        print("📊 Datasets Disponibles:\n")
        for category, files in datasets.items():
            if files:
                print(f"  {category}:")
                for f in files:
                    size = f.stat().st_size / 1024  # KB
                    print(f"    - {f.name} ({size:.1f} KB)")
        
        return datasets


# Función de conveniencia para uso rápido
def get_loader():
    """Retorna un DatasetLoader configurado automáticamente."""
    return DatasetLoader()


# Ejemplo de uso
if __name__ == "__main__":
    # Crear loader
    loader = get_loader()
    
    # Listar datasets
    loader.list_datasets()
    
    # Cargar Titanic
    df = loader.load_titanic('train')
    print(f"\n✅ Dataset Titanic cargado: {df.shape}")
    print(df.head())
