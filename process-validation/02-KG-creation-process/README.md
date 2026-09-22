# Reproducing the knowledge graph creation process

## 1. Data preparation

First, we symlink the output from the importation process into the RDFizer input folder:


```
cd process-validation/KG-creation-process/rdfizer_input/
ln -s ../../importation-process/preprocessed-datasets/GOE.json GOE.json
ln -s ../../importation-process/preprocessed-datasets/LEO.json LEO.json
ln -s ../../importation-process/preprocessed-datasets/LUH.json LUH.json
ln -s ../../importation-process/preprocessed-datasets/OSN.json OSN.json
```

## 2. Running SDM-RDFizer

Next, we run the SDM-RDFizer. Therefore, we first create and use a conda environment containing the SDM-RDFizer package and its dependencies. (For other installation options, see SDM-RDFizer [docs](https://github.com/SDM-TIB/SDM-RDFizer/tree/master#installing-and-running-the-sdm-rdfizer) and [wiki](https://github.com/SDM-TIB/SDM-RDFizer/wiki/Install&Run)). For running the RDFizer, a config file ([config.ini](./rdfizer_input/config.ini)) is prepared which is then supplied to the run command via the `-c` parameter:


```
conda create -n rdfizer rdfizer
conda activate rdfizer
python3 -m rdfizer -c config.ini
conda deactivate
```

All output files – the knowledge graph triples – are stored in the [rdfizer_triples](../KG-creation-process/rdfizer_triples/) directory as defined in the [config.ini](./rdfizer_input/config.ini) file. We obtain a single file containing all datasets per integrated research data repository in n-triples format:


```
rdfizer_triples/
├ GOE.nt
├ LEO.nt
├ LUH.nt
└ OSN.nt
```