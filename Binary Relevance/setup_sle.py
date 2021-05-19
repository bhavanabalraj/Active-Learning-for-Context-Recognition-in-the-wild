import os

def write_job_script(label_num, run):
    folder = "label_" + str(label_num) + "/full_supervised"
    f = open(folder + "/job_script.csh", "w")
    f.write("#!/bin/tcsh\n#BSUB -n 1\n#BSUB -W 1440\n#BSUB -J " + str(label_num) + "_basic_" + str(run) + \
    "\n#BSUB -o stdout.%J\n#BSUB -e stderr.%J\n\nconda activate /share/mpsingh/bbalraj/my_env\npython -u AL_strategies_SL.py full " + str(label_num))
    f.close()

def submit_jobs(label_num):
    os.chdir("label_" + str(label_num) +"/full_supervised/")
    os.system("rm -rf std*")
    os.system("rm -rf metrics*")
    os.system("bsub < job_script.csh")
    os.chdir("../../")

for i in range(51):
  os.system("mkdir label_" + str(i))
  os.system("mkdir label_" + str(i) + "/full_supervised/")
  os.system("cp AL_strategies_SL.py label_" + str(i) + "/full_supervised/")
  os.system("cp copy_model_sl.py label_" + str(i))
  write_job_script(i, 1)
  submit_jobs(i)
