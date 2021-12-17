from setuptools import setup
from pathlib import Path

def get_version_from_init(folder: Path=None) -> str:
      if folder is None:
            folder = Path(__file__).parent
      
      init_file = folder / 'chembl_structure_pipeline' / '__init__.py'

      with open(init_file) as fp:
            for line in fp:
                  if line.startswith('__version__'):
                        return line.split('=')[1].strip(' "\n')
      
      raise RuntimeError(f"Could not find version string in {init_file}")

setup(name='chembl_structure_pipeline',
      version=get_version_from_init(),
      description='ChEMBL Structure Pipeline',
      url='https://www.ebi.ac.uk/chembl/',
      author='Greg Landrum',
      author_email='greg.landrum@t5informatics.com',
      license='MIT',
      packages=['chembl_structure_pipeline'],
      package_data={'chembl_structure_pipeline': ['data/*']},
      zip_safe=False)
