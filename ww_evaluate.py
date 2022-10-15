import weightwatcher as ww
from robustbench.utils import load_model
import argparse

parser = argparse.ArgumentParser(description='WW')
parser.add_argument('--attack-type', type=str, default=0, choices=['Linf', 'corruptions'], help='type of adversial attack')
parser.add_argument('--index', type=int, default=0, help='index of the model')
parser.add_argument('--dataset', type=str, default='imagenet', help='which dataset to use')

args = parser.parse_args()

# 4
# 6
model_dict = \
{
'Linf': ['Wong2020Fast', 'Engstrom2019Robustness', 'Salman2020Do_R50', 'Standard_R50'],
'corruptions': ['Geirhos2018_SIN','Geirhos2018_SIN_IN','Geirhos2018_SIN_IN_IN',
        'Hendrycks2020Many','Hendrycks2020AugMix','Standard_R50']
}

print(f"Loading Model {model_dict[args.attack_type][args.index]} of Attack {args.attack_type}")
model = load_model(model_dict[args.attack_type][args.index], 
                        model_dir=f"/work/yefan0726/checkpoints/robustbench_models/{args.attack_type}", 
                        dataset=args.dataset, 
                        threat_model=args.attack_type)

watcher = ww.WeightWatcher(model=model) 
details = watcher.analyze(plot=False, randomize=True, mp_fit=True, ww2x=False, min_evals=0, max_evals=None)


details.to_csv(f"ww_metrics/{args.attack_type}/{model_dict[args.attack_type][args.index]}.csv")
