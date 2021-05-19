import os

strategies = ["random", "entropy", "mean_margin", "lcp"]

def create_dir_copy_model(strategy):
    os.system("mkdir " + strategy)
    os.system("sudo cp full_supervised/data_split.pickle " + strategy + "/")
    os.system("sudo cp full_supervised/initial_model_dict.pt " + strategy + "/")
    os.system("sudo cp full_supervised/AL_strategies_ES.py " + strategy + "/")

def write_job_script(strategy, run):
    f = open(strategy + "/job_script.csh", "w")
    f.write("#!/bin/tcsh\n#BSUB -n 1\n#BSUB -W 1440\n#BSUB -J " + strategy + "_full_" + str(run) + \
    "\n#BSUB -o stdout.%J\n#BSUB -e stderr.%J\n\nconda activate /share/mpsingh/bbalraj/my_env\npython -u AL_strategies_ES.py " + strategy + ' 1000')
    f.close()

def submit_jobs(strategy):
    os.chdir(strategy)
    os.system("rm -rf std*")
    os.system("rm -rf metrics*")
    os.system("bsub < job_script.csh")
    os.chdir("../")

def main():
    for strategy in strategies:
        create_dir_copy_model(strategy)
        write_job_script(strategy, 1)
        submit_jobs(strategy)

if __name__ == "__main__":
    main()
