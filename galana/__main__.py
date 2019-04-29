import pickle
import os
import sys
import xamin
import preprocessing
import models


root_dir = os.getcwd()
data_dir = os.path.abspath(root_dir + "/data/")
mine_prog_path = data_dir + "/mine_prog.pickle"
ml_prog_path = data_dir + "/ml_prog.pickle"


def load_progress(pickle_path):
    if (os.path.isfile(pickle_path)) is True:
        pickle_to_import = open(pickle_path, "rb")
        return pickle.load(pickle_to_import)
    else:
        return None


def save_progress(phase_num, pickle_path):
    prog = {"Progress": phase_num}
    pickle_to_export = open(pickle_path, "wb")
    pickle.dump(prog, pickle_to_export)
    pickle_to_export.close()


def mine_phase_one_data_retrieval():
    print("Retrieving all data...")
    xamin.multi_core_download()
    save_progress(2, mine_prog_path)
    mine_phase_two_data_preprocessing()


def mine_phase_two_data_preprocessing():
    print("Cleaning data...")
    xamin.mc_gz_to_csv()
    preprocessing.canonicalize_galaxies()
    save_progress(3, mine_prog_path)
    mine_phase_three_clustering()


def mine_phase_three_clustering():
    # save_progress(5, mine_prog_path)
    # mine_final_phase()
    pass


def mine_final_phase():
    print("You have finished running the data pipeline. Results are available at: data/results/")


if __name__ == '__main__':
    system_arguments = ' '.join(sys.argv[1:])


def manip_images(train_image_path, train_sols, clean_sols, augmented_sols):
    preprocessing.process_kaggle(train_sols, clean_sols)
    preprocessing.update_solutions(clean_sols, augmented_sols)
    preprocessing.augment_images(train_image_path, clean_sols)


if __name__ == '__main__':
    model_paths = models.initialize_default_paths()
    system_arguments = ' '.join(sys.argv[1:])
    if system_arguments == "Manip Data":
        manip_images(model_paths.train_image_path, model_paths.train_solutions, model_paths.clean_train_solutions, model_paths.augmented_solutions)
    elif system_arguments == "Train Model":
        models.train_model(model_paths)
    elif system_arguments == "Train Transfer Model":
        model_paths = models.initialize_default_paths()
        preprocessing.process_kaggle(model_paths.train_solutions, model_paths.clean_train_solutions)
        models.train_model(model_paths, transfer=True)
    elif system_arguments == "Crop":
        model_paths = models.initialize_default_paths()
        preprocessing.crop_all(model_paths.train_image_path)
    elif system_arguments == "Mine":
        progress = load_progress(mine_prog_path)
        if progress is None:
            mine_phase_one_data_retrieval()
        else:
            num = progress['Progress']
            switcher = {
                1: mine_phase_one_data_retrieval,
                2: mine_phase_two_data_preprocessing(),
                3: mine_phase_three_clustering(),
                4: mine_final_phase
            }

            current_phase = switcher.get(num, lambda: "Corrupt pickle.")
            current_phase()

    # elif system_arguments == "ML":
    #     progress = load_progress(ml_prog_path)
    #     if progress is None:
    #         ml_phase_one_data_retrieval()
    #     else:
    #         num = progress['Progress']
    #         switcher = {
    #             1: phase_one_data_retrieval,
    #             2: phase_two_data_cleaning,
    #             3: phase_three_further_data,
    #             4: phase_four_logs,
    #             5: phase_five_get_sdfs,
    #             7: final_phase
    #         }
    #
    #         current_phase = switcher.get(num, lambda: "Corrupt pickle.")
    #         current_phase()
