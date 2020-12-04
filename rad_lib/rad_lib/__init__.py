from pathlib import Path
import sys
home_dir = Path().home() 
rad_dir = home_dir / 'repos/voila-eoas/libradtran'
examples_dir = home_dir / 'repos/voila-eoas/libradtran/examples'
soundings_dir = home_dir / 'repos/voila-eoas/libradtran/data/atmmod'


sys.path.insert(0, str(rad_dir))
sep='*'*30
print(f'{sep}\ncontext imported. Front of path:\n{sys.path[0]}\n')
