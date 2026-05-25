import sys
from pathlib import Path

# Add project root to sys.path for imports
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
