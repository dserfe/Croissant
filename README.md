# Croissant

This repo contanis the tool of Croissant mutation testing and the scripts to reproduce results.

## File structure
The directory structure of Croissant is as follows:

```
Croissant
   ├── scripts:                 The directory which contains all scripts to reproduce the experiments
   └── mutation_testing:        The tool for mutation testing
       
```

## Tool of mutation testing

### Environment

- Linux OS
- java 1.8.0
- maven 3.6.3

Please download the source code of projects from https://zenodo.org/record/7690720#.ZABSAS-B35g to reproduce the results, since there are some dependencies changed in some projects to make them work well.


### Install Croissant mutation tool
```
git clone https://github.com/dserfe/Croissant
cd Croissant/mutation_testing
mvn install
```

### Run Croissant mutation tool
One can run croissant mutation testing with the following commands:

```
cd Croissant/mutation_testing
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir InputTestClassPath -o OutputTestClassPath -t Threahold -n TestClassName -mo MutationOperator -tm Template <-j>"
```

Croissant mutation configuration options:
- `-dir`: the input test class path `InputTestClassPath`
- `-o`: the output test class path `OutputTestClassPath`; In order to run detection tools on mutants, please configure the output path in original project test class path, which is the same as input path `InputTestClassPath`
- `-t`: the default `Threshold` to control NOD and ID test flakiness
- `-n`: the name of the test class `TestClassName` to mutate 
- `-mo`: the mutation operator selected 
- `-tm`: the mutation template selected
- `-j`: The default mutation is on Junit4 tests. When mutate on Junit5 tests, please add `-j` option
- `-all_nod_id`: an option to run all NOD and ID mutation operators automatically
- `-all_od`: an option to run all OD mutation operators automatically

One can change `mutation.threshold` to control flakiness of NOD and ID mutants, or change `mutation.count` to control the number of cleaners for OD mutants. The two properties are configured in `target/test-classes/mutation.config`, which can be changed during runtime:
```
mutation.threshold=0.8 # value from 0 to 1
mutation.count=5 # value from 0 to 50
```
To run generated mutants with surefire, one can run with Surefire, e.g., to run mutants in test `org.apache.commons.csv.LexerTest` from `commons-csv`:
```
cd commons-csv
mvn sirefire:test -Dtest=org.apache.commons.csv.LexerTest
```

Examples:
- An example to get `STDZ` mutants on test `org.apache.commons.csv.LexerTest` from `commons-csv` (Junit5):
```
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir ${path}/commons-csv/target/test-classes -o ${path}/commons-csv/target/test-classes -t 1 -n org.apache.commons.csv.LexerTest -mo TimeZoneDependencyMO -tm TimezoneTemplate -j"
```

- An example to run all NOD/ID mutation operators on test `org.apache.commons.csv.LexerTest` from `commons-csv` (Junit5):
```
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir ${path}/commons-csv/target/test-classes -o ${path}/commons-csv/target/test-classes -t 1 -n org.apache.commons.csv.LexerTest -all_nod_id -j"
```

- An example to run all NOD/ID mutation operators on test `org.apache.commons.cli.UtilTest` from `commons-cli` (Junit4):
```
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir ${path}/commons-cli/target/test-classes -o ${path}/commons-cli/target/test-classes -t 1 -n org.apache.commons.cli.UtilTest -all_nod_id"
```

## Reproduce the results

### Set Up
To set up the experiment environment, please run the following command:

```
bash scripts/setup.sh
```
Please download the source code of projects from https://zenodo.org/record/7690720#.ZABSAS-B35g to reproduce the results, since there are some dependencies changed in some projects to make them work well. Then move all the projects into `scripts/projects`.

### Reproduce NOD/ID results

This section is to reproduce the results of evaluating Surefire/NonDex with NOD/ID mutants. The following commands will 1) run all NOD and ID mutation operators on each project 2) run Surefire and NonDex on NOD/ID mutants with thresholds changing from 0.1 to 1:

- Input

An `input.csv` contains `url`, `sha`, and `junit version` of each project, e.g.,
```
https://github.com/apache/commons-cli,8adbf64def81ee3e812e802a398ef5afbbfc69ee,4
...
```
- Run the commands:

```
cd scripts
bash all_nod.sh input.csv 
```
- Output

An `output` folder will be generated, for each run, a `TimeStamp1` folder will be generated which includes `logs`, `results`, `mutant` for each project
```
output
   ├── TimeStamp1
    │   ├── results
    │   ├── logs
    │   └── mutant
   ├── TimeStamp2 
    │   ├── results
    │   ├── logs
    │   └── mutant
    └── ...
```
- Demo

This is a demo to generate NOD and ID mutants on `commons-codec`, and then run NonDex and Surefire on the mutants:
```
cd scripts
bash all_nod.sh projects/codec.csv
```

### Reproduce OD results

This section is to reproduce the results of evaluating iDFlakies with OD mutants. The following commands will 1) run all OD mutation operators on each project 2) run iDFlakies on OD mutants with the number of cleaners chaning from 0 to 50:

- Input

An `input.csv` contains `url`, `sha`, and `junit version` of each project, e.g.,
```
https://github.com/apache/commons-cli,8adbf64def81ee3e812e802a398ef5afbbfc69ee,4
...
```
- Run the commands:

```
cd scripts
bash all_od.sh input.csv 
```
- Output

An `output` folder will be generated, for each run, a `TimeStamp1` folder will be generated which includes `logs`, `results`, `mutant` for each project
```
output
   ├── TimeStamp1
    │   ├── results
    │   ├── logs
    │   └── mutant
   ├── TimeStamp2 
    │   ├── results
    │   ├── logs
    │   └── mutant
    └── ...
```
- Demo

This is a demo to generate OD mutants on `commons-codec`, and then iDFlakies on the mutants:
```
cd scripts
bash all_od.sh projects/codec.csv
```
