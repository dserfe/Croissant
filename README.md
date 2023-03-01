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
mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir InputTestClassPath -o OutputTestClassPath -t Threahold -n TestClass -mo MutationOperator -tm Template"
```

Croissant mutation configuration options:
- `-dir`: the input test class path
- `-o`: the output test class path
- `-t`: the default threahold to control NOD and ID test flakiness
- `-n`: the name of the test class to mutate 
- `-mo`: the mutation operator selected
- `-tm`: the mutation template selected
- `-all_nod_id`: an option to run all NOD and ID mutation operators automatically
- `-all_od`: an option to run all OD mutation operators automatically

One can change `mutation.threshold` to control flakiness of NOD and ID mutants, or change `mutation.count` to control the number of cleaners for OD mutants. The two properties are configured in `target/test-classes/mutation.config`, which can be changed during runtime:
```
mutation.threshold=0.8 # value from 0 to 1
mutation.count=5 # value from 0 to 50
```
## Reproduce the results

### Set Up
To set up the experiment environment, please following command:

```
bash setup.sh
```

### OD results
#### Input
#### Output

### NOD results
#### Input
#### Output
