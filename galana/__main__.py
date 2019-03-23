import pickle
import os
import sys
import data


root_dir = os.getcwd()
data_dir = os.path.abspath(root_dir + "/data/")
pickle_path = data_dir + "/prog.pickle"
bash_script_loc = root_dir + "/utils/"


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
    phase_six_get_descriptors()


def phase_six_get_descriptors():

    save_progress(7)


def final_phase():
    print("You have finished running the data pipeline. Results are available at: data/results/")


def get_all_mining_data():
    print(data.get_all_tables())


if __name__ == '__main__':
    if ' '.join(sys.argv[1:]) == "Get All Mining Data":
        get_all_mining_data()
    # progress = load_progress()
    # if progress is None:
    #     phase_one_data_retrieval()
    # else:
    #     num = progress['Progress']
    #     switcher = {
    #         1: phase_one_data_retrieval,
    #         2: phase_two_data_cleaning,
    #         3: phase_three_further_data,
    #         4: phase_four_logs,
    #         5: phase_five_get_sdfs,
    #         6: phase_six_get_descriptors,
    #         7: final_phase
    #     }
    #
    #     current_phase = switcher.get(num, lambda: "Corrupt pickle.")
    #     current_phase()
