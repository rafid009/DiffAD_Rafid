import pandas as pd
import numpy as np

swat_folder = 'tf_dataset/swat'
synth_folder = 'tf_dataset/synth'

swat_train = pd.read_csv(f"{swat_folder}/swat_train.csv")
swat_test = pd.read_csv(f"{swat_folder}/swat_test.csv")
synth_train = pd.read_csv(f"{synth_folder}/synth_train.csv")
synth_test = pd.read_csv(f"{synth_folder}/synth_test.csv")

swat_mean = swat_train.to_numpy().nanmean(axis=0)
synth_mean = synth_train.to_numpy()..nanmean(axis=0)
swat_std = swat_train.to_numpy()..nanstd(axis=0)
synth_std = synth_train.to_numpy()..nanstd(axis=0)
swat_train = (swat_train - swat_mean) / swat_std
swat_train.to_csv(f"{swat_folder}/swat_train.csv", index=False)
swat_test = (swat_test - swat_mean) / swat_std
swat_test.to_csv(f"{swat_folder}/swat_test.csv", index=False)
np.save(f"{swat_folder}/swat_mean.npy", swat_mean.to_numpy())
np.save(f"{swat_folder}/swat_std.npy", swat_std.to_numpy())
synth_train = (synth_train - synth_mean) / synth_std
synth_train.to_csv(f"{synth_folder}/synth_train.csv", index=False)
synth_test = (synth_test - synth_mean) / synth_std
synth_test.to_csv(f"{synth_folder}/synth_test.csv", index=False)
np.save(f"{synth_folder}/synth_mean.npy", synth_mean.to_numpy())
np.save(f"{synth_folder}/synth_std.npy", synth_std.to_numpy())

