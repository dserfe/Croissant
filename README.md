# Croissant

This repo contanis the tool of Croissant and the scripts to reproduce results.

## File structure
The directry structure of Croissant is as follows, there are also detailed README file inside each directory:

```
Croissant
   ├── scripts:                 The directory which contains all scripts to reproduce the experiments
   └── mutation_testing:        The tool for mutation testing
       
```

## Tool of mutation testing

### Environment
```
- Linux OS
- java 1.8.0
- maven 3.6.3
```

### install Croissant
```
git clone https://github.com/dserfe/Croissant
cd Croissant/mutation_testing
mvn install
```

### Running Croissant mutation testing
One can run croissant mutation testing with the following commands:

```
cd Croissant/mutation_testing
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir InputTestClassPath -o OutputTestClassPath -t Threahold -n TestClassName -mo MutationOperator -tm Template"
```

Croissant mutation configuration options:
- `-dir`: the input test class path `InputTestClassPath`
- `-o`: the output test class path `OutputTestClassPath`
- `-t`: the default `Threahold` to control NOD and ID test flakiness
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

An example to run `STDZ` mutation operator on test `org.apache.commons.csv.LexerTest` from `commons-csv` (Junit5):
```
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir ${InputPath}/commons-csv/target/test-classes -o ${OutputPath}/commons-csv/target/test-classes -t 1 -n org.apache.commons.csv.LexerTest -mo TimeZoneDependencyMO -tm TimezoneTemplate -j"
```

An example to run all NOD/ID mutation operators on test `org.apache.commons.csv.LexerTest` from `commons-csv` (Junit5):
```
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir ${InputPath}/commons-csv/target/test-classes -o ${OutputPath}/commons-csv/target/test-classes -t 1 -n org.apache.commons.csv.LexerTest -all_nod_id -j"
```

An example to run all NOD/ID mutation operators on test `org.apache.commons.cli.UtilTest` from `commons-cli` (Junit4):
```
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir ${InputPath}/commons-cli/target/test-classes -o ${OutputPath}/commons-cli/target/test-classes -t 1 -n org.apache.commons.cli.UtilTest -all_nod_id"
```

## Reproduce the results

### Set Up
To set up the experiment environment, please run the following command:

```
bash scripts/setup.sh
```

### OD results

- Input
An `input.csv` contains `url`, `sha`, and `Junit version` of each project, e.g.,
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
    ...
```

### NOD results
- Input
An `input.csv` contains `url`, `sha`, and `Junit version` of each project, e.g.,
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
    ...
```
