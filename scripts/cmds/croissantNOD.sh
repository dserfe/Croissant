module=$1
testClass=$2
junit=$3

if [ $junit == '4' ]; then
    timeout 1200s mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir ${module}/test-classes -o ${module}/test-classes -t 1 -n ${testClass}"
else
    timeout 1200s mvn exec:java -Dexec.mainClass=com.framework.App -Dexec.args="-dir ${module}/test-classes -o ${module}/test-classes -t 1 -n ${testClass} -j"
fi