import pickle
import os
import sys
import xamin
import ned
import models


root_dir = os.getcwd()
data_dir = os.path.abspath(root_dir + "/data/")
pickle_path = data_dir + "/prog.pickle"


def load_progress():
    if (os.path.isfile(pickle_path)) is True:
        pickle_to_import = open(pickle_path, "rb")
        return pickle.load(pickle_to_import)
    else:
        return None


def save_progress(phase_num):
    prog = {"Progress": phase_num}
    pickle_to_export = open(pickle_path, "wb")
    pickle.dump(prog, pickle_to_export)
    pickle_to_export.close()


def phase_one_data_retrieval():
    print("Retrieving all data...")
    xamin.get_all_raw()
    save_progress(2)
    phase_two_data_cleaning()


def phase_two_data_cleaning():

    save_progress(3)
    phase_three_further_data()


def phase_three_further_data():

    save_progress(4)
    phase_four_logs()


def phase_four_logs():

    save_progress(5)
    phase_five_get_sdfs()


def phase_five_get_sdfs():

    save_progress(6)
    final_phase()


def final_phase():
    print("You have finished running the data pipeline. Results are available at: data/results/")


def get_all_mining_data():
    xamin.install()
    xamin.get_all_raw()


def get_gz():
    # xamin.multi_core_download()
    # xamin.mc_gz_to_csv()
    ned.get_list_of_objects()


def mine_gz():
    pass


if __name__ == '__main__':
    system_arguments = ' '.join(sys.argv[1:])
    if system_arguments == "Download Data":
        get_gz()
        # get_all_mining_data()
    elif system_arguments == "Mine Data":
        mine_gz()
    elif system_arguments == "Train Model":
        models.train_model()
    else:
        progress = load_progress()
        if progress is None:
            phase_one_data_retrieval()
        else:
            num = progress['Progress']
            switcher = {
                1: phase_one_data_retrieval,
                2: phase_two_data_cleaning,
                3: phase_three_further_data,
                4: phase_four_logs,
                5: phase_five_get_sdfs,
                7: final_phase
            }

            current_phase = switcher.get(num, lambda: "Corrupt pickle.")
            current_phase()
