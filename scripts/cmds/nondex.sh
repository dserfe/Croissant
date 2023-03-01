testClass=$1

mvn edu.illinois:nondex-maven-plugin:2.1.1:nondex -Dtest=${testClass} -Drat.skip -Dspotbugs.skip -Denforcer.skip=true -Dcheckstyle.skip -Djacoco.skip -DnondexRuns=5
