# Reproducing the dataset importation process

The basic dataset importation process including API calls and raw metadata handling is described in the [README.md](../../Mapping_files/README.md#importation-process) of the [Mapping_files directory](../../Mapping_files/).

Below are the steps to obtain one file for each of the imported reasearch dataset repositores (GOE, LEO, LUH, OSN) as input for the SDM-RDFizer.

- **Input:** directory containing json files (mapped to LDM) for each reasearch dataset repository (GOE, LEO, LUH, OSN).
- **Processing:** `python3 process-validation/importation-process/preprocess_dataset.py GOE`
- **Output:** One file containing all preprocessed datasets for each repository.

```
preprocessed-datasets/
├ GOE.json
├ LEO.json
├ LUH.json
└ OSN.json
```
