from termcolor import cprint
import copy
import sys
from ..engine import HyperTuner

class RandomSearch(HyperTuner):
    "Basic hypertuner"

    def __init__(self, model_fn, **kwargs):
        """ RandomSearch hypertuner
        Args:
            model_name (str): used to prefix results. Default: ts

            iterations (int): number of model to test
            executions (int): number of exection for each model tested

            display_model (str): base: cpu/single gpu version, multi-gpu: multi-gpu, both: base and multi-gpu. default (Nothing)

            num_gpu (int): number of gpu to use. Default 0
            gpu_mem (int): amount of RAM per GPU. Used for batch size calculation

            local_dir (str): where to store results and models. Default results/
            gs_dir (str): Google cloud bucket to use to store results and model (optional). Default None

            dry_run (bool): do not train the model just run the pipeline. Default False
            max_fail_streak (int): number of failed model before giving up. Default 20

        """  
        cprint('-=[RandomSearch Tuning]=-', 'magenta')
        super(RandomSearch, self).__init__(model_fn, **kwargs)

    def search(self,x, y, **kwargs):
        for cur_iteration in range(self.num_iterations):
            cprint("[%s/%s instance]" % (cur_iteration, self.num_iterations), 'magenta') 
            
            instance = self.get_random_instance()
            cprint("|- model size is:%d" % instance.model_size, 'blue')
            if not instance:
                cprint("[FATAL] No valid model found - check your model_fn() function is valid", 'red')
                return
            for cur_execution in range(self.num_executions):
                cprint("|- execution: %s/%s" % (cur_execution + 1, self.num_executions), 'cyan')
                #Note: the results are not used for this tuner.
                if not self.dry_run:
                    _ = instance.fit(x, y, **kwargs)
            self.record_results()