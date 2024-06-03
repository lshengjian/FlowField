from typing import List
from omegaconf import OmegaConf,DictConfig
from pathlib import Path
from functools import lru_cache
cache_cfg={}
def load_config()->List[str]:
    global cache_cfg
    root_path=Path(__file__).parent.parent.parent
    app_file = root_path/'conf/app.yaml'
    cfg = OmegaConf.load(app_file)
    print(OmegaConf.to_yaml(cfg))
    problems_dir:Path = root_path/'conf/problems'
    ps= problems_dir.rglob('*.yaml')
    cache_cfg['main']=cfg
    rt=[]
    for p in ps:
        cfg=OmegaConf.load(p)
        cache_cfg[p.stem]=cfg
        rt.append(p.stem)
        #print(OmegaConf.to_yaml(cfg))
    return rt
@lru_cache(maxsize=10) 
def get_config(pname:str='01_fall')->DictConfig:
    if len(cache_cfg)<2:
        load_config()
    cfg = OmegaConf.merge(cache_cfg['main'], cache_cfg[pname])
    return cfg

   
if __name__ == "__main__":
    print(get_config())
